# 🗺️ Navigation Guide - Find Anything Fast

> **Quick reference to navigate the AI Engineering Handbook**

---

## 🚀 I Want To...

### Learn AI Engineering
- **Start Learning** → [START_HERE.md](START_HERE.md)
- **Beginner Path** → [Week 1-2 Guide](START_HERE.md#beginner-path-weeks-1-2)
- **Full Roadmap** → [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md)
- **Track Progress** → [PROGRESS.md](PROGRESS.md)

### Run Code Examples
- **All Examples** → [examples/README.md](examples/README.md)
- **First Example** → [Gemini Integration](integrations/gemini_integration.py)
- **Chatbot** → [Simple Chat](poc/examples/simple_chat.py)
- **Memory** → [Mem0 Integration](integrations/mem0_integration.py)

### Learn Specific Topics
- **Browse All Topics** → [HANDBOOK_INDEX.md](HANDBOOK_INDEX.md)
- **AI Basics** → [Foundations](handbook/01-foundations/README.md)
- **LLMs** → [LLM Fundamentals](handbook/02-llm-fundamentals/README.md)
- **Prompting** → [Prompt Engineering](handbook/03-prompt-engineering/README.md)
- **Memory** → [Memory & Context](handbook/06-memory-context/README.md)
- **Agents** → [Agent Architecture](handbook/05-agent-architecture/README.md)
- **RAG** → [RAG Systems](handbook/07-rag-systems/README.md)

### Find Reference Material
- **Terminology** → [Glossary](reference/GLOSSARY.md)
- **All References** → [Reference Index](reference/README.md)
- **External Links** → [Resources](reference/RESOURCES.md)
- **API Docs** → [API Reference](reference/api-reference/)

### Build a Project
- **Templates** → [templates/](templates/)
- **POC Projects** → [poc/](poc/)
- **Case Studies** → [Case Studies](handbook/17-case-studies/README.md)

### Get Help
- **Troubleshooting** → [Troubleshooting Guide](handbook/18-troubleshooting/README.md)
- **Setup Issues** → [SETUP.md](SETUP.md)
- **FAQ** → [examples/README.md#faq](examples/README.md#faq)

---

## 📂 Folder Structure Quick Reference

```
📁 Root
├── 📄 START_HERE.md          ← New? Start here!
├── 📄 README.md              ← Main handbook overview
├── 📄 HANDBOOK_INDEX.md      ← Complete content index
├── 📄 NAVIGATION.md          ← This file
├── 📄 LEARNING_ROADMAP.md    ← 8-week learning path
├── 📄 PROGRESS.md            ← Track your progress
├── 📄 SETUP.md               ← Environment setup
│
├── 📁 handbook/              ← 📚 Main learning content
│   ├── 01-foundations/       → AI/ML basics
│   ├── 02-llm-fundamentals/  → How LLMs work
│   ├── 03-prompt-engineering/→ Effective prompts
│   ├── 04-embeddings-vectors/→ Vector databases
│   ├── 05-agent-architecture/→ Building agents
│   ├── 06-memory-context/    → Memory with Mem0 ✨
│   ├── 07-rag-systems/       → RAG implementation
│   ├── 08-tools-functions/   → Function calling
│   ├── 09-multi-agent/       → Multi-agent systems
│   ├── 10-frameworks/        → LangChain, etc.
│   ├── 11-fine-tuning/       → Custom models
│   ├── 12-multimodal/        → Vision, audio
│   ├── 13-security/          → Best practices
│   ├── 14-optimization/      → Performance
│   ├── 15-monitoring/        → Observability
│   ├── 16-deployment/        → Production
│   ├── 17-case-studies/      → Real examples
│   └── 18-troubleshooting/   → Common issues
│
├── 📁 examples/              ← 💻 Runnable code
│   ├── README.md             → Examples index
│   ├── 01-basic/             → Hello world, chat
│   ├── 02-prompting/         → Prompt techniques
│   ├── 03-embeddings/        → Vector search
│   ├── 04-agents/            → AI agents
│   ├── 05-rag/               → RAG systems
│   ├── 06-multi-agent/       → Multi-agent
│   └── 07-production/        → Production code
│
├── 📁 integrations/          ← 🔌 LLM providers
│   ├── gemini_integration.py ✅ Complete
│   ├── mem0_integration.py   ✅ Complete
│   └── ...
│
├── 📁 poc/                   ← 🚀 Your projects
│   ├── simple-chatbot/
│   ├── document-qa/
│   ├── ai-agent/
│   └── examples/
│       └── simple_chat.py    ✅ Interactive chat
│
├── 📁 reference/             ← 📖 Quick reference
│   ├── GLOSSARY.md           → AI terminology
│   ├── RESOURCES.md          → External links
│   ├── api-reference/        → API docs
│   └── cheatsheets/          → Quick guides
│
├── 📁 templates/             ← 📝 Project templates
│   ├── agent-template/
│   ├── rag-template/
│   └── project-template/
│
├── 📁 notebooks/             ← 📓 Jupyter notebooks
│   └── *.ipynb
│
└── 📁 your-notes/            ← ✍️ Your personal space
    ├── discoveries/
    ├── experiments/
    └── ideas/
```

---

## 🎯 By Learning Stage

### Stage 1: Absolute Beginner (Week 1-2)
```
START_HERE.md
  ↓
handbook/01-foundations/
  ↓
handbook/02-llm-fundamentals/
  ↓
examples/01-basic/
  ↓
integrations/gemini_integration.py
```

### Stage 2: Intermediate (Week 3-4)
```
handbook/03-prompt-engineering/
  ↓
handbook/04-embeddings-vectors/
  ↓
handbook/06-memory-context/ (Mem0)
  ↓
examples/03-embeddings/
  ↓
integrations/mem0_integration.py
```

### Stage 3: Advanced (Week 5-8)
```
handbook/05-agent-architecture/
  ↓
handbook/07-rag-systems/
  ↓
handbook/09-multi-agent/
  ↓
examples/05-rag/
  ↓
poc/your-project/
```

### Stage 4: Production (Week 8+)
```
handbook/13-security/
  ↓
handbook/14-optimization/
  ↓
handbook/16-deployment/
  ↓
examples/07-production/
```

---

## 🔍 By Topic

### Fundamentals
| Topic | Handbook | Examples | Integration |
|-------|----------|----------|-------------|
| AI Basics | [01-foundations](handbook/01-foundations/) | - | - |
| LLMs | [02-llm-fundamentals](handbook/02-llm-fundamentals/) | [01-basic](examples/01-basic/) | [gemini](integrations/gemini_integration.py) |
| Prompting | [03-prompt-engineering](handbook/03-prompt-engineering/) | [02-prompting](examples/02-prompting/) | - |

### Core Concepts
| Topic | Handbook | Examples | Integration |
|-------|----------|----------|-------------|
| Embeddings | [04-embeddings-vectors](handbook/04-embeddings-vectors/) | [03-embeddings](examples/03-embeddings/) | - |
| Agents | [05-agent-architecture](handbook/05-agent-architecture/) | [04-agents](examples/04-agents/) | - |
| Memory | [06-memory-context](handbook/06-memory-context/) | [04-agents](examples/04-agents/) | [mem0](integrations/mem0_integration.py) ✨ |
| RAG | [07-rag-systems](handbook/07-rag-systems/) | [05-rag](examples/05-rag/) | - |

### Advanced
| Topic | Handbook | Examples | Integration |
|-------|----------|----------|-------------|
| Multi-Agent | [09-multi-agent](handbook/09-multi-agent/) | [06-multi-agent](examples/06-multi-agent/) | - |
| Frameworks | [10-frameworks](handbook/10-frameworks/) | - | - |
| Fine-tuning | [11-fine-tuning](handbook/11-fine-tuning/) | - | - |

### Production
| Topic | Handbook | Examples | Integration |
|-------|----------|----------|-------------|
| Security | [13-security](handbook/13-security/) | [07-production](examples/07-production/) | - |
| Optimization | [14-optimization](handbook/14-optimization/) | [07-production](examples/07-production/) | - |
| Deployment | [16-deployment](handbook/16-deployment/) | - | - |

---

## 📱 Quick Commands

### Setup
```bash
# Initial setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Run Examples
```bash
# Basic examples
python integrations/gemini_integration.py
python integrations/mem0_integration.py
python poc/examples/simple_chat.py

# Specific categories
python examples/01-basic/hello_llm.py
python examples/02-prompting/zero_shot.py
python examples/04-agents/simple_agent.py
```

### Open Documentation
```bash
# Main guides
open START_HERE.md
open HANDBOOK_INDEX.md
open LEARNING_ROADMAP.md

# Specific topics
open handbook/06-memory-context/README.md
open examples/README.md
open reference/GLOSSARY.md
```

---

## 🎓 By Learning Goal

### Goal: Understand AI Basics
```
1. Read: handbook/01-foundations/README.md
2. Read: handbook/02-llm-fundamentals/README.md
3. Run: examples/01-basic/hello_llm.py
```

### Goal: Build a Chatbot
```
1. Read: handbook/03-prompt-engineering/README.md
2. Run: poc/examples/simple_chat.py
3. Read: handbook/06-memory-context/README.md
4. Run: integrations/mem0_integration.py
5. Build: Use templates/chatbot-template/
```

### Goal: Implement RAG
```
1. Read: handbook/04-embeddings-vectors/README.md
2. Read: handbook/07-rag-systems/README.md
3. Run: examples/03-embeddings/
4. Run: examples/05-rag/
5. Build: Use templates/rag-template/
```

### Goal: Create AI Agent
```
1. Read: handbook/05-agent-architecture/README.md
2. Read: handbook/08-tools-functions/README.md
3. Run: examples/04-agents/
4. Build: Use templates/agent-template/
```

### Goal: Production Deployment
```
1. Read: handbook/13-security/README.md
2. Read: handbook/14-optimization/README.md
3. Read: handbook/16-deployment/README.md
4. Run: examples/07-production/
```

---

## 🔗 Cross-References

### If You're Reading...

**handbook/01-foundations/** → Next: [LLM Fundamentals](handbook/02-llm-fundamentals/)

**handbook/02-llm-fundamentals/** → Try: [Basic Examples](examples/01-basic/)

**handbook/03-prompt-engineering/** → Try: [Prompting Examples](examples/02-prompting/)

**handbook/04-embeddings-vectors/** → Try: [Embedding Examples](examples/03-embeddings/)

**handbook/05-agent-architecture/** → Try: [Agent Examples](examples/04-agents/)

**handbook/06-memory-context/** → Try: [Mem0 Integration](integrations/mem0_integration.py)

**handbook/07-rag-systems/** → Try: [RAG Examples](examples/05-rag/)

---

## 🆘 Common Questions

**"Where do I start?"**  
→ [START_HERE.md](START_HERE.md)

**"How do I run examples?"**  
→ [examples/README.md](examples/README.md)

**"What's the learning path?"**  
→ [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md)

**"What does this term mean?"**  
→ [Glossary](reference/GLOSSARY.md)

**"How do I build X?"**  
→ [Case Studies](handbook/17-case-studies/README.md)

**"Something's not working"**  
→ [Troubleshooting](handbook/18-troubleshooting/README.md)

**"What's Mem0?"**  
→ [Memory Chapter](handbook/06-memory-context/README.md)

---

## 📊 Content Status

| Section | Status | Completion |
|---------|--------|------------|
| Foundations | 🟡 Partial | ~40% |
| LLM Fundamentals | 🟡 Partial | ~40% |
| Prompt Engineering | 🟡 Partial | ~40% |
| Embeddings | 🟡 Partial | ~30% |
| Agent Architecture | 🟡 Partial | ~40% |
| **Memory & Context** | 🟢 **Complete** | **100%** ✨ |
| RAG Systems | 🔴 Planned | ~10% |
| Tools & Functions | 🔴 Planned | ~10% |
| Multi-Agent | 🔴 Planned | ~5% |
| Production | 🔴 Planned | ~10% |

**Legend**: 🟢 Complete | 🟡 Partial | 🔴 Planned

---

## 🎯 Recommended Paths

### Path A: Theory First
```
1. Read all handbook chapters
2. Then run examples
3. Build projects
```

### Path B: Practice First
```
1. Run examples
2. Read relevant chapters
3. Build projects
```

### Path C: Project-Based
```
1. Choose project
2. Learn as needed
3. Build incrementally
```

**Most Recommended**: Path B (Practice First) - Learn by doing!

---

**Lost? Start here**: [START_HERE.md](START_HERE.md)  
**Need help?**: [Troubleshooting](handbook/18-troubleshooting/README.md)  
**Ready to learn?**: [HANDBOOK_INDEX.md](HANDBOOK_INDEX.md)
