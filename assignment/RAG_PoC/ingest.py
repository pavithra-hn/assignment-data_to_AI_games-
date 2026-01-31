# ingest.py - Create embeddings and persist to vector store
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data")
PERSIST_DIR = "vector_db"

# Choose embedding backend based on env
USE_OPENAI = bool(os.getenv("OPENAI_API_KEY"))

from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def load_documents(data_dir: Path):
    """Load markdown, text, pdf from folder."""
    docs = []
    
    for path in data_dir.rglob("*"):
        if path.is_file():
            try:
                if path.suffix.lower() == ".pdf":
                    loader = PyPDFLoader(str(path))
                    docs.extend(loader.load())
                    print(f"  [OK] {path.name} (PDF)")
                elif path.suffix.lower() in [".md", ".markdown"]:
                    loader = UnstructuredMarkdownLoader(str(path))
                    docs.extend(loader.load())
                    print(f"  [OK] {path.name} (Markdown)")
                elif path.suffix.lower() == ".txt":
                    loader = TextLoader(str(path), encoding="utf8")
                    docs.extend(loader.load())
                    print(f"  [OK] {path.name} (Text)")
            except Exception as e:
                print(f"  [ERROR] {path.name}: {e}")
    
    return docs


def main():
    print("=" * 60)
    print("  RAG PoC - Document Ingestion")
    print("=" * 60)
    
    # Check data directory
    if not DATA_DIR.exists():
        print(f"\n[ERROR] Data directory '{DATA_DIR}' not found.")
        print("  Create it and add your documents (PDF, MD, TXT)")
        return
    
    # Load documents
    print("\n[STEP 1] Loading documents...")
    docs = load_documents(DATA_DIR)
    print(f"\n  Loaded {len(docs)} document(s)")
    
    if not docs:
        print("\n[ERROR] No documents found in data/ folder")
        return
    
    # Split into chunks
    print("\n[STEP 2] Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)
    print(f"  Created {len(chunks)} chunks")
    
    # Create embeddings
    print("\n[STEP 3] Creating embeddings...")
    if USE_OPENAI:
        print("  Using OpenAI Embeddings")
        embeddings = OpenAIEmbeddings()
    else:
        print("  Using HuggingFace sentence-transformers (local)")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    # Persist to Chroma
    print("\n[STEP 4] Persisting to Chroma vector store...")
    
    # Remove existing DB if present
    if Path(PERSIST_DIR).exists():
        import shutil
        shutil.rmtree(PERSIST_DIR)
        print("  Removed existing vector database")
    
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    
    print(f"\n[DONE] Vector database persisted to: {PERSIST_DIR}/")
    print(f"  Total chunks indexed: {len(chunks)}")
    print("\nNext: Run 'python query.py' to ask questions")


if __name__ == "__main__":
    main()
