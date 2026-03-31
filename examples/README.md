# Code Examples Index

> **Runnable examples organized by topic - learn by doing!**

---

## 🎯 How to Use These Examples

### For Beginners
1. Start with `01-basic/`
2. Run examples in order
3. Read the code comments
4. Modify and experiment

### For Experienced Developers
1. Jump to your topic of interest
2. Copy and adapt code
3. Combine patterns
4. Build your own projects

---

## 📂 Examples by Category

### 🟢 01. Basic Examples
**Path**: `examples/01-basic/`  
**Difficulty**: ⭐ Beginner  
**Time**: 5-10 minutes each

| File | Description | What You'll Learn |
|------|-------------|-------------------|
| `hello_llm.py` | Your first LLM call | Basic API usage |
| `simple_chat.py` | Basic conversation | Message handling |
| `token_counter.py` | Count tokens | Token management |
| `streaming_response.py` | Stream responses | Real-time output |

**Prerequisites**: API key setup  
**Next**: Prompting examples

---

### 🟡 02. Prompt Engineering
**Path**: `examples/02-prompting/`  
**Difficulty**: ⭐⭐ Beginner-Intermediate  
**Time**: 10-15 minutes each

| File | Description | Technique |
|------|-------------|-----------|
| `zero_shot.py` | No examples needed | Direct instruction |
| `few_shot.py` | Learn from examples | In-context learning |
| `chain_of_thought.py` | Step-by-step reasoning | CoT prompting |
| `system_prompts.py` | Set AI behavior | Role definition |
| `prompt_templates.py` | Reusable prompts | Template patterns |

**Learn More**: [Prompt Engineering Guide](../handbook/03-prompt-engineering/README.md)

---

### 🟡 03. Embeddings & Vectors
**Path**: `examples/03-embeddings/`  
**Difficulty**: ⭐⭐ Intermediate  
**Time**: 15-20 minutes each

| File | Description | Concept |
|------|-------------|---------|
| `create_embeddings.py` | Generate embeddings | Vector representation |
| `similarity_search.py` | Find similar text | Semantic search |
| `vector_db_demo.py` | Store & retrieve | Vector database |
| `clustering.py` | Group similar items | Unsupervised learning |

**Learn More**: [Embeddings Guide](../handbook/04-embeddings-vectors/README.md)

---

### 🟠 04. AI Agents
**Path**: `examples/04-agents/`  
**Difficulty**: ⭐⭐⭐ Intermediate-Advanced  
**Time**: 20-30 minutes each

| File | Description | Pattern |
|------|-------------|---------|
| `simple_agent.py` | Basic agent loop | Agent fundamentals |
| `react_agent.py` | Reasoning + Acting | ReAct pattern |
| `tool_using_agent.py` | Agent with tools | Function calling |
| `memory_agent.py` | Agent with memory | Stateful agents |

**Learn More**: [Agent Architecture](../handbook/05-agent-architecture/README.md)

---

### 🟠 05. RAG Systems
**Path**: `examples/05-rag/`  
**Difficulty**: ⭐⭐⭐ Advanced  
**Time**: 30-45 minutes each

| File | Description | Component |
|------|-------------|-----------|
| `basic_rag.py` | Simple RAG | Retrieve + Generate |
| `advanced_rag.py` | Optimized RAG | Advanced techniques |
| `rag_evaluation.py` | Measure quality | Evaluation metrics |
| `document_qa.py` | Q&A over docs | Practical application |

**Learn More**: [RAG Systems Guide](../handbook/07-rag-systems/README.md)

---

### 🔴 06. Multi-Agent Systems
**Path**: `examples/06-multi-agent/`  
**Difficulty**: ⭐⭐⭐⭐ Advanced  
**Time**: 45-60 minutes each

| File | Description | Pattern |
|------|-------------|---------|
| `research_team.py` | Collaborative agents | Multi-agent coordination |
| `orchestrator.py` | Agent manager | Orchestration |
| `debate_agents.py` | Agents discussing | Multi-perspective |

**Learn More**: [Multi-Agent Guide](../handbook/09-multi-agent/README.md)

---

### 🔴 07. Production Examples
**Path**: `examples/07-production/`  
**Difficulty**: ⭐⭐⭐⭐ Advanced  
**Time**: 30-60 minutes each

| File | Description | Best Practice |
|------|-------------|---------------|
| `secure_agent.py` | Security patterns | Input validation, secrets |
| `monitored_agent.py` | Logging & metrics | Observability |
| `cached_agent.py` | Caching strategies | Performance |
| `rate_limited.py` | Rate limiting | API management |

**Learn More**: [Production Guide](../handbook/16-deployment/README.md)

---

## 🚀 Quick Start Examples

### Run Your First Example (2 minutes)

```bash
# Navigate to examples
cd examples/01-basic

# Run hello world
python hello_llm.py
```

### Try Interactive Chat (5 minutes)

```bash
# Run chatbot
cd ../../poc/examples
python simple_chat.py
```

### Experiment with Prompts (10 minutes)

```bash
# Try different prompting techniques
cd ../../examples/02-prompting
python zero_shot.py
python few_shot.py
python chain_of_thought.py
```

---

## 📊 Examples by Learning Path

### 🟢 Week 1-2: Foundations
```
examples/01-basic/
├── hello_llm.py           ← Start here
├── simple_chat.py
└── token_counter.py

examples/02-prompting/
├── zero_shot.py
├── few_shot.py
└── chain_of_thought.py
```

