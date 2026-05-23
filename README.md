# 🎓 CourseMate AI
### *Retrieval Augmented Generation — Study Assistant*

> **CourseMate AI** is an AI-powered study assistant designed to help students interact with their learning materials more efficiently. Modern students rely on multiple sources of study material such as lecture notes, textbooks, PDFs, and research papers. These documents are often long and difficult to navigate, making it time-consuming to find specific information.

---

## 🧠 What is RAG?

| Component | Role |
|-----------|------|
| **LLM** (e.g. Claude) | Powerful language model — but has no access to your study data |
| **Your Documents** | PDFs, notes, textbooks — the knowledge base |
| **RAG Pipeline** | Connects external data to the LLM → context-aware answers |

```
External Data Sources ──► Pipeline ──► Context-Aware LLM Responses
                                           = RAG Application
```

---

## 🗺️ Development Plan

> We'll follow each step below and build the full project along the way.

---

## Pipeline Overview

```
📄 Upload Docs  ──►  📦 Load  ──►  ✂️ Chunk  ──►  🔢 Embed
                                                        │
💬 User Query  ──►  🔢 Embed  ──►  🔍 Search  ──►  🧩 Retrieve  ──►  🤖 LLM Answer
```

---

## Step-by-Step Breakdown

### Step 1 — User Uploads Study Material

Students upload learning resources such as:

- 📄 PDFs
- 📝 Lecture notes
- 📚 Textbooks
- 🔬 Research papers

---

### Step 2 — Document Loading

The system loads documents using **document loaders**.

**Goal:** Convert raw files into document objects that can be processed. You may clean the document as well.

---

### Step 3 — Text Splitting (Chunking)

Documents are usually too large for **LLM context windows**.

> Using an LLM, we write prompts — but there's a token limit called the **Context Window**. So we split documents into smaller chunks.

✅ Chunking improves retrieval accuracy.

---

### Step 4 — Embedding Generation

Each chunk is converted into a **vector embedding**.

Embedding models transform text into numerical vectors that represent **semantic meaning**:

```
"Gradient Descent Optimization"
           ↓
  [0.23, -0.81, 0.44, ...]
```

---

### Step 5 — Vector Database Storage

All embeddings are stored inside a **vector database**.

The vector database stores:

| Data | Description |
|------|-------------|
| `embeddings` | Numerical vector representations |
| `original text chunks` | The actual content |
| `metadata` | Source, page number, etc. |

---

### Step 6 — User Asks a Question

Now the student interacts with the system. 💬

---

### Step 7 — Query Embedding

The question is **also converted into an embedding** using the same embedding model.

---

### Step 8 — Similarity Search

The vector database performs **semantic similarity search**.

**Goal:** Find chunks that are most relevant to the question.

---

### Step 9 — Retriever Component

The retriever selects the **top-k relevant chunks**.
These chunks form the **context** passed to the LLM.

---

### Step 10 — LLM Answers

Based on the retrieved context, the **LLM generates a precise, grounded answer**. 🎯

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

## 📦 Document Loader Integration

> Any kind of document loaded through LangChain is converted into a **Document object** containing two fields:

| Field | Description |
|-------|-------------|
| `page_content` | The actual text content of the document |
| `metadata` | Source info — file path, page number, etc. |

**Example output:**
```python
[Document(metadata={'source': 'document_loaders/notes.txt'}, page_content='Hello how are you \n\nI want to see what can I do and also I need your help \nplease help me')]
```

---

## 🧪 Code — Basic Document Loader

**`test.py`**
```python
from langchain_community.document_loaders import TextLoader

data = TextLoader("document_loaders/notes.txt")
docs = data.load()

print(docs)                  # full document object
print(len(docs))             # number of documents
print(docs[0].page_content)  # the actual text
print(docs[0].metadata)      # file path metadata
print("1st:", docs[0])
```

---

## 🤖 Code — Document Loader + LLM Integration

**`main.py`**
```python
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = TextLoader("document_loaders/notes.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}")
    ]
)

model = ChatMistralAI(model="mistral-small-latest")

prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)

print(result.content)
```

---

*CourseMate AI — Making study materials smarter, one chunk at a time.*