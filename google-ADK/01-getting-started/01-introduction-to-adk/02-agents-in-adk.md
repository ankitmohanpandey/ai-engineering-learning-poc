# Agents in ADK

> **Understanding and creating AI agents with Google ADK**

An agent is the core building block of Google ADK. It's an AI-powered entity that can understand instructions, reason about problems, use tools, and interact with users or other systems.

---

## 🎯 What is an Agent?

### Definition
An **Agent** in Google ADK is an autonomous AI system that can:
- **Perceive** - Understand inputs and context
- **Reason** - Make decisions using LLMs
- **Act** - Execute actions via tools
- **Learn** - Improve from interactions
- **Communicate** - Interact with users and other agents

### Agent Components
```
┌─────────────────────────────────────────────────────────┐
│                    AI Agent                            │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Input       │────────►│   Input Processing   │
│   Handler     │         │   (Parse, Validate)  │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Memory System      │
                         │  - Working Memory    │
                         │  - Context Retrieval │
                         │  - State Management  │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   LLM Interface     │
                         │  - Reasoning        │
                         │  - Planning         │
                         │  - Decision Making  │
                         └──────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌──────────┐    ┌──────────┐    ┌──────────┐
            │  Tool 1  │    │  Tool 2  │    │  Tool N  │
            │ (Search) │    │ (Calc)   │    │ (API)    │
            └──────────┘    └──────────┘    └──────────┘
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Response           │
                         │   Generation         │
                         │  - Format Output     │
                         │  - Safety Check      │
                         │  - Quality Control   │
                         └──────────────────────┘
```

---

## 🏗️ Agent Types

### 1. **Simple Conversational Agent**
Basic chatbot for conversations and Q&A

```python
from google_adk import Agent

# Simple conversational agent
chat_agent = Agent(
    name="chat_agent",
    description="A simple conversational AI assistant",
    model="text-bison@001",
    instructions="You are a helpful AI assistant. Be friendly and informative."
)
```

**Use Cases:**
- Customer service chatbots
- Information assistants
- Educational tutors
- Personal assistants

### 2. **Task-Oriented Agent**
Agent focused on specific tasks with tools

```python
from google_adk import Agent, Tool

def calculate(expression: str) -> str:
    """Calculate mathematical expressions"""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid expression"

# Task-oriented agent
task_agent = Agent(
    name="calculator_agent",
    description="Agent that can perform calculations",
    model="text-bison@001",
    tools=[Tool(calculate, name="calculate")],
    instructions="You are a calculator assistant. Use the calculate tool for math operations."
)
```

**Use Cases:**
- Data analysis assistants
- Document processors
- Code generators
- Research assistants

### 3. **Multi-Tool Agent**
Agent with multiple specialized tools

```python
from google_adk import Agent, Tool

# Multiple tools
def search_web(query: str) -> str:
    """Search the web for information"""
    # Implementation here
    return f"Search results for: {query}"

def send_email(to: str, subject: str, body: str) -> str:
    """Send an email"""
    # Implementation here
    return f"Email sent to: {to}"

# Multi-tool agent
multi_tool_agent = Agent(
    name="productivity_agent",
    description="Agent with multiple productivity tools",
    model="text-bison@001",
    tools=[
        Tool(search_web, name="search_web"),
        Tool(send_email, name="send_email"),
        Tool(calculate, name="calculate")
    ],
    instructions="You are a productivity assistant. Use appropriate tools to help users."
)
```

**Use Cases:**
- Personal productivity assistants
- Business process automation
- Workflow automation
- Enterprise assistants

### 4. **ReAct Agent**
Reasoning + Acting pattern agent

```python
react_agent = Agent(
    name="research_agent",
    description="Agent that reasons before acting",
    model="text-bison@001",
    tools=[search_web, calculate, analyze_data],
    instructions="""
    You are a research assistant that follows the ReAct pattern:
    
    1. Thought: Analyze what you need to do
    2. Action: Choose and execute a tool
    3. Observation: Review the tool result
    4. Thought: Decide next step
    5. Repeat until you have the answer
    
    Always show your reasoning process.
    """
)
```

**Use Cases:**
- Complex problem solving
- Research and analysis
- Planning and strategy
- Diagnostic systems

---

## 🔄 Agent Lifecycle

### 1. **Initialization**
```python
# Create agent instance
agent = Agent(
    name="my_agent",
    description="Agent description",
    model="text-bison@001",
    # ... other configuration
)

# Initialize agent
agent.initialize()
```

### 2. **Execution Loop**
```
┌─────────────────┐
│   Receive Input  │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Validate Input │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Retrieve Memory│
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Generate Plan  │
└─────────┬───────┘
          │
┌─────────▼───────┐
│ Execute Tools   │
└─────────┬───────┘
          │
┌─────────▼───────┐
│ Generate Output │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Store Memory   │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Return Output  │
└─────────────────┘
```

### 3. **State Management**
```python
# Agent states
class AgentState:
    INITIALIZING = "initializing"
    READY = "ready"
    PROCESSING = "processing"
    ERROR = "error"
    TERMINATED = "terminated"

# Check agent state
if agent.state == AgentState.READY:
    response = agent.run(user_input)
```

---

## ⚙️ Agent Configuration

### Basic Configuration
```python
agent = Agent(
    name="my_agent",
    description="Agent description",
    model="text-bison@001",
    temperature=0.7,
    max_tokens=1024,
    instructions="Agent instructions"
)
```

