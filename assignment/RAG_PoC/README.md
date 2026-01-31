# Digital Employee RAG PoC

A Retrieval-Augmented Generation (RAG) Proof of Concept for a Digital Employee assistant.

---

## Architecture

```
+------------------+     +------------------+     +------------------+
|   Documents      |     |   Embeddings     |     |   Vector Store   |
|   (PDF/MD/TXT)   | --> |   (OpenAI or     | --> |   (ChromaDB)     |
|                  |     |    HuggingFace)  |     |                  |
+------------------+     +------------------+     +--------+---------+
                                                          |
                             ingest.py                    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - | - - - - -
                             query.py                     |
                                                          v
+------------------+     +------------------+     +------------------+
|   User Query     | --> |   Retriever      | --> |   Top-K Chunks   |
|                  |     |   (Similarity)   |     |   + Sources      |
+------------------+     +------------------+     +--------+---------+
                                                          |
                                                          v
+------------------+     +------------------+     +------------------+
|   Final Answer   | <-- |   OpenAI GPT     | <-- |   Prompt +       |
|   + Sources      |     |   (LLM)          |     |   Context        |
+------------------+     +------------------+     +------------------+
```

---

## Project Structure

```
RAG_PoC/
|-- ingest.py            # Ingest documents -> Create embeddings -> Persist
|-- query.py             # Load vector DB -> Retrieve -> Answer
|-- data/                # Put your documents here
|   |-- handbook.md
|   +-- policy.txt
|-- vector_db/           # ChromaDB persistence (created by ingest.py)
|-- requirements.txt     # Python dependencies
|-- .env                 # API keys
+-- README.md            # This file
```

---

## Quick Start

### 1. Install Dependencies

```bash
cd RAG_PoC
pip install -r requirements.txt
```

### 2. Configure API Key

Create `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Add Documents

Put your PDF, Markdown, or Text files in `data/` folder.

### 4. Ingest Documents

```bash
python ingest.py
```

Output:
```
============================================================
  RAG PoC - Document Ingestion
============================================================

[STEP 1] Loading documents...
  [OK] handbook.md (Markdown)
  [OK] policy.txt (Text)

  Loaded 2 document(s)

[STEP 2] Splitting into chunks...
  Created 4 chunks

[STEP 3] Creating embeddings...
  Using OpenAI Embeddings

[STEP 4] Persisting to Chroma vector store...

[DONE] Vector database persisted to: vector_db/
  Total chunks indexed: 4
```

### 5. Query Documents

```bash
python query.py
```

Output:
```
============================================================
  RAG PoC - Query Interface
============================================================

[INFO] Loading vector database...
[INFO] Using OpenAI GPT-3.5-turbo

============================================================
  Ready! Ask questions about your documents.
  Type 'exit' or 'quit' to stop.
============================================================

Your Question: How long do we retain customer data?

[Searching...]

--- Answer ---
According to the Data Retention Policy, customer data is retained for 
3 years from the last interaction. After 3 years, data will be 
anonymized or deleted. Customers can also request data deletion at any time.

--- Sources (retrieved chunks) ---

[1] Source: policy.txt
    Content: Data Retention Policy...Customer data will be retained 
    for 3 years from the last interaction...
----------------------------------------
```

---

## Features

| Feature | Implementation |
|---------|----------------|
| Document Loading | PDF, Markdown, Text via LangChain loaders |
| Text Chunking | RecursiveCharacterTextSplitter (1000 chars, 200 overlap) |
| Embeddings | OpenAI or HuggingFace sentence-transformers |
| Vector Store | ChromaDB with persistence |
| Retrieval | Similarity search, top-4 chunks |
| LLM | OpenAI GPT-3.5-turbo |
| Source Tracking | Returns source documents with answers |

---

## Sample Questions

| Question | Expected Answer Source |
|----------|------------------------|
| How long do we retain customer data? | policy.txt |
| Who must complete security training? | handbook.md |
| What encryption is required for PII? | policy.txt |
| What is the approved chat platform? | handbook.md |

---

## Configuration

### Using Local Embeddings (No OpenAI for embeddings)

If you don't set `OPENAI_API_KEY`, the system uses local HuggingFace embeddings:
```
sentence-transformers/all-MiniLM-L6-v2
```

Note: LLM still requires OpenAI API key for answer generation.

### Changing Chunk Size

Edit `ingest.py`:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,    # Adjust this
    chunk_overlap=200   # Adjust this
)
```

### Changing Number of Retrieved Chunks

Edit `query.py`:
```python
retriever = vectordb.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}  # Change to retrieve more/fewer chunks
)
```

---

## Files

| File | Purpose |
|------|---------|
| `ingest.py` | Load documents, create embeddings, persist to ChromaDB |
| `query.py` | Load vector DB, retrieve chunks, generate answers |
| `rag_demo.py` | Simple standalone demo (alternative) |
| `requirements.txt` | Python dependencies |

---

## Production Notes

- **Better Chunking**: Use semantic-aware chunkers or split by sections
- **Retrieval**: Experiment with `mmr` search type for diversity
- **Security**: Use local embeddings for sensitive data
- **Scaling**: Use managed vector DBs (Pinecone, Weaviate)
- **Monitoring**: Log queries, responses, and sources

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Vector database not found` | Run `python ingest.py` first |
| `OPENAI_API_KEY not found` | Add key to `.env` file |
| `No documents found` | Add files to `data/` folder |

---

**Built with LangChain + ChromaDB + OpenAI**
