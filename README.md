# The AI Engineering Handbook

> **A comprehensive, evolving handbook for AI Engineering - from fundamentals to production systems**

This handbook is designed to grow with your learning journey. It covers everything from AI basics to building production-ready AI agents, with space for continuous additions as you learn and discover new concepts.

---

## � **New Here? [START HERE →](START_HERE.md)**

**Quick Links**:
- 📖 [5-Minute Quick Start](START_HERE.md#5-minute-quick-start)
- 💻 [Run First Example](START_HERE.md#run-your-first-example)
- 🗺️ [Learning Paths](START_HERE.md#learning-paths)
- 📚 [Full Handbook Index](HANDBOOK_INDEX.md)

---

## � Handbook Navigation

### Part I: Foundations
1. [Introduction to AI Engineering](#introduction-to-ai-engineering)
2. [Handbook Structure](#handbook-structure)
3.## 🎯 Choose Your Path

### 👨‍🎓 **I'm New to AI**
**Start Here**: [Complete Beginner Guide](START_HERE.md#beginner-path-weeks-1-2)
1. Read [AI Foundations](handbook/01-foundations/README.md)
2. Run [First Example](START_HERE.md#run-your-first-example)
3. Follow [Week 1-2 Path](START_HERE.md#beginner-path-weeks-1-2)

### 💻 **I Want to Code**
**Start Here**: [Quick Start](START_HERE.md#5-minute-quick-start)
1. Setup in 2 minutes
2. Run `python integrations/gemini_integration.py`
3. Browse [Code Examples](examples/README.md)

### 🏗️ **I'm Building a Project**
**Start Here**: [Project Templates](templates/)
1. Choose template (Chatbot, RAG, Agent)
2. Copy to `poc/your-project/`
3. Follow template README

### 📚 **I Need Reference**
**Start Here**: [Handbook Index](HANDBOOK_INDEX.md)
1. Search [Glossary](reference/GLOSSARY.md)
2. Browse by topic
3. Check [Troubleshooting](handbook/18-troubleshooting/README.md)

---

## Quick Start Guide

Follow these steps to get started:

### 1. Environment Setup

### Part II: Core Knowledge
5. [AI & Machine Learning Fundamentals](handbook/01-foundations/README.md)
6. [Large Language Models (LLMs)](handbook/02-llm-fundamentals/README.md)
7. [Prompt Engineering](handbook/03-prompt-engineering/README.md)
8. [Embeddings & Vector Databases](handbook/04-embeddings-vectors/README.md)

### Part III: Building AI Systems
9. [AI Agent Architecture](handbook/05-agent-architecture/README.md)
10. [Memory & Context Management](handbook/06-memory-context/README.md)
11. [RAG (Retrieval Augmented Generation)](handbook/07-rag-systems/README.md)
12. [Tool Use & Function Calling](handbook/08-tools-functions/README.md)

### Part IV: Advanced Topics
13. [Multi-Agent Systems](handbook/09-multi-agent/README.md)
14. [LLM Frameworks (LangChain, LlamaIndex)](handbook/10-frameworks/README.md)
15. [Fine-tuning & Custom Models](handbook/11-fine-tuning/README.md)
16. [Multimodal AI](handbook/12-multimodal/README.md)

### Part V: Production & Deployment
17. [Security & Best Practices](handbook/13-security/README.md)
18. [Performance Optimization](handbook/14-optimization/README.md)
19. [Monitoring & Observability](handbook/15-monitoring/README.md)
20. [Production Deployment](handbook/16-deployment/README.md)

### Part VI: Practical Implementation
21. [Code Examples & Patterns](examples/README.md)
22. [POC Projects](poc/README.md)
23. [Case Studies](handbook/17-case-studies/README.md)
24. [Troubleshooting Guide](handbook/18-troubleshooting/README.md)

### Part VII: Reference & Resources
25. [API References](reference/README.md)
26. [Glossary](reference/GLOSSARY.md)
27. [External Resources](reference/RESOURCES.md)
28. [Your Learning Journey](PROGRESS.md)

---

## Introduction to AI Engineering

**AI Engineering** is the practice of building, deploying, and maintaining AI-powered applications and systems.

### Key Aspects

**Traditional Software Engineering:**
- Write deterministic code
- Predictable outputs
- Rule-based logic

**AI Engineering:**
- Work with probabilistic models
- Handle uncertainty
- Prompt-based interactions
- Continuous learning and adaptation

### AI Engineer vs ML Engineer

| Aspect | ML Engineer | AI Engineer |
|--------|-------------|-------------|
| **Focus** | Model training & optimization | Application development |
| **Skills** | Statistics, algorithms, data science | Software engineering, APIs, integration |
| **Output** | Trained models | Production applications |
| **Tools** | TensorFlow, PyTorch, scikit-learn | LangChain, LlamaIndex, APIs |
| **Workflow** | Data → Train → Evaluate → Deploy | Design → Integrate → Deploy → Monitor |

### Why AI Engineering?

✅ **Rapid Development**: Build AI apps without training models  
✅ **Leverage Existing Models**: Use GPT, Gemini, Claude, etc.  
✅ **Focus on Value**: Solve business problems, not ML research  
✅ **Scalability**: Production-ready systems  
✅ **Integration**: Connect AI with existing systems  

---

## Handbook Structure

This handbook is organized for progressive learning and easy expansion:

```
ai-engineering-handbook/
│
├── README.md                          # This handbook index
├── SETUP.md                           # Environment setup
├── LEARNING_ROADMAP.md               # Structured learning paths
├── PROGRESS.md                        # Your learning tracker
├── requirements.txt                   # Dependencies
├── .env.example                       # Configuration template
│
├── handbook/                          # 📚 Main handbook content
│   │
│   ├── 01-foundations/               # Part II: Core Knowledge
│   │   ├── README.md                 # AI/ML fundamentals overview
│   │   ├── 01-what-is-ai.md         # Introduction to AI
│   │   ├── 02-ml-basics.md          # Machine Learning
│   │   ├── 03-deep-learning.md      # Neural Networks
│   │   └── 04-ai-engineering.md     # AI Engineering role
│   │
│   ├── 02-llm-fundamentals/         # LLM deep dive
│   │   ├── README.md                 # LLM overview
│   │   ├── 01-how-llms-work.md      # Architecture & training
│   │   ├── 02-tokens.md             # Tokenization
│   │   ├── 03-context-windows.md    # Context management
│   │   ├── 04-parameters.md         # Temperature, top-p, etc.
│   │   └── 05-model-comparison.md   # GPT, Gemini, Claude, etc.
│   │
│   ├── 03-prompt-engineering/       # Prompting techniques
│   │   ├── README.md                 # Prompt engineering guide
│   │   ├── 01-basics.md             # Basic prompting
│   │   ├── 02-zero-shot.md          # Zero-shot learning
│   │   ├── 03-few-shot.md           # Few-shot learning
│   │   ├── 04-chain-of-thought.md   # CoT prompting
│   │   ├── 05-advanced-techniques.md # Advanced patterns
│   │   └── 06-prompt-templates.md   # Reusable templates
│   │
│   ├── 04-embeddings-vectors/       # Embeddings & vector DBs
│   │   ├── README.md                 # Embeddings overview
│   │   ├── 01-what-are-embeddings.md
│   │   ├── 02-creating-embeddings.md
│   │   ├── 03-vector-databases.md   # Pinecone, Chroma, etc.
│   │   ├── 04-similarity-search.md
│   │   └── 05-use-cases.md
│   │
│   ├── 05-agent-architecture/       # Part III: Building AI Systems
│   │   ├── README.md                 # Agent architecture
│   │   ├── 01-what-are-agents.md
│   │   ├── 02-react-pattern.md      # Reasoning + Acting
│   │   ├── 03-agent-components.md
│   │   ├── 04-decision-making.md
│   │   └── diagrams/                # Architecture diagrams
│   │
│   ├── 06-memory-context/           # Memory systems
│   │   ├── README.md
│   │   ├── 01-short-term-memory.md  # Conversation history
│   │   ├── 02-long-term-memory.md   # Persistent storage
│   │   ├── 03-working-memory.md     # Active context
│   │   └── 04-memory-strategies.md
│   │
│   ├── 07-rag-systems/              # RAG implementation
│   │   ├── README.md                 # RAG overview
│   │   ├── 01-rag-architecture.md
│   │   ├── 02-document-processing.md
│   │   ├── 03-retrieval-strategies.md
│   │   ├── 04-generation.md
│   │   └── 05-evaluation.md
│   │
│   ├── 08-tools-functions/          # Tool use & function calling
│   │   ├── README.md
│   │   ├── 01-function-calling.md
│   │   ├── 02-tool-design.md
│   │   ├── 03-tool-execution.md
│   │   └── 04-error-handling.md
│   │
│   ├── 09-multi-agent/              # Part IV: Advanced Topics
│   │   ├── README.md
│   │   ├── 01-multi-agent-patterns.md
│   │   ├── 02-communication.md
│   │   ├── 03-orchestration.md
│   │   └── 04-use-cases.md
│   │
│   ├── 10-frameworks/               # LangChain, LlamaIndex, etc.
│   │   ├── README.md
│   │   ├── 01-langchain/
│   │   ├── 02-llamaindex/
│   │   ├── 03-autogen/
│   │   └── 04-comparison.md
│   │
│   ├── 11-fine-tuning/              # Custom models
│   │   ├── README.md
│   │   ├── 01-when-to-fine-tune.md
│   │   ├── 02-data-preparation.md
│   │   ├── 03-training.md
│   │   └── 04-evaluation.md
│   │
│   ├── 12-multimodal/               # Vision, audio, etc.
│   │   ├── README.md
│   │   ├── 01-vision-models.md
│   │   ├── 02-audio-processing.md
│   │   └── 03-multimodal-agents.md
│   │
│   ├── 13-security/                 # Part V: Production
│   │   ├── README.md
│   │   ├── 01-api-key-management.md
│   │   ├── 02-input-validation.md
│   │   ├── 03-rate-limiting.md
│   │   ├── 04-data-privacy.md
│   │   └── 05-security-checklist.md
│   │
│   ├── 14-optimization/             # Performance tuning
│   │   ├── README.md
│   │   ├── 01-token-optimization.md
│   │   ├── 02-caching.md
│   │   ├── 03-latency-reduction.md
│   │   └── 04-cost-optimization.md
│   │
│   ├── 15-monitoring/               # Observability
│   │   ├── README.md
│   │   ├── 01-logging.md
│   │   ├── 02-metrics.md
│   │   ├── 03-tracing.md
│   │   └── 04-alerting.md
│   │
│   ├── 16-deployment/               # Production deployment
│   │   ├── README.md
│   │   ├── 01-deployment-options.md
│   │   ├── 02-containerization.md
│   │   ├── 03-scaling.md
│   │   └── 04-ci-cd.md
│   │
│   ├── 17-case-studies/             # Real-world examples
│   │   ├── README.md
│   │   ├── 01-chatbot.md
│   │   ├── 02-document-qa.md
│   │   ├── 03-code-assistant.md
│   │   └── 04-research-agent.md
│   │
│   └── 18-troubleshooting/          # Common issues
│       ├── README.md
│       ├── 01-api-errors.md
│       ├── 02-performance-issues.md
│       └── 03-debugging-guide.md
│
├── examples/                          # 💻 Part VI: Code Examples
│   ├── README.md                     # Examples index
│   ├── 01-basic/                     # Basic examples
│   │   ├── hello_llm.py
│   │   ├── simple_chat.py
│   │   └── token_counter.py
│   ├── 02-prompting/                 # Prompt examples
│   │   ├── zero_shot.py
│   │   ├── few_shot.py
│   │   └── chain_of_thought.py
│   ├── 03-embeddings/                # Embedding examples
│   │   ├── create_embeddings.py
│   │   ├── similarity_search.py
│   │   └── vector_db_demo.py
│   ├── 04-agents/                    # Agent examples
│   │   ├── simple_agent.py
│   │   ├── react_agent.py
│   │   └── tool_using_agent.py
│   ├── 05-rag/                       # RAG examples
│   │   ├── basic_rag.py
│   │   ├── advanced_rag.py
│   │   └── rag_evaluation.py
│   ├── 06-multi-agent/               # Multi-agent examples
│   │   ├── research_team.py
│   │   └── orchestrator.py
│   └── 07-production/                # Production examples
│       ├── secure_agent.py
│       ├── monitored_agent.py
│       └── cached_agent.py
│
├── poc/                               # 🚀 Your POC projects
│   ├── README.md                     # POC documentation
│   ├── simple-chatbot/               # Project 1
│   ├── document-qa/                  # Project 2
│   ├── ai-agent/                     # Project 3
│   └── templates/                    # Project templates
│
├── integrations/                      # 🔌 LLM provider integrations
│   ├── README.md
│   ├── gemini/
│   │   ├── basic.py
│   │   ├── advanced.py
│   │   └── streaming.py
│   ├── openai/
│   ├── anthropic/
│   └── local-models/
│
├── notebooks/                         # 📓 Jupyter experiments
│   ├── README.md
│   ├── 01-llm-exploration.ipynb
│   ├── 02-prompt-testing.ipynb
│   ├── 03-embeddings-demo.ipynb
│   └── 04-agent-experiments.ipynb
│
├── reference/                         # 📖 Part VII: Reference
│   ├── README.md                     # Reference index
│   ├── GLOSSARY.md                   # AI/ML terminology
│   ├── RESOURCES.md                  # External resources
│   ├── api-reference/                # API documentation
│   │   ├── gemini.md
│   │   ├── openai.md
│   │   └── anthropic.md
│   └── cheatsheets/                  # Quick references
│       ├── prompting.md
│       ├── langchain.md
│       └── vector-dbs.md
│
├── templates/                         # 📝 Reusable templates
│   ├── agent-template/
│   ├── rag-template/
│   └── project-template/
│
└── your-notes/                        # ✍️ Your personal notes
    ├── README.md                     # Notes index
    ├── discoveries/                  # Things you discovered
    ├── experiments/                  # Experiment results
    └── ideas/                        # Future project ideas
```

---

## Learning Path

### 🎯 Beginner (Weeks 1-2)

**Objectives:**
- Understand what AI and ML are
- Learn LLM basics
- Make first API call to LLM
- Understand tokens and embeddings

**Topics:**
1. AI/ML fundamentals → `basics/`
2. What are LLMs → `llm-concepts/01_what_are_llms.md`
3. Tokens & embeddings → `llm-concepts/02_tokens_embeddings.md`
4. First LLM API call → `integrations/gemini_integration.py`

**Hands-on:**
- Set up environment
- Run basic prompt examples
- Experiment with different prompts
- Understand token counting

### 🚀 Intermediate (Weeks 3-4)

**Objectives:**
- Master prompt engineering
- Understand context and memory
- Build simple AI agent
- Learn RAG (Retrieval Augmented Generation)

**Topics:**
1. Prompt engineering → `llm-concepts/03_prompt_engineering.md`
2. Context & memory → `llm-concepts/04_context_memory.md`
3. Agent architecture → `architecture/01_agent_architecture.md`
4. Build first agent → `poc/examples/simple_chat.py`

**Hands-on:**
- Design effective prompts
- Implement conversation memory
- Build simple chatbot
- Create RAG system

### 🏆 Advanced (Weeks 5-8)

**Objectives:**
- Design complex AI systems
- Implement multi-agent workflows
- Production deployment
- Monitoring and optimization

**Topics:**
1. Workflows → `architecture/02_workflows.md`
2. Orchestration → `architecture/03_orchestration.md`
3. Multi-agent systems → `poc/examples/multi_agent.py`
4. Production best practices → `security/`

**Hands-on:**
- Build multi-agent system
- Implement tool calling
- Deploy to production
- Monitor and optimize

---

## Quick Start

### Prerequisites
- Python 3.8+
- API key for LLM provider (Gemini, OpenAI, etc.)
- Basic Python knowledge

### Installation

```bash
# Clone repository
cd "/Users/5149844/windsurf/personal learning/learning/ai-engineering-learning-poc"

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

### First LLM Call

```python
# Run your first LLM interaction
python integrations/gemini_integration.py

# Or try the simple chat example
python poc/examples/simple_chat.py
```

### Explore Examples

```bash
# Basic prompts
python llm-concepts/examples/basic_prompts.py

# Embeddings demo
python llm-concepts/examples/embeddings_demo.py

# RAG example
python poc/examples/rag_example.py
```

---

## Core Concepts

### 1. Large Language Models (LLMs)

**What are LLMs?**
- Neural networks trained on massive text data
- Predict next token based on context
- Can generate human-like text
- Understand and follow instructions

**Popular LLMs:**
- **Google Gemini**: Multimodal, fast, cost-effective
- **OpenAI GPT-4**: Powerful, versatile
- **Anthropic Claude**: Long context, safe
- **Meta Llama**: Open-source

**Key Properties:**
- **Context Window**: How much text they can process (e.g., 128K tokens)
- **Temperature**: Randomness in responses (0 = deterministic, 1 = creative)
- **Max Tokens**: Maximum response length

### 2. Tokens

**What are Tokens?**
- Chunks of text (words, subwords, characters)
- LLMs process text as tokens
- Pricing based on token count

**Examples:**
```
"Hello, world!" → ["Hello", ",", " world", "!"] = 4 tokens
"AI Engineering" → ["AI", " Engineering"] = 2 tokens
```

**Why Tokens Matter:**
- **Cost**: Pay per token (input + output)
- **Limits**: Context window measured in tokens
- **Performance**: More tokens = slower, more expensive

**Token Counting:**
```python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4")
tokens = encoder.encode("Hello, world!")
print(f"Token count: {len(tokens)}")
```

### 3. Embeddings

**What are Embeddings?**
- Numerical representations of text
- Capture semantic meaning
- Enable similarity search

**Vector Representation:**
```
"cat" → [0.2, 0.8, 0.1, ..., 0.5]  (1536 dimensions)
"dog" → [0.3, 0.7, 0.2, ..., 0.4]  (similar to cat)
"car" → [0.9, 0.1, 0.8, ..., 0.2]  (different from cat)
```

**Use Cases:**
- Semantic search
- Similarity matching
- Clustering
- Recommendation systems
- RAG (Retrieval Augmented Generation)

**Creating Embeddings:**
```python
from openai import OpenAI

client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-ada-002",
    input="Your text here"
)
embedding = response.data[0].embedding
```

### 4. Prompt Engineering

**What is Prompt Engineering?**
- Crafting effective instructions for LLMs
- Getting desired outputs
- Optimizing quality and consistency

**Prompt Structure:**
```
[System Message]  ← Define role and behavior
[Context]         ← Provide background information
[Instruction]     ← Clear task description
[Examples]        ← Few-shot learning (optional)
[Input]           ← User input or data
[Output Format]   ← Specify desired format
```

**Techniques:**
- **Zero-shot**: No examples, just instruction
- **Few-shot**: Provide examples
- **Chain-of-thought**: Ask to explain reasoning
- **Role-playing**: "You are an expert..."
- **Format specification**: JSON, markdown, etc.

**Example:**
```python
prompt = """
You are a helpful AI assistant specialized in Python programming.

Task: Explain the following code in simple terms.

Code:
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```

Provide:
1. What the code does
2. How it works
3. Example usage
"""
```

### 5. Memory in AI Agents

**Why Memory?**
- Maintain conversation context
- Remember user preferences
- Learn from interactions
- Provide personalized responses

**Types of Memory:**

**Short-term Memory (Conversation History):**
```python
conversation_history = [
    {"role": "user", "content": "What's the weather?"},
    {"role": "assistant", "content": "I don't have real-time data..."},
    {"role": "user", "content": "Can you check it?"}
]
```

**Long-term Memory (Vector Database):**
```python
# Store important information
vector_db.store(
    text="User prefers Python over JavaScript",
    metadata={"user_id": "123", "type": "preference"}
)

# Retrieve relevant memories
memories = vector_db.search("programming language preference")
```

**Working Memory (Current Context):**
- Current task
- Active tools
- Intermediate results

### 6. Context Window

**What is Context Window?**
- Maximum tokens LLM can process at once
- Includes: system message + history + current input + output

**Examples:**
- GPT-3.5: 4K tokens
- GPT-4: 8K-128K tokens
- Gemini 1.5 Pro: 1M tokens
- Claude 3: 200K tokens

**Managing Context:**
```python
# Summarize old messages
if total_tokens > context_limit:
    summary = summarize_conversation(old_messages)
    conversation_history = [summary] + recent_messages
```

### 7. RAG (Retrieval Augmented Generation)

**What is RAG?**
- Enhance LLM with external knowledge
- Retrieve relevant information
- Generate informed responses

**How RAG Works:**
```
1. User Query → "What's our refund policy?"
2. Embed Query → [0.2, 0.8, ...]
3. Search Vector DB → Find similar documents
4. Retrieve Context → "Refund policy: 30 days..."
5. Augment Prompt → Query + Retrieved Context
6. Generate Response → LLM produces answer
```

**Benefits:**
- Up-to-date information
- Domain-specific knowledge
- Reduced hallucinations
- Verifiable sources

---

## AI Agent Architecture

### What is an AI Agent?

An AI agent is a system that:
- **Perceives**: Receives input from users/environment
- **Reasons**: Uses LLM to understand and plan
- **Acts**: Takes actions via tools/APIs
- **Learns**: Improves through feedback

### Basic Agent Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      AI Agent                            │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   User       │────────►│   Input Processing   │
│   Input      │         │   (Parse, validate)  │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Memory System      │
                         │  - Conversation      │
                         │  - Long-term         │
                         │  - Working           │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   LLM (Brain)        │
                         │  - Reasoning         │
                         │  - Planning          │
                         │  - Decision making   │
                         └──────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌──────────┐    ┌──────────┐    ┌──────────┐
            │  Tool 1  │    │  Tool 2  │    │  Tool N  │
            │  (API)   │    │  (DB)    │    │  (Code)  │
            └──────────┘    └──────────┘    └──────────┘
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Response           │
                         │   Generation         │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   User Output        │
                         └──────────────────────┘
```

### Components Explained

**1. Input Processing**
- Parse user input
- Validate and sanitize
- Extract intent

**2. Memory System**
- Store conversation history
- Retrieve relevant context
- Manage working memory

**3. LLM (Brain)**
- Understand user intent
- Plan actions
- Generate responses
- Decide which tools to use

**4. Tools/Functions**
- External APIs
- Database queries
- Code execution
- File operations
- Web search

**5. Response Generation**
- Format output
- Add context
- Ensure quality

### Agent Patterns

**1. ReAct (Reasoning + Acting)**
```
Thought: I need to find the weather
Action: call_weather_api("New York")
Observation: 72°F, sunny
Thought: I have the information
Response: "It's 72°F and sunny in New York"
```

**2. Chain-of-Thought**
```
Step 1: Understand the question
Step 2: Break down the problem
Step 3: Solve each part
Step 4: Combine results
```

**3. Multi-Agent**
```
Researcher Agent → Gathers information
Analyst Agent → Analyzes data
Writer Agent → Creates report
```

---

## Setup Instructions

See detailed guide in [SETUP.md](SETUP.md)

### Quick Setup

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Set up environment variables
cp .env.example .env

# 3. Add your API keys to .env
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# 4. Run first example
python poc/examples/simple_chat.py
```

---

## Security & Best Practices

### Never Hardcode Secrets

❌ **Bad:**
```python
api_key = "sk-1234567890abcdef"  # NEVER DO THIS
```

✅ **Good:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

### Use Environment Variables

**`.env` file:**
```bash
GEMINI_API_KEY=your_actual_key_here
OPENAI_API_KEY=your_openai_key_here
VECTOR_DB_URL=your_db_url_here
```

**`.gitignore`:**
```
.env
*.key
secrets/
```

### Rate Limiting

```python
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=10, period=60)  # 10 calls per minute
def call_llm(prompt):
    return llm.generate(prompt)
```

### Input Validation

```python
def validate_input(user_input):
    # Check length
    if len(user_input) > 10000:
        raise ValueError("Input too long")
    
    # Sanitize
    sanitized = user_input.strip()
    
    return sanitized
```

### Error Handling

```python
try:
    response = llm.generate(prompt)
except RateLimitError:
    print("Rate limit exceeded, waiting...")
    time.sleep(60)
except APIError as e:
    print(f"API error: {e}")
    # Fallback logic
```

---

## Progress Tracking

Track your learning journey in [PROGRESS.md](PROGRESS.md)

### Weekly Updates
- What you learned
- What you built
- Challenges faced
- Next steps

### Completed Topics
- ✅ LLM basics
- ✅ First API call
- ⏳ Prompt engineering
- ⏳ RAG implementation

---

## Customization

### Renaming Repository

To rename this repository:

1. **Update folder name:**
   ```bash
   mv ai-engineering-learning-poc your-new-name
   ```

2. **Update README.md:**
   - Change repository name at top
   - Update any references

3. **Update Git remote (if using Git):**
   ```bash
   # If you've already initialized git
   git remote set-url origin https://github.com/yourusername/your-new-name.git
   ```

---

## Resources

### Official Documentation
- **Google Gemini**: https://ai.google.dev/docs
- **OpenAI**: https://platform.openai.com/docs
- **Anthropic Claude**: https://docs.anthropic.com/
- **LangChain**: https://python.langchain.com/docs/
- **LlamaIndex**: https://docs.llamaindex.ai/

### Learning Resources
- **Prompt Engineering Guide**: https://www.promptingguide.ai/
- **AI Engineering**: https://www.latent.space/
- **Papers**: https://arxiv.org/

### Communities
- **Reddit**: r/MachineLearning, r/LocalLLaMA
- **Discord**: LangChain, LlamaIndex communities
- **Twitter**: Follow AI researchers and practitioners

---

## Contributing to Your Learning

This is YOUR learning repository. Feel free to:
- Add your own notes
- Create new examples
- Document discoveries
- Track experiments
- Build projects

---

## Next Steps

1. ✅ Complete setup → [SETUP.md](SETUP.md)
2. 📚 Start learning path → [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md)
3. 💻 Run first example → `python poc/examples/simple_chat.py`
4. 📝 Track progress → [PROGRESS.md](PROGRESS.md)
5. 🚀 Build your first agent!

---

**Happy Learning! 🚀 Build amazing AI systems!**
