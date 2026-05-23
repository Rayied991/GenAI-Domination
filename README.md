# 🎓 CourseMate AI
### Retrieval Augmented Generation — Study Assistant

> **CourseMate AI** is an AI-powered study assistant that helps students interact with their learning materials more efficiently. Modern students rely on multiple sources — lecture notes, textbooks, PDFs, and research papers — which are often long and difficult to navigate.

---

## 🧠 What is RAG?

RAG (Retrieval Augmented Generation) bridges the gap between a powerful LLM and your personal study data.

| Component | Role |
|-----------|------|
| **LLM** (e.g. Claude, Mistral) | Powerful language model — but has no access to your documents |
| **Your Documents** | PDFs, notes, textbooks — the knowledge base |
| **RAG Pipeline** | Connects external data to the LLM → context-aware answers |

```
External Data Sources ──► Pipeline ──► Context-Aware LLM Responses
                                            = RAG Application
```

---

## 🗺️ Full Pipeline Overview

```
📄 Upload Docs  ──►  📦 Load  ──►  ✂️ Chunk  ──►  🔢 Embed  ──►  🗄️ Store
                                                                        │
💬 User Query  ──►  🔢 Embed  ──►  🔍 Search  ──►  🧩 Retrieve  ──►  🤖 LLM Answer
```

---

## 📋 Step-by-Step Breakdown

### Step 1 — Upload Study Material

Students upload learning resources such as:

- 📄 PDFs
- 📝 Lecture notes
- 📚 Textbooks
- 🔬 Research papers

---

### Step 2 — Document Loading

The system loads files using **document loaders**, converting raw files into structured `Document` objects ready for processing.

Every `Document` object has two fields:

| Field | Description |
|-------|-------------|
| `page_content` | The actual text content of the document |
| `metadata` | Source info — file path, page number, etc. |

**Example output:**
```python
[Document(
    metadata={'source': 'document_loaders/notes.txt'},
    page_content='Hello how are you\n\nI want to see what can I do...'
)]
```

---

### Step 3 — Text Splitting (Chunking)

Documents are usually too large to fit inside an **LLM's context window** (the token limit for a single prompt). So we split them into smaller, manageable chunks.

> ✅ Chunking improves retrieval accuracy by allowing precise matching between the query and relevant sections.

---

### Step 4 — Embedding Generation

Each chunk is converted into a **vector embedding** — a numerical representation of its semantic meaning.

```
"Gradient Descent Optimization"
           ↓  Embedding Model
  [0.23, -0.81, 0.44, 0.67, ...]
```

Two pieces of text with similar meaning will have embeddings that are numerically close together, enabling semantic search.

---

### Step 5 — Vector Database Storage

All embeddings are stored in a **vector database** alongside their original content.

| Stored Data | Description |
|-------------|-------------|
| `embeddings` | Numerical vector representations |
| `original text chunks` | The actual content |
| `metadata` | Source file, page number, etc. |

---

### Step 6 — User Asks a Question

The student types a question into the interface. 💬

---

### Step 7 — Query Embedding

The question is **also converted into an embedding** using the same embedding model used during ingestion. This ensures the query and documents live in the same vector space.

---

### Step 8 — Similarity Search

The vector database performs a **semantic similarity search**, comparing the query embedding against all stored chunk embeddings.

**Goal:** Find the chunks most relevant to the question — even if they use different wording.

---

### Step 9 — Retrieval

The retriever selects the **top-k most relevant chunks**. These chunks form the **context** that gets passed to the LLM.

---

### Step 10 — LLM Generates an Answer

Based on the retrieved context, the LLM generates a **precise, grounded answer** — citing only information from the student's own study materials. 🎯

---

## 🏗️ RAG Core Components

```
RAG (Retrieval Augmented Generation)
├── 1. Document Loader
├── 2. Text Splitter
├── 3. Vector Database
└── 4. Retriever
```

---

## 💻 Code Examples

### Basic Text Document Loader

```python
# test.py
from langchain_community.document_loaders import TextLoader

data = TextLoader("document_loaders/notes.txt")
docs = data.load()

print(docs)                   # Full document object
print(len(docs))              # Number of documents loaded
print(docs[0].page_content)  # The actual text
print(docs[0].metadata)      # File path metadata
```

---

### Text Loader + LLM Integration

```python
# main.py
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load document
data = TextLoader("document_loaders/notes.txt")
docs = data.load()

# Define prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes the text"),
    ("human", "{data}")
])

# Initialize model
model = ChatMistralAI(model="mistral-small-latest")

# Run
prompt = template.format_messages(data=docs[0].page_content)
result = model.invoke(prompt)
print(result.content)
```

---

### PDF Loader + LLM Integration

```python
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = PyPDFLoader("document_loaders/GRU.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI that summarizes the text"),
    ("human", "{data}")
])

model = ChatMistralAI(model="mistral-small-latest")

prompt = template.format_messages(data=docs[0].page_content)
result = model.invoke(prompt)
print(result.content)
```

---

### Web-Based Loader

```python
from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/macbook-pro/"

data = WebBaseLoader(url)
docs = data.load()

print(len(docs))              # Number of pages loaded
print(docs[0].page_content)  # Scraped page content
```

---

## 📦 Loader Summary

| Loader | Import | Use Case |
|--------|--------|----------|
| `TextLoader` | `langchain_community.document_loaders` | Plain `.txt` files |
| `PyPDFLoader` | `langchain_community.document_loaders` | PDF documents |
| `WebBaseLoader` | `langchain_community.document_loaders` | Web pages / URLs |

---

*CourseMate AI — Making study materials smarter, one chunk at a time.*