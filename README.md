# Basic RAG (Retrieval-Augmented Generation)

A simple Retrieval-Augmented Generation (RAG) project built from scratch to understand how modern AI document search works without relying on high-level frameworks.

## Features

* Document ingestion from text files
* Sentence chunking with configurable overlap
* Embedding generation using a Sentence Transformer model
* Cosine similarity-based semantic search
* Top-k chunk retrieval
* LLM integration for answering questions
* Source attribution for retrieved answers
* Similarity threshold to avoid unnecessary LLM calls

## Project Flow

```text
Documents
    │
    ▼
Chunking
    │
    ▼
Generate Embeddings
    │
    ▼
Store Chunks + Embeddings
    │
    ▼
User Question
    │
    ▼
Generate Question Embedding
    │
    ▼
Cosine Similarity Search
    │
    ▼
Retrieve Top Chunks
    │
    ▼
LLM
    │
    ▼
Grounded Answer + Source
```

## Tech Stack

* Python
* sentence-transformers
* NumPy
* Ollama / OpenAI-compatible LLM (depending on your setup)

## Example

**Question**

```
Can we use Spring with Java?
```

**Answer**

```
Yes. Spring Framework is designed to work with the Java platform.

Source:
documents/spring.txt
```

## Project Structure

```
basic-rag/
│
├── documents/
│   ├── java.txt
│   ├── python.txt
│   └── spring.txt
│
├── chunker.py
├── embeddings.py
├── similarity.py
├── retriever.py
├── main.py
└── README.md
```

## What I Learned

* How embeddings represent semantic meaning
* Why chunking is important in RAG
* How cosine similarity retrieves relevant information
* How Retrieval-Augmented Generation works internally
* How to ground LLM responses using retrieved context
* Why similarity thresholds help reduce hallucinations and unnecessary LLM calls

## Future Improvements

* Replace brute-force similarity search with FAISS
* Support PDF ingestion
* Store metadata alongside chunks
* Use a vector database such as ChromaDB or Qdrant
* Add a simple web interface
* Add conversation history and memory
