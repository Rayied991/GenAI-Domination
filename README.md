# Project Phases & Development Roadmap
# Phase-1: Research Layer

# Phase-2: Bedrock models:
someone researched a topic and published a paper, but they dont have funding/money so they cant implement it. here comes some big company from this  paper they make a bedrock models.
# Phase-3: Providers:
these bedrock model became providers.
providers are LLM.

# Phase-4: 
This is where youn comes in picture 

You are going to use these LLM models and create some great AI applications.


# Plan of Action:
- 1.LLM foundation
- 2. RAG System
- 3. Agentic AI
- 4. Project and deployment


# What is LLM?

LLM= Large Language Model
Now break it into 3 words:

1. Large
    - It is trained on a huge amount of text data. (books,websites,wikipedia,articles,code,conversations, etc..).
2. Language
    - It understands and generates human language.
    Like English,Hindi,Spanish... even programming languages like Python.

3. Model
    - It is a deep learning system (a neural network ) that learns patterns from data.

- When you type : "What is Python?"[converts to number(embeddings)->[0.0,1,1,1.1,1,1,0.2,0.2...]]

 The LLM does NOT:
 - Search Google
 - Think like a Human
 - Understand meaning like we do

Instead It:
 - Looks at patterns it learned.
 - Predicts the next most likely word
 - Keeps predicting word by word.

Some Popular LLMs:
- GPT Models
- Gemini Models
- LLaMa
- Claude
- Grok
- Mistral ... etc

How to use these models:

Problem:
If every provider has a different SDK, different syntax, different response format... How do we build scalable AI applications?
- LangChain is the solution.

# Langchain Components:
 1. Models
 2. Prompts
 3. Chains
 4. Memory
 5. Indexes
 6. Agents


# Models:
Models are the core intelligent layer. They generate text,embeddings or other outputs. They connect your application to LLM providers like:
- OpenAI
- Google DeepMind
- Anthropic

In a practical Generative AI, there are mainly 3 important types of models:

1. Chat/ Language Models

- Generate text
- Answer questions
- Write code
- Summarize content
2. Embedding Models

- Convert text into numbers (vectors)
- Used in search & RAG
- Help find similar content

3. MultiModal Models
- Work with more than just text
- Can process images, audio or files

# Prompts:

A prompt is the instruction we give to a language model,

It tells the model:
- What to do
- How to respond
- What format to use

Without prompts, the model has no direction.

LLMs are powerful but they are not mind readers.
The quality of output depends on:
- How clearly we instruct them.
- Better prompt -> Better output.

# Types of Prompts:
1. Simple Prompt:
Just a direct instruction.
Example:
Explain what is Machine Learning.
Basic. Straightforward.

2. System + User Prompt
Modern chat models use roles:

- System → Sets behavior
- User → Asks question

Example:
System:
You are a helpful AI teacher.
User:
Explain LLMs in simple terms.
System controls tone and style.

3. Prompt Templates
Instead of writing prompts manually every time, we create reusable templates.
Example:
Explain {topic} in simple terms.
Now you can replace {topic} dynamically.
This is useful in applications.

4. Structured Prompts
Used when we want:

-JSON output
-Bullet points
-Fixed format

Example:
Respond in json format with keys:
definition , example
This makes output machine readable.

# Chains:
- A chain is a sequence of steps connected together.
Instead of:
One prompt-> One response
We create:
Step 1->Step 2-> Step 3->final output.

Real AI applications are not one-step.
Example:
User asks:
Summarize this article and translate it into Hindi.
What actually happens?

- Summarize text
- Translate summary
- Return result

That's a chain.
# Memory:

Memory allows the AI system to remember past interactions.
Without memory:
Every message is treated independently.
With memory:
The model can use previous context.

Example:
User: My name is Akarsh.
Later...
User: What is my name?
Without memory → Model doesn't know.
With memory → It remembers.

# Indexes:

Indexes allow us to connect external data to an LLM.
LLMs only know what they were trained on.
Indexes help them use:

- PDFs
- Documents
- Databases
- Company data
- Websites

LLMs:
❌ Don't know your company data
❌ Don't know private documents
❌ Don't update in real-time
So how do we solve this?
We connect external knowledge.
That system is called Retrieval.

# Agents:

Agents are AI systems that can decide what action to take.
Unlike normal chains:
Chains → Follow fixed steps
Agents → Decide the next step dynamically.

Normal LLM:
User → Prompt → Response
But what if the task requires:

- Searching the web
- Doing calculations
- Calling an API
- Using a database

The LLM alone cannot do that.
It needs tools.

virtual env:
uv:[https://docs.astral.sh/uv/#__tabbed_1_2]
PS D:\Gen-AI> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
downloading uv 0.11.8 (x86_64-pc-windows-msvc)
installing to C:\Users\Rayied\.local\bin                                                                                                                                                       
  uv.exe                                                                                                                                                                                       
  uvx.exe                                                                                                                                                                                      
  uvw.exe                                                                                                                                                                                      
everything's installed!                                                                                                                                                                        

To add C:\Users\Rayied\.local\bin to your PATH, either restart your shell or run:

    set Path=C:\Users\Rayied\.local\bin;%Path%   (cmd)
    $env:Path = "C:\Users\Rayied\.local\bin;$env:Path"   (powershell)
PS D:\Gen-AI> $env:Path = "C:\Users\Rayied\.local\bin;$env:Path"

virtual env:
uv venv
.venv\Scripts\activate

Requirements.txt:
langchain
langchain-core
langchain-community
langgraph
langchain-openai
langchain-google-genai
langchain-groq
langchain-mistralai
python-dotenv
faiss-cpu
tiktoken
fastapi
uvicorn
requests
langchain_huggingface

uv pip install -r requirements.txt