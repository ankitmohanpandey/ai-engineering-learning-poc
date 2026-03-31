# Memory & Context Management

> **Part III: Building AI Systems - Chapter 6**

Learn how to give your AI agents memory so they can remember past interactions and maintain context across conversations.

---

## 📚 What You'll Learn

By the end of this section, you'll understand:
- ✅ Why memory is crucial for AI agents
- ✅ Different types of memory systems
- ✅ How to implement memory with Mem0
- ✅ Memory management strategies
- ✅ Best practices for context handling

---

## 🧠 Why Memory Matters

**Problem**: LLMs are stateless - they don't remember previous conversations.

**Solution**: Add a memory layer to store and retrieve relevant information.

### Without Memory
```
User: "My name is Ankit"
AI: "Nice to meet you, Ankit!"

[New conversation]
User: "What's my name?"
AI: "I don't know your name."  ❌
```

### With Memory
```
User: "My name is Ankit"
AI: "Nice to meet you, Ankit!" [Stores: name=Ankit]

[New conversation]
User: "What's my name?"
AI: "Your name is Ankit!"  ✅
```

---

## 📖 Chapters

### [01. Short-Term Memory](01-short-term-memory.md)
**Duration**: 30 minutes  
**Difficulty**: Beginner

Conversation history and session context:
- What is short-term memory?
- Conversation history management
- Context window limitations
- Message summarization
- Implementation patterns

**Key Takeaway**: Short-term memory maintains context within a single conversation session.

---

### [02. Long-Term Memory](02-long-term-memory.md)
**Duration**: 45 minutes  
**Difficulty**: Intermediate

Persistent memory across sessions:
- What is long-term memory?
- Vector databases for memory
- Mem0 framework
- Memory retrieval strategies
- User-specific memory

**Key Takeaway**: Long-term memory enables AI to remember information across multiple sessions and conversations.

---

### [03. Working Memory](03-working-memory.md)
**Duration**: 30 minutes  
**Difficulty**: Intermediate

Active context and task state:
- What is working memory?
- Task-specific context
- Intermediate results
- Tool outputs
- State management

**Key Takeaway**: Working memory holds information needed for the current task being executed.

---

### [04. Memory Strategies](04-memory-strategies.md)
**Duration**: 45 minutes  
**Difficulty**: Advanced

Advanced memory management:
- Memory consolidation
- Forgetting strategies
- Priority-based retrieval
- Memory updates
- Performance optimization

**Key Takeaway**: Effective memory strategies balance relevance, recency, and performance.

---

## 🔧 Memory Framework: Mem0

**Mem0** is an intelligent memory layer for AI applications.

### What is Mem0?

Mem0 (formerly EmbedChain) provides:
- **Persistent Memory**: Store information across sessions
- **Semantic Search**: Find relevant memories using embeddings
- **Multi-User Support**: Separate memory per user
- **Automatic Updates**: Consolidate and update memories
- **Easy Integration**: Works with any LLM

### Quick Start with Mem0

```python
from mem0 import Memory

# Initialize memory
memory = Memory()

# Add memories
memory.add(
    "User prefers Python over JavaScript",
    user_id="user123"
)

memory.add(
    "User is learning AI Engineering",
    user_id="user123"
)

# Search memories
results = memory.search(
    "programming preferences",
    user_id="user123"
)

# Get all user memories
all_memories = memory.get_all(user_id="user123")

# Update memory
memory.update(
    memory_id="mem_123",
    data="User is now proficient in Python"
)

# Delete memory
memory.delete(memory_id="mem_123")
```

### Mem0 with LLMs

```python
from mem0 import Memory
import google.generativeai as genai

# Initialize
memory = Memory()
genai.configure(api_key="your-key")
model = genai.GenerativeModel('gemini-pro')

# Add context from conversation
user_message = "I love building AI agents with Python"
memory.add(user_message, user_id="user123")

# Retrieve relevant memories
relevant_memories = memory.search(
    "user preferences",
    user_id="user123"
)

# Build context-aware prompt
context = "\n".join([m['memory'] for m in relevant_memories])
prompt = f"""
Context about the user:
{context}

User: {user_message}
Assistant:
"""

response = model.generate_content(prompt)
```

---

## 🏗️ Memory Architecture

### Three-Layer Memory System