### 🟡 Week 3-4: Intermediate
```
examples/03-embeddings/
├── create_embeddings.py
├── similarity_search.py
└── vector_db_demo.py

examples/04-agents/
├── simple_agent.py
├── react_agent.py
└── memory_agent.py
```

### 🔴 Week 5-8: Advanced
```
examples/05-rag/
├── basic_rag.py
├── advanced_rag.py
└── rag_evaluation.py

examples/06-multi-agent/
├── research_team.py
└── orchestrator.py

examples/07-production/
├── secure_agent.py
├── monitored_agent.py
└── cached_agent.py
```

---

## 🎓 Learning by Example

### Pattern 1: Read → Run → Modify

1. **Read the code**
   - Understand what it does
   - Read comments
   - Note key concepts

2. **Run the example**
   ```bash
   python example_file.py
   ```

3. **Modify and experiment**
   - Change parameters
   - Add features
   - Break it (learn from errors)

### Pattern 2: Copy → Adapt → Build

1. **Copy example code**
   ```bash
   cp examples/04-agents/simple_agent.py my_agent.py
   ```

2. **Adapt to your needs**
   - Modify for your use case
   - Add your logic
   - Integrate with your data

3. **Build something new**
   - Combine multiple patterns
   - Create your own project
   - Share your work

---

## 🔥 Most Popular Examples

### Top 5 Examples to Try First

1. **🥇 Simple Chat** - `poc/examples/simple_chat.py`
   - Interactive chatbot
   - Conversation memory
   - Command handling

2. **🥈 Gemini Integration** - `integrations/gemini_integration.py`
   - Complete API usage
   - All features demonstrated
   - Production patterns

3. **🥉 Mem0 Memory** - `integrations/mem0_integration.py`
   - Persistent memory
   - Multi-user support
   - Memory-enabled chatbot

4. **Zero-Shot Prompting** - `examples/02-prompting/zero_shot.py`
   - Basic prompting
   - Different tasks
   - Prompt patterns

5. **Simple Agent** - `examples/04-agents/simple_agent.py`
   - Agent fundamentals
   - Decision making
   - Tool usage

---

## 💡 Example Templates

### Basic LLM Call Template

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Your prompt here")
print(response.text)
```

### Chatbot Template

```python
from mem0 import Memory
import google.generativeai as genai

class Chatbot:
    def __init__(self, user_id):
        self.user_id = user_id
        self.memory = Memory()
        self.model = genai.GenerativeModel('gemini-pro')
    
    def chat(self, message):
        # Retrieve context
        context = self.memory.search(message, user_id=self.user_id)
        
        # Generate response
        response = self.model.generate_content(
            f"Context: {context}\nUser: {message}"
        )
        
        # Store memory
        self.memory.add(message, user_id=self.user_id)
        
        return response.text
```

### Agent Template

```python
class SimpleAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.tools = {}  # Your tools
    
    def run(self, task):
        while not task_complete:
            # Think
            thought = self.model.generate_content(f"Think: {task}")
            
            # Act
            action = self.choose_action(thought)
            result = self.execute_action(action)
            
            # Observe
            task = self.update_task(result)
        
        return final_result
```

---

## 🛠️ Setup for Examples

### Prerequisites

```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Add your API keys to .env
```

### Required API Keys

- **Google Gemini**: For LLM examples
- **OpenAI** (optional): For OpenAI examples
- **Anthropic** (optional): For Claude examples

### Verify Setup

```bash
# Test your setup
python -c "import google.generativeai as genai; print('✓ Setup OK')"
```

---

## 📚 Related Resources

### Handbook Chapters
- [LLM Fundamentals](../handbook/02-llm-fundamentals/README.md)
- [Prompt Engineering](../handbook/03-prompt-engineering/README.md)
- [Agent Architecture](../handbook/05-agent-architecture/README.md)
- [Memory & Context](../handbook/06-memory-context/README.md)

### Integration Examples
- [Gemini Integration](../integrations/gemini_integration.py)
- [Mem0 Integration](../integrations/mem0_integration.py)

### Project Templates
- [Simple Chatbot](../poc/simple-chatbot/)
- [Document Q&A](../poc/document-qa/)
- [AI Agent](../poc/ai-agent/)

---

## ❓ FAQ

**Q: Which example should I start with?**  
A: Start with `examples/01-basic/hello_llm.py` or run `integrations/gemini_integration.py`

**Q: Do I need to run examples in order?**  
A: Not required, but recommended for beginners. Advanced users can jump to any topic.

**Q: Can I modify the examples?**  
A: Absolutely! That's the best way to learn. Copy, modify, experiment.

**Q: Examples not working?**  
A: Check [Troubleshooting](../handbook/18-troubleshooting/README.md) or verify your API keys in `.env`

**Q: How do I contribute my own examples?**  
A: Add them to `your-notes/experiments/` or create a PR!

---

## 🎯 Next Steps

After running examples:

1. **Build Your Own**
   - Use templates from `templates/`
   - Start a project in `poc/`
   - Document in `your-notes/`

2. **Deep Dive**
   - Read related handbook chapters
   - Explore advanced topics
   - Study production patterns

3. **Share & Learn**
   - Share your projects
   - Help others
   - Keep learning!

---

**Happy Coding! 💻✨**

**Need Help?** → [Troubleshooting](../handbook/18-troubleshooting/README.md) | [Glossary](../reference/GLOSSARY.md)
