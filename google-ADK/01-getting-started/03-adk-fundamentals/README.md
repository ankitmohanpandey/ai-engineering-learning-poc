# Google ADK Fundamentals

> **Core concepts and building blocks of Google ADK**

This section covers the fundamental concepts you need to understand to build effective AI agents with Google ADK. Master these foundations before moving to more advanced topics.

---

## 🎯 Learning Objectives

After completing this section, you will understand:
- **Core ADK Architecture** - How agents work under the hood
- **Agent Components** - Building blocks of AI agents
- **Memory Systems** - How agents remember and learn
- **Tool Integration** - Connecting agents to external services
- **Safety & Guardrails** - Building responsible AI agents
- **Configuration & Deployment** - Production-ready setup

---

## 📚 Topics Overview

### 1. **[Agent Core Concepts](./01-agent-core-concepts.md)**
- What is an AI Agent?
- Agent Lifecycle
- Agent States and Transitions
- Agent Types and Patterns

### 2. **[Memory Systems](./02-memory-systems.md)**
- Working Memory
- Episodic Memory
- Semantic Memory
- Long-term Memory
- Memory Management Strategies

### 3. **[Tool Integration](./03-tool-integration.md)**
- Built-in Tools
- Custom Tool Development
- Tool Composition
- Tool Security and Validation

### 4. **[Agent Configuration](./04-agent-configuration.md)**
- Model Selection and Parameters
- Memory Configuration
- Safety Settings
- Performance Tuning

### 5. **[Safety & Guardrails](./05-safety-guardrails.md)**
- Input Validation
- Output Filtering
- Content Moderation
- Ethical AI Practices

### 6. **[Error Handling](./06-error-handling.md)**
- Common Error Types
- Error Recovery Strategies
- Debugging Techniques
- Logging and Monitoring

---

## 🏗️ Agent Architecture

### High-Level View
```
┌─────────────────────────────────────────────────────────┐
│                    AI Agent                            │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   User       │────────►│   Input Processing   │
│   Input      │         │   (Validate, Parse)  │
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
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Output             │
                         │   Delivery           │
                         └──────────────────────┘
```

### Key Components Explained

#### 1. **Input Processing**
- **Validation**: Ensure input is safe and valid
- **Parsing**: Extract intent and entities
- **Preprocessing**: Clean and normalize input
- **Context Integration**: Combine with memory

#### 2. **Memory System**
- **Working Memory**: Current task context
- **Episodic Memory**: Conversation history
- **Semantic Memory**: Knowledge and facts
- **Long-term Memory**: Persistent learning

#### 3. **LLM Interface**
- **Reasoning**: Understand and analyze problems
- **Planning**: Create action plans
- **Decision Making**: Choose appropriate actions
- **Tool Selection**: Decide which tools to use

#### 4. **Tool System**
- **Built-in Tools**: Pre-built capabilities
- **Custom Tools**: User-defined functions
- **Tool Execution**: Run external operations
- **Result Processing**: Handle tool outputs

#### 5. **Response Generation**
- **Content Creation**: Generate appropriate responses
- **Formatting**: Structure output properly
- **Safety Checks**: Ensure safe and appropriate content
- **Quality Control**: Verify response quality

---

## 🧠 Memory Systems Deep Dive

### Memory Hierarchy
```
┌─────────────────────────────────────────────────────────┐
│                Memory Architecture                      │
└─────────────────────────────────────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐
│   Working Memory    │  │  Episodic Memory   │
│                    │  │                    │
│ • Current Task     │  │ • Conversations    │
│ • Active Context   │  │ • Interactions     │
│ • Short-term State │  │ • Session History  │
│ • Temporary Data   │  │ • User Preferences│
│                    │  │                    │
│ Duration: Minutes  │  │ Duration: Days     │
│ Size: Limited      │  │ Size: Configurable │
└─────────────────────┘  └─────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐
│  Semantic Memory    │  │ Long-term Memory    │
│                    │  │                    │
│ • Knowledge Base   │  │ • Learned Patterns  │
│ • Facts & Info     │  │ • User Behavior     │
│ • Concepts         │  │ • Adaptations       │
│ • Relationships    │  │ • Personalization   │
│                    │  │                    │
│ Duration: Permanent │  │ Duration: Permanent │
│ Size: Scalable     │  │ Size: Unlimited     │
└─────────────────────┘  └─────────────────────┘
```