```
┌─────────────────────────────────────────────┐
│          AI Agent with Memory                │
└─────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Short-   │ │ Working  │ │  Long-   │
│  Term    │ │  Memory  │ │  Term    │
│ Memory   │ │          │ │ Memory   │
└──────────┘ └──────────┘ └──────────┘
│            │            │
│ Current    │ Active     │ Persistent
│ Session    │ Task       │ Storage
│            │            │
│ In-Memory  │ In-Memory  │ Vector DB
│ List       │ Dict       │ (Mem0)
└────────────┴────────────┴───────────┘
```

### Memory Flow

```
User Input
    │
    ▼
┌─────────────────┐
│ Retrieve        │
│ Relevant        │
│ Memories        │◄─── Long-Term Memory
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Build Context   │
│ with Memories   │◄─── Short-Term Memory
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ LLM Processing  │
│ with Context    │◄─── Working Memory
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Store New       │
│ Information     │──► Long-Term Memory
└─────────────────┘
    │
    ▼
Response to User
```

---

## 💡 Memory Types Comparison

| Type | Duration | Storage | Use Case | Example |
|------|----------|---------|----------|---------|
| **Short-Term** | Single session | In-memory list | Conversation flow | Chat history |
| **Working** | Current task | In-memory dict | Active processing | Tool outputs |
| **Long-Term** | Persistent | Vector DB | Cross-session | User preferences |

---

## 🛠️ Hands-On Practice

### Exercise 1: Simple Memory System

Create a basic memory system:

```python
class SimpleMemory:
    def __init__(self):
        self.short_term = []  # Conversation history
        self.long_term = {}   # User facts
    
    def add_message(self, role, content):
        """Add to short-term memory"""
        self.short_term.append({
            'role': role,
            'content': content
        })
    
    def store_fact(self, key, value):
        """Add to long-term memory"""
        self.long_term[key] = value
    
    def get_context(self, max_messages=10):
        """Get recent conversation"""
        return self.short_term[-max_messages:]
    
    def recall_fact(self, key):
        """Retrieve from long-term memory"""
        return self.long_term.get(key)
```

### Exercise 2: Mem0 Integration

Build a chatbot with Mem0:

```python
from mem0 import Memory
import google.generativeai as genai

class MemoryBot:
    def __init__(self, user_id):
        self.user_id = user_id
        self.memory = Memory()
        self.model = genai.GenerativeModel('gemini-pro')
    
    def chat(self, message):
        # Retrieve relevant memories
        memories = self.memory.search(
            message,
            user_id=self.user_id,
            limit=5
        )
        
        # Build context
        context = "\n".join([
            f"- {m['memory']}"
            for m in memories
        ])
        
        # Create prompt with context
        prompt = f"""
        What you know about the user:
        {context}
        
        User: {message}
        Assistant:
        """
        
        # Generate response
        response = self.model.generate_content(prompt)
        
        # Store new information
        self.memory.add(message, user_id=self.user_id)
        
        return response.text

# Usage
bot = MemoryBot(user_id="user123")
print(bot.chat("I love Python programming"))
print(bot.chat("What do I like?"))  # Will remember!
```

### Exercise 3: Memory Summarization

Handle context window limits:

```python
def summarize_conversation(messages, model):
    """Summarize old messages to save tokens"""
    
    conversation = "\n".join([
        f"{m['role']}: {m['content']}"
        for m in messages
    ])
    
    prompt = f"""
    Summarize this conversation in 2-3 sentences,
    preserving key information:
    
    {conversation}
    """
    
    summary = model.generate_content(prompt)
    return summary.text

# Use it
if len(conversation_history) > 20:
    old_messages = conversation_history[:10]
    summary = summarize_conversation(old_messages, model)
    
    # Replace old messages with summary
    conversation_history = [
        {'role': 'system', 'content': f'Previous context: {summary}'}
    ] + conversation_history[10:]
```

---

## 📊 Memory Management Strategies

### 1. Recency-Based
Keep most recent N messages:
```python
memory = conversation[-10:]  # Last 10 messages
```

### 2. Relevance-Based
Keep most relevant information:
```python
relevant = memory.search(current_query, limit=5)
```

### 3. Hybrid Approach
Combine recency and relevance:
```python
recent = conversation[-5:]  # Recent context
relevant = memory.search(query, limit=3)  # Relevant facts
context = recent + relevant
```

### 4. Token-Based
Stay within token limits:
```python
def fit_to_token_limit(messages, max_tokens=4000):
    total_tokens = 0
    selected = []
    
    for msg in reversed(messages):
        msg_tokens = count_tokens(msg)
        if total_tokens + msg_tokens > max_tokens:
            break
        selected.insert(0, msg)
        total_tokens += msg_tokens
    
    return selected
```

