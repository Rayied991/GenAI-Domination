# Project Phases & Development Roadmap

## Phase 1: Research Layer
Researchers study and publish papers on AI topics.

## Phase 2: Bedrock Models
Big companies take those research papers and implement them into foundational (bedrock) models.

## Phase 3: Providers
These bedrock models become providers — they are the LLMs.

## Phase 4: You
This is where **you** come in. You use these LLM models to create great AI applications.

---

# Plan of Action

1. LLM Foundation
2. RAG System
3. Agentic AI
4. Project and Deployment

---

# What is LLM?

**LLM = Large Language Model**

Break it into 3 words:

### 1. Large
- Trained on a huge amount of text data (books, websites, Wikipedia, articles, code, conversations, etc.)

### 2. Language
- Understands and generates human language (English, Hindi, Spanish... even programming languages like Python)

### 3. Model
- A deep learning system (a neural network) that learns patterns from data

> When you type: `"What is Python?"` → it converts to numbers (embeddings) → `[0.0, 1, 1, 1.1, 1, 1, 0.2, 0.2...]`

### The LLM does NOT:
- Search Google
- Think like a human
- Understand meaning like we do

### Instead, it:
- Looks at patterns it learned
- Predicts the next most likely word
- Keeps predicting word by word

### Some Popular LLMs:
- GPT Models
- Gemini Models
- LLaMA
- Claude
- Grok
- Mistral

---

# The Problem & Solution

If every provider has a different SDK, different syntax, different response format... how do we build scalable AI applications?

**LangChain is the solution.**

---

# LangChain Components

1. Models
2. Prompts
3. Chains
4. Memory
5. Indexes
6. Agents

---

# 1. Models

Models are the core intelligent layer. They generate text, embeddings, or other outputs. They connect your application to LLM providers like OpenAI, Google DeepMind, and Anthropic.

### Types of Models:

**Chat / Language Models**
- Generate text
- Answer questions
- Write code
- Summarize content

**Embedding Models**
- Convert text into numbers (vectors)
- Used in search & RAG
- Help find similar content

**MultiModal Models**
- Work with more than just text
- Can process images, audio, or files

---

# 2. Prompts

A prompt is the instruction we give to a language model. It tells the model:
- What to do
- How to respond
- What format to use

> Without prompts, the model has no direction. Better prompt → Better output.

### Types of Prompts:

**1. Simple Prompt**
Just a direct instruction.
```
Explain what is Machine Learning.
```
Basic. Straightforward.

**2. System + User Prompt**
Modern chat models use roles:
- System → Sets behavior
- User → Asks question

```
System: You are a helpful AI teacher.
User: Explain LLMs in simple terms.
```
System controls tone and style.

**3. Prompt Templates**
Instead of writing prompts manually every time, we create reusable templates.
```
Explain {topic} in simple terms.
```
Now you can replace `{topic}` dynamically. This is useful in applications.

**4. Structured Prompts**
Used when we want:
- JSON output
- Bullet points
- Fixed format

```
Respond in JSON format with keys: definition, example
```
This makes output machine-readable.

---

# 3. Chains

A chain is a sequence of steps connected together.

Instead of: `One prompt → One response`

We create: `Step 1 → Step 2 → Step 3 → Final Output`

### Example:
User asks: *"Summarize this article and translate it into Hindi."*

What actually happens:
1. Summarize text
2. Translate summary
3. Return result

**That's a chain.**

---

# 4. Memory

Memory allows the AI system to remember past interactions.

- **Without memory:** Every message is treated independently.
- **With memory:** The model can use previous context.

### Example:
```
User: My name is Akarsh.
Later...
User: What is my name?
```
- Without memory → Model doesn't know.
- With memory → It remembers.

---

# 5. Indexes

Indexes allow us to connect external data to an LLM. LLMs only know what they were trained on. Indexes help them use:

- PDFs
- Documents
- Databases
- Company data
- Websites

### The Problem:
LLMs:
- ❌ Don't know your company data
- ❌ Don't know private documents
- ❌ Don't update in real-time

### The Solution:
We connect external knowledge. That system is called **Retrieval**.

---

# 6. Agents

Agents are AI systems that can decide what action to take.

| | |
|---|---|
| Chains | Follow fixed steps |
| Agents | Decide the next step dynamically |

### Why Agents?

Normal LLM: `User → Prompt → Response`

But what if the task requires:
- Searching the web
- Doing calculations
- Calling an API
- Using a database

The LLM alone cannot do that. **It needs tools.**