### Memory Management Strategies

#### 1. **Working Memory Management**
```python
# Configure working memory
working_memory_config = {
    "max_size": 1000,          # Maximum tokens
    "retention_time": 300,     # 5 minutes
    "compression_enabled": True,
    "priority_scoring": True
}

# Working memory operations
agent.add_to_working_memory("current_task", "Analyze user request")
agent.get_from_working_memory("current_task")
agent.clear_working_memory()
```

#### 2. **Episodic Memory Management**
```python
# Configure episodic memory
episodic_memory_config = {
    "retention_days": 30,      # Keep for 30 days
    "max_conversations": 1000,  # Max conversations stored
    "compression_enabled": True,
    "search_indexing": True
}

# Episodic memory operations
agent.store_conversation(user_input, agent_response)
agent.search_conversations("previous discussions about X")
agent.get_conversation_history(user_id, limit=10)
```

#### 3. **Semantic Memory Management**
```python
# Configure semantic memory
semantic_memory_config = {
    "vector_dimension": 768,
    "similarity_threshold": 0.8,
    "max_entries": 10000,
    "auto_indexing": True
}

# Semantic memory operations
agent.store_knowledge("Python is a programming language", tags=["programming", "python"])
agent.search_knowledge("programming languages")
agent.get_related_concepts("python")
```

---

## 🛠️ Tool System Architecture

### Tool Categories

#### 1. **Built-in Tools**
```python
# Search tools
google_search_tool = GoogleSearchTool()
web_crawler_tool = WebCrawlerTool()

# Computation tools
calculator_tool = CalculatorTool()
data_analyzer_tool = DataAnalyzerTool()

# Communication tools
email_tool = EmailTool()
slack_tool = SlackTool()

# File operations
file_reader_tool = FileReaderTool()
file_writer_tool = FileWriterTool()
```

#### 2. **Custom Tools**
```python
# Define custom tool
def weather_forecast(location: str, days: int = 7) -> dict:
    """Get weather forecast for a location"""
    # Implementation here
    return {
        "location": location,
        "forecast": [...],
        "days": days
    }

# Register custom tool
weather_tool = Tool(
    func=weather_forecast,
    name="weather_forecast",
    description="Get weather forecast for a location",
    parameters={
        "location": {
            "type": "string",
            "description": "City name or coordinates",
            "required": True
        },
        "days": {
            "type": "integer",
            "description": "Number of days to forecast",
            "default": 7,
            "min": 1,
            "max": 14
        }
    }
)

agent.add_tool(weather_tool)
```

#### 3. **Tool Composition**
```python
# Compose multiple tools
def research_topic(topic: str) -> str:
    """Research a topic using multiple tools"""
    # Search for information
    search_results = google_search_tool.search(topic)
    
    # Analyze the data
    analysis = data_analyzer_tool.analyze(search_results)
    
    # Generate summary
    summary = summarize_tool.summarize(analysis)
    
    return summary

# Register composed tool
research_tool = Tool(
    func=research_topic,
    name="research_topic",
    description="Research a topic comprehensively"
)
```

---

## 🛡️ Safety & Guardrails

### Safety Layers

#### 1. **Input Validation**
```python
class InputValidator:
    def validate_input(self, user_input: str) -> ValidationResult:
        """Validate user input for safety"""
        checks = [
            self.check_length(user_input),
            self.check_content(user_input),
            self.check_patterns(user_input),
            self.check_rate_limit(user_input)
        ]
        
        return ValidationResult(all(checks))
    
    def check_content(self, input_text: str) -> bool:
        """Check for harmful content"""
        harmful_patterns = [
            r'(?i)(hate|violence|illegal)',
            r'(?i)(personal.*information|ssn|credit.*card)',
            # Add more patterns
        ]
        
        return not any(re.search(pattern, input_text) for pattern in harmful_patterns)
```

#### 2. **Output Filtering**
```python
class OutputFilter:
    def filter_output(self, output: str) -> str:
        """Filter agent output for safety"""
        # Remove PII
        filtered = self.remove_pii(output)
        
        # Check for harmful content
        if self.contains_harmful_content(filtered):
            filtered = self.sanitize_content(filtered)
        
        # Apply content policies
        filtered = self.apply_content_policies(filtered)
        
        return filtered
```