### Advanced Configuration
```python
agent = Agent(
    name="advanced_agent",
    description="Advanced agent configuration",
    model="text-bison@001",
    
    # Model parameters
    temperature=0.7,
    max_tokens=2048,
    top_p=0.9,
    top_k=40,
    
    # Memory configuration
    memory_config={
        "working_memory_size": 2000,
        "episodic_memory_days": 30,
        "semantic_memory_enabled": True
    },
    
    # Safety configuration
    safety_config={
        "input_validation": True,
        "output_filtering": True,
        "rate_limiting": True
    },
    
    # Performance configuration
    performance_config={
        "caching_enabled": True,
        "parallel_tool_execution": True,
        "timeout_seconds": 30
    }
)
```

---

## 🧠 Memory in Agents

### Working Memory
```python
# Configure working memory
agent = Agent(
    name="memory_agent",
    memory_config={
        "working_memory_size": 1000,  # tokens
        "retention_time": 300,       # 5 minutes
        "compression_enabled": True
    }
)

# Use working memory
agent.add_to_working_memory("current_task", "Analyze user request")
task = agent.get_from_working_memory("current_task")
```

### Episodic Memory
```python
# Configure episodic memory
agent = Agent(
    name="episodic_agent",
    memory_config={
        "episodic_memory_days": 30,
        "max_conversations": 1000,
        "search_indexing": True
    }
)

# Store and retrieve conversations
agent.store_conversation(user_input, agent_response)
history = agent.get_conversation_history(user_id, limit=10)
```

### Semantic Memory
```python
# Configure semantic memory
agent = Agent(
    name="semantic_agent",
    memory_config={
        "semantic_memory_enabled": True,
        "vector_dimension": 768,
        "similarity_threshold": 0.8
    }
)

# Store and search knowledge
agent.store_knowledge("Python is a programming language", tags=["programming"])
results = agent.search_knowledge("programming languages")
```

---

## 🛡️ Agent Safety

### Input Validation
```python
agent = Agent(
    name="safe_agent",
    safety_config={
        "input_validation": True,
        "max_input_length": 10000,
        "blocked_patterns": ["hate", "violence"],
        "rate_limiting": {
            "max_requests_per_minute": 60,
            "max_requests_per_hour": 1000
        }
    }
)
```

### Output Filtering
```python
agent = Agent(
    name="filtered_agent",
    safety_config={
        "output_filtering": True,
        "pii_detection": True,
        "content_moderation": True,
        "bias_detection": True
    }
)
```

---

## 🚀 Best Practices

### 1. **Clear Instructions**
```python
# Good instructions
instructions = """
You are a customer service agent for an e-commerce company.

Your responsibilities:
1. Help customers with order inquiries
2. Assist with product information
3. Handle return requests
4. Escalate complex issues to human agents

Guidelines:
- Always be polite and professional
- Ask for order numbers when needed
- Provide clear, step-by-step solutions
- Never make promises you can't keep
- Use the available tools to get accurate information
"""
```

### 2. **Appropriate Tool Selection**
```python
# Choose tools that match the agent's purpose
customer_service_agent = Agent(
    name="customer_service",
    tools=[
        search_orders,
        check_inventory,
        process_return,
        escalate_to_human
    ]
)
```

### 3. **Memory Optimization**
```python
# Configure memory based on use case
chatbot_memory = {
    "working_memory_size": 1000,
    "episodic_memory_days": 7,
    "semantic_memory_enabled": False
}

research_agent_memory = {
    "working_memory_size": 4000,
    "episodic_memory_days": 90,
    "semantic_memory_enabled": True
}
```

### 4. **Error Handling**
```python
try:
    response = agent.run(user_input)
except RateLimitError:
    response = "I'm receiving too many requests. Please try again later."
except ToolExecutionError:
    response = "I'm having trouble with my tools. Let me try a different approach."
except Exception as e:
    response = "I'm experiencing technical difficulties. Please try again later."
```

---

## 📊 Agent Performance

### Monitoring Metrics
- **Response Time**: Time to generate responses
- **Token Usage**: Input and output tokens consumed
- **Tool Success Rate**: Percentage of successful tool executions
- **Error Rate**: Frequency of errors
- **User Satisfaction**: Feedback and ratings

### Performance Optimization
```python
# Optimize for performance
agent = Agent(
    name="optimized_agent",
    performance_config={
        "caching_enabled": True,
        "cache_ttl": 3600,
        "parallel_tool_execution": True,
        "max_concurrent_tools": 5,
        "timeout_seconds": 30
    }
)
```

---

## 🎯 Use Case Examples

### Customer Service Agent
```python
customer_service_agent = Agent(
    name="customer_service",
    description="Handles customer inquiries and support",
    model="text-bison@001",
    tools=[
        search_orders,
        check_inventory,
        process_return,
        create_support_ticket,
        escalate_to_human
    ],
    instructions="""
    You are a customer service agent. Help customers with:
    - Order status and tracking
    - Product information and availability
    - Returns and exchanges
    - Technical support
    
    Always be polite, professional, and helpful. Use available tools to provide accurate information.
    """
)
```

### Data Analysis Agent
```python
data_analyst_agent = Agent(
    name="data_analyst",
    description="Analyzes data and generates insights",
    model="text-bison@001",
    tools=[
        query_database,
        analyze_data,
        create_visualization,
        generate_report
    ],
    instructions="""
    You are a data analyst. Help users with:
    - Data exploration and analysis
    - Statistical calculations
    - Creating charts and visualizations
    - Generating insights and recommendations
    
    Always verify data accuracy and provide clear explanations of your analysis.
    """
)
```

---

## 📚 Next Steps

1. **Learn about Structure Output** → `03-structure-output.md`
2. **Understand Model Configuration** → `04-configuring-model.md`
3. **Master Tools in ADK** → `05-tools-in-adk.md`
4. **Build Your First Agent** → Try the examples

---

**🤖 Start building powerful AI agents with Google ADK!**
