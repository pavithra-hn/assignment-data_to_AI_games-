# query.py - Retrieve and answer using RAG
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

PERSIST_DIR = "vector_db"
USE_OPENAI = bool(os.getenv("OPENAI_API_KEY"))


def get_embeddings():
    """Get embedding model (same as used during ingestion)."""
    if USE_OPENAI:
        return OpenAIEmbeddings()
    else:
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )


def format_docs(docs):
    """Format retrieved documents into context string."""
    return "\n\n".join(doc.page_content for doc in docs)


def main():
    print("=" * 60)
    print("  RAG PoC - Query Interface")
    print("=" * 60)
    
    # Check vector DB exists
    if not os.path.exists(PERSIST_DIR):
        print(f"\n[ERROR] Vector database not found at '{PERSIST_DIR}'")
        print("  Run 'python ingest.py' first to create the database")
        return
    
    # Load embeddings
    print("\n[INFO] Loading vector database...")
    embeddings = get_embeddings()
    
    # Load persisted Chroma
    vectordb = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )
    
    # Create retriever
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    
    # Create LLM
    if USE_OPENAI:
        print("[INFO] Using OpenAI GPT-3.5-turbo")
        llm = ChatOpenAI(
            temperature=0.0,
            model="gpt-3.5-turbo"
        )
    else:
        print("[ERROR] OPENAI_API_KEY not found.")
        print("  Set OPENAI_API_KEY in .env file or use a local LLM")
        return
    
    # Create prompt template
    template = """You are a helpful Digital Employee Assistant. 
Answer the question based ONLY on the following context. 
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: {question}

Answer:"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create RAG chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    print("\n" + "=" * 60)
    print("  Ready! Ask questions about your documents.")
    print("  Type 'exit' or 'quit' to stop.")
    print("=" * 60)
    
    while True:
        print()
        query = input("Your Question: ").strip()
        
        if not query:
            continue
        
        if query.lower() in ("exit", "quit"):
            print("\nGoodbye!")
            break
        
        try:
            # Get relevant docs for source display
            print("\n[Searching...]")
            docs = retriever.invoke(query)
            
            # Show sources
            print("\n--- Sources ---")
            for i, doc in enumerate(docs, start=1):
                source = os.path.basename(doc.metadata.get("source", "unknown"))
                print(f"  [{i}] {source}")
            
            # Generate answer
            print("\n[Generating answer...]")
            answer = rag_chain.invoke(query)
            
            # Print answer
            print("\n--- Answer ---")
            print(answer)
            
            # Print source content
            print("\n--- Source Details ---")
            for i, doc in enumerate(docs, start=1):
                source = os.path.basename(doc.metadata.get("source", "unknown"))
                print(f"\n[{i}] {source}")
                print(f"    {doc.page_content[:150]}...")
                print("-" * 40)
                
        except Exception as e:
            print(f"\n[ERROR] {e}")


if __name__ == "__main__":
    main()