#### 3. **Rate Limiting**
```python
class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}
    
    def is_allowed(self, user_id: str) -> bool:
        """Check if user is allowed to make a request"""
        now = time.time()
        
        # Clean old requests
        self.clean_old_requests(now)
        
        # Check current user requests
        user_requests = self.requests.get(user_id, [])
        
        if len(user_requests) >= self.max_requests:
            return False
        
        # Add current request
        user_requests.append(now)
        self.requests[user_id] = user_requests
        
        return True
```

---

## ⚙️ Configuration Best Practices

### 1. **Model Configuration**
```python
# Optimize model parameters for different use cases
configs = {
    "creative_writing": {
        "temperature": 0.9,
        "top_p": 0.95,
        "max_tokens": 2048
    },
    "factual_answers": {
        "temperature": 0.1,
        "top_p": 0.5,
        "max_tokens": 512
    },
    "code_generation": {
        "temperature": 0.2,
        "top_p": 0.8,
        "max_tokens": 1024
    }
}
```

### 2. **Memory Configuration**
```python
# Optimize memory for different scenarios
memory_configs = {
    "customer_service": {
        "working_memory_size": 2000,
        "episodic_memory_days": 90,
        "semantic_memory_enabled": True
    },
    "data_analysis": {
        "working_memory_size": 4000,
        "episodic_memory_days": 7,
        "semantic_memory_enabled": False
    }
}
```

### 3. **Performance Tuning**
```python
# Performance optimization settings
performance_config = {
    "caching_enabled": True,
    "cache_ttl": 3600,  # 1 hour
    "parallel_tool_execution": True,
    "max_concurrent_tools": 5,
    "timeout_seconds": 30
}
```

---

## 📊 Monitoring & Debugging

### Key Metrics to Monitor
- **Response Time**: How long agents take to respond
- **Token Usage**: Input and output token consumption
- **Tool Success Rate**: How often tools execute successfully
- **Error Rates**: Frequency and types of errors
- **User Satisfaction**: Feedback and interaction quality

### Debugging Techniques
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Add debug information to agent
agent = Agent(
    name="debug_agent",
    debug_mode=True,
    log_level="DEBUG",
    trace_execution=True
)

# Monitor agent execution
@agent.monitor_execution
def monitored_run(user_input: str) -> str:
    return agent.run(user_input)
```

---

## 🎯 Practical Examples

### Example 1: Customer Service Agent
```python
customer_service_agent = Agent(
    name="customer_service",
    model="text-bison@001",
    memory_config={
        "working_memory_size": 2000,
        "episodic_memory_days": 90,
        "semantic_memory_enabled": True
    },
    tools=[
        search_knowledge_base,
        create_support_ticket,
        check_order_status,
        escalate_to_human
    ],
    safety_config={
        "input_validation": True,
        "output_filtering": True,
        "rate_limiting": True
    }
)
```

### Example 2: Data Analysis Agent
```python
data_analyst_agent = Agent(
    name="data_analyst",
    model="text-bison@001",
    memory_config={
        "working_memory_size": 4000,
        "episodic_memory_days": 7,
        "semantic_memory_enabled": False
    },
    tools=[
        query_database,
        analyze_data,
        create_visualization,
        generate_report
    ],
    performance_config={
        "parallel_tool_execution": True,
        "max_concurrent_tools": 3,
        "timeout_seconds": 60
    }
)
```

---

## 📚 Next Steps

After mastering these fundamentals:

1. **Practice** → Build your own agents using these concepts
2. **Explore** → `../examples/` for hands-on practice
3. **Advanced Topics** → `../../02-agent-development/`
4. **Production** → `../../04-safety-production/`

---

## 🔗 Additional Resources

- **ADK Documentation**: [Official Docs](https://cloud.google.com/adk/docs)
- **Best Practices**: [Google AI Best Practices](https://ai.google/responsibility/)
- **Community**: [Google Cloud Community](https://cloud.google.com/community)
- **Support**: [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-adk)

---

**🎉 Master these fundamentals to build amazing AI agents!**