---

## 🎯 Best Practices

### ✅ Do's

1. **Store Structured Data**
   ```python
   memory.add({
       'type': 'preference',
       'category': 'programming',
       'value': 'Python',
       'timestamp': datetime.now()
   })
   ```

2. **Use Metadata for Filtering**
   ```python
   memory.search(
       query="preferences",
       filters={'type': 'preference'}
   )
   ```

3. **Update, Don't Duplicate**
   ```python
   # Check if memory exists
   existing = memory.search("user name", limit=1)
   if existing:
       memory.update(existing[0]['id'], new_data)
   else:
       memory.add(new_data)
   ```

4. **Implement Forgetting**
   ```python
   # Remove old, irrelevant memories
   old_memories = memory.get_all(
       user_id=user_id,
       filters={'timestamp': {'$lt': cutoff_date}}
   )
   for m in old_memories:
       memory.delete(m['id'])
   ```

### ❌ Don'ts

1. **Don't Store Everything**
   - Be selective about what to remember
   - Filter out noise and irrelevant information

2. **Don't Ignore Privacy**
   - Don't store sensitive information
   - Implement data retention policies
   - Allow users to delete their data

3. **Don't Exceed Context Windows**
   - Monitor token usage
   - Implement summarization
   - Prioritize relevant information

4. **Don't Forget to Update**
   - Keep memories current
   - Consolidate duplicate information
   - Remove outdated facts

---

## 🔍 Memory Retrieval Strategies

### Semantic Search
```python
# Find by meaning, not exact match
results = memory.search(
    "what programming languages does user know",
    user_id=user_id
)
# Returns: "User is proficient in Python and JavaScript"
```

### Filtered Search
```python
# Search with constraints
results = memory.search(
    query="projects",
    user_id=user_id,
    filters={
        'type': 'project',
        'status': 'active'
    }
)
```

### Time-Based Retrieval
```python
# Get recent memories
recent = memory.get_all(
    user_id=user_id,
    filters={'timestamp': {'$gt': last_week}}
)
```

---

## 📈 Performance Optimization

### 1. Caching
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_user_memories(user_id):
    return memory.get_all(user_id=user_id)
```

### 2. Batch Operations
```python
# Add multiple memories at once
memories = [
    "User likes Python",
    "User is learning AI",
    "User prefers dark mode"
]
memory.add_batch(memories, user_id=user_id)
```

### 3. Async Operations
```python
import asyncio

async def retrieve_memories_async(query, user_id):
    return await memory.search_async(query, user_id=user_id)
```

---

## 🔗 Related Topics

**Prerequisites**:
- [LLM Fundamentals](../02-llm-fundamentals/README.md)
- [Embeddings & Vectors](../04-embeddings-vectors/README.md)

**Next Steps**:
- [RAG Systems](../07-rag-systems/README.md)
- [AI Agent Architecture](../05-agent-architecture/README.md)

**Related Examples**:
- `examples/04-agents/memory_agent.py`
- `integrations/mem0_integration.py`

---

## 📚 Additional Resources

### Mem0 Documentation
- Official Docs: https://docs.mem0.ai/
- GitHub: https://github.com/mem0ai/mem0
- Examples: https://github.com/mem0ai/mem0/tree/main/examples

### Articles
- "Building Stateful AI Agents"
- "Memory Systems in LLM Applications"
- "Vector Databases for AI Memory"

### Videos
- Mem0 Tutorial Series
- Building AI with Memory
- Context Management Best Practices

---

## ✅ Completion Checklist

- [ ] Understand three types of memory
- [ ] Install and configure Mem0
- [ ] Build chatbot with memory
- [ ] Implement memory retrieval
- [ ] Handle context window limits
- [ ] Apply memory best practices
- [ ] Complete hands-on exercises

---

## 💡 Key Takeaways

1. **Memory is Essential**: LLMs need memory to be truly useful
2. **Three Types**: Short-term, Working, Long-term
3. **Mem0 Simplifies**: Framework handles complexity
4. **Balance is Key**: Relevance vs. Recency vs. Performance
5. **Privacy Matters**: Handle user data responsibly

---

**Next**: [RAG Systems →](../07-rag-systems/README.md)

**Estimated Time**: 2-3 hours total  
**Difficulty**: ⭐⭐ Intermediate  
**Status**: 🟢 Complete with Mem0!
