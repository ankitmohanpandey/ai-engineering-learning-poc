# Configuring Model in ADK

> **Optimizing LLM models for specific use cases**

Model configuration is crucial for getting the best performance from your AI agents. Google ADK provides extensive options to fine-tune model behavior for different applications.

---

## 🎯 Model Parameters Overview

### Core Parameters
- **Model Selection**: Choose the right LLM for your use case
- **Temperature**: Control response creativity and randomness
- **Max Tokens**: Limit response length
- **Top P**: Nucleus sampling for probability distribution
- **Top K**: Limit vocabulary choices
- **Frequency Penalty**: Reduce repetition
- **Presence Penalty**: Encourage diverse topics

---

## 🤖 Available Models

### 1. **Text Models**
For general text generation and conversation

```python
from google_adk import Agent

# Gemini Pro - General purpose
gemini_pro_agent = Agent(
    name="gemini_pro_agent",
    model="gemini-pro",
    description="Agent using Gemini Pro model"
)

# Text Bison - Cost-effective
text_bison_agent = Agent(
    name="text_bison_agent",
    model="text-bison@001",
    description="Agent using Text Bison model"
)

# Text Unicorn - High performance
text_unicorn_agent = Agent(
    name="text_unicorn_agent",
    model="text-unicorn@001",
    description="Agent using Text Unicorn model"
)
```

### 2. **Chat Models**
Optimized for conversational AI

```python
# Chat Bison - Conversational AI
chat_bison_agent = Agent(
    name="chat_bison_agent",
    model="chat-bison@001",
    description="Agent optimized for conversations"
)

# Gemini Pro Vision - Multimodal
gemini_vision_agent = Agent(
    name="gemini_vision_agent",
    model="gemini-pro-vision",
    description="Agent with vision capabilities"
)
```

### 3. **Code Models**
Specialized for code generation and analysis

```python
# Code Bison - Code generation
code_bison_agent = Agent(
    name="code_bison_agent",
    model="code-bison@001",
    description="Agent for code generation"
)

# Code Gecko - Code completion
code_gecko_agent = Agent(
    name="code_gecko_agent",
    model="code-gecko@001",
    description="Agent for code completion"
)
```

---

## 🌡️ Temperature Configuration

### Understanding Temperature
Temperature controls the randomness in model responses:
- **Low (0.0-0.3)**: Deterministic, focused responses
- **Medium (0.4-0.7)**: Balanced creativity and consistency
- **High (0.8-1.0)**: Creative, diverse responses

### Temperature by Use Case

```python
# Factual responses - Low temperature
factual_agent = Agent(
    name="factual_agent",
    model="text-bison@001",
    temperature=0.1,
    instructions="Provide accurate, factual information. Be precise and consistent."
)

# Creative writing - High temperature
creative_agent = Agent(
    name="creative_agent",
    model="text-bison@001",
    temperature=0.9,
    instructions="Be creative and imaginative. Generate diverse and original content."
)

# Balanced conversation - Medium temperature
conversation_agent = Agent(
    name="conversation_agent",
    model="chat-bison@001",
    temperature=0.7,
    instructions="Be engaging and natural in conversation. Balance creativity with coherence."
)

# Code generation - Low-medium temperature
code_agent = Agent(
    name="code_agent",
    model="code-bison@001",
    temperature=0.2,
    instructions="Generate clean, functional code. Be precise and follow best practices."
)
```

### Dynamic Temperature
Adjust temperature based on context

```python
def get_temperature_for_context(context: str) -> float:
    """Determine appropriate temperature based on context"""
    
    if "factual" in context.lower() or "data" in context.lower():
        return 0.1
    elif "creative" in context.lower() or "story" in context.lower():
        return 0.9
    elif "code" in context.lower() or "programming" in context.lower():
        return 0.2
    else:
        return 0.7

# Agent with dynamic temperature
dynamic_agent = Agent(
    name="dynamic_agent",
    model="text-bison@001",
    temperature_provider=get_temperature_for_context,
    instructions="Adapt your response style based on the context."
)
```

---

## 📏 Token Configuration

### Max Tokens
Control response length for different use cases

```python
# Short responses - Quick answers
short_response_agent = Agent(
    name="short_agent",
    model="text-bison@001",
    max_tokens=100,
    instructions="Provide concise, brief answers. Maximum 2-3 sentences."
)

# Medium responses - Detailed explanations
medium_response_agent = Agent(
    name="medium_agent",
    model="text-bison@001",
    max_tokens=500,
    instructions="Provide detailed explanations with examples. 3-5 paragraphs."
)

# Long responses - Comprehensive analysis
long_response_agent = Agent(
    name="long_agent",
    model="text-bison@001",
    max_tokens=2048,
    instructions="Provide comprehensive, in-depth analysis with multiple sections."
)
```

### Token Optimization Strategies

```python
# Token-efficient agent
efficient_agent = Agent(
    name="efficient_agent",
    model="text-bison@001",
    max_tokens=256,
    temperature=0.5,
    instructions="""
    Be concise and efficient with your language.
    Use bullet points for lists.
    Avoid unnecessary words and phrases.
    Focus on essential information.
    """
)

# Context-aware token allocation
def get_max_tokens_for_input(input_text: str) -> int:
    """Determine appropriate max tokens based on input"""
    input_length = len(input_text.split())
    
    if input_length < 10:
        return 100  # Short input, short output
    elif input_length < 50:
        return 300  # Medium input, medium output
    else:
        return 800  # Long input, detailed output
```

---

## 🎯 Top P and Top K Configuration

### Top P (Nucleus Sampling)
Controls probability mass for token selection

```python
# Conservative Top P - Focused responses
conservative_agent = Agent(
    name="conservative_agent",
    model="text-bison@001",
    top_p=0.5,
    instructions="Be precise and focused. Stick to the most likely responses."
)

# Standard Top P - Balanced responses
standard_agent = Agent(
    name="standard_agent",
    model="text-bison@001",
    top_p=0.9,
    instructions="Provide balanced, natural responses."
)

# High Top P - Diverse responses
diverse_agent = Agent(
    name="diverse_agent",
    model="text-bison@001",
    top_p=0.95,
    instructions="Be creative and explore diverse possibilities."
)
```

### Top K (Vocabulary Limiting)
Limit the number of tokens considered

```python
# Low Top K - Very focused
focused_agent = Agent(
    name="focused_agent",
    model="text-bison@001",
    top_k=20,
    instructions="Use common, straightforward language. Be very direct."
)

# Medium Top K - Balanced
balanced_agent = Agent(
    name="balanced_agent",
    model="text-bison@001",
    top_k=40,
    instructions="Use natural, varied vocabulary appropriate for the context."
)

# High Top K - Rich vocabulary
rich_agent = Agent(
    name="rich_agent",
    model="text-bison@001",
    top_k=100,
    instructions="Use rich, expressive vocabulary. Be articulate and sophisticated."
)
```

---

## ⚖️ Penalty Configuration

### Frequency Penalty
Reduce repetition of tokens

```python
# High frequency penalty - Avoid repetition
no_repetition_agent = Agent(
    name="no_repetition_agent",
    model="text-bison@001",
    frequency_penalty=2.0,
    instructions="Avoid repeating words and phrases. Use varied language."
)

# Medium frequency penalty - Natural repetition
natural_agent = Agent(
    name="natural_agent",
    model="text-bison@001",
    frequency_penalty=0.5,
    instructions="Use natural repetition when it adds clarity or emphasis."
)

# No frequency penalty - Allow repetition
repetition_allowed_agent = Agent(
    name="repetition_allowed_agent",
    model="text-bison@001",
    frequency_penalty=0.0,
    instructions="Repeat when it serves the purpose of emphasis or clarity."
)
```

### Presence Penalty
Encourage introduction of new topics

```python
# High presence penalty - Diverse topics
diverse_topics_agent = Agent(
    name="diverse_topics_agent",
    model="text-bison@001",
    presence_penalty=1.5,
    instructions="Introduce new ideas and perspectives. Avoid staying on one topic."
)

# Medium presence penalty - Balanced exploration
balanced_topics_agent = Agent(
    name="balanced_topics_agent",
    model="text-bison@001",
    presence_penalty=0.5,
    instructions="Balance depth and breadth. Explore related topics naturally."
)

# Low presence penalty - Focused discussion
focused_topics_agent = Agent(
    name="focused_topics_agent",
    model="text-bison@001",
    presence_penalty=0.0,
    instructions="Stay focused on the main topic. Avoid unnecessary tangents."
)
```

---

## 🔧 Advanced Configuration

### Model Selection Strategy
Choose models based on requirements

```python
def select_model_for_task(task_type: str, budget: str = "medium") -> str:
    """Select appropriate model based on task and budget"""
    
    model_map = {
        "low": {
            "conversation": "text-bison@001",
            "generation": "text-bison@001",
            "analysis": "text-bison@001",
            "code": "code-bison@001"
        },
        "medium": {
            "conversation": "chat-bison@001",
            "generation": "text-bison@001",
            "analysis": "text-bison@001",
            "code": "code-bison@001"
        },
        "high": {
            "conversation": "gemini-pro",
            "generation": "text-unicorn@001",
            "analysis": "gemini-pro",
            "code": "code-gecko@001"
        }
    }
    
    return model_map.get(budget, model_map["medium"]).get(task_type, "text-bison@001")

# Dynamic model selection
dynamic_model_agent = Agent(
    name="dynamic_model_agent",
    model=select_model_for_task("conversation", "medium"),
    instructions="Use the best model for the task."
)
```

### Context Window Configuration
Manage context for different use cases

```python
# Small context - Simple tasks
small_context_agent = Agent(
    name="small_context_agent",
    model="text-bison@001",
    context_window=1024,
    instructions="Handle simple, short-context tasks efficiently."
)

# Medium context - Standard tasks
medium_context_agent = Agent(
    name="medium_context_agent",
    model="text-bison@001",
    context_window=4096,
    instructions="Handle standard tasks with moderate context requirements."
)

# Large context - Complex tasks
large_context_agent = Agent(
    name="large_context_agent",
    model="gemini-pro",
    context_window=32768,
    instructions="Handle complex tasks requiring extensive context."
)
```

### Batch Configuration
Process multiple inputs efficiently

```python
# Batch processing agent
batch_agent = Agent(
    name="batch_agent",
    model="text-bison@001",
    batch_size=10,
    max_tokens=200,
    temperature=0.3,
    instructions="""
    Process multiple inputs efficiently.
    Provide consistent, concise responses for each item.
    """
)

# Process batch
inputs = ["Analyze this", "Summarize that", "Explain concept"]
responses = batch_agent.process_batch(inputs)
```

---

## 📊 Performance Optimization

### Cost Optimization
Reduce costs while maintaining quality

```python
# Cost-optimized agent
cost_optimized_agent = Agent(
    name="cost_optimized_agent",
    model="text-bison@001",  # Most cost-effective
    max_tokens=150,          # Limit output
    temperature=0.3,          # Reduce variability
    top_p=0.8,             # Focused responses
    instructions="""
    Be concise and efficient.
    Use minimal tokens while maintaining clarity.
    Focus on essential information.
    """
)
```

### Latency Optimization
Reduce response time

```python
# Fast response agent
fast_agent = Agent(
    name="fast_agent",
    model="text-bison@001",
    max_tokens=100,
    temperature=0.1,
    cache_enabled=True,
    instructions="""
    Provide quick, direct responses.
    Use simple, clear language.
    Avoid unnecessary elaboration.
    """
)
```

### Quality Optimization
Maximize response quality

```python
# High-quality agent
quality_agent = Agent(
    name="quality_agent",
    model="gemini-pro",
    max_tokens=1024,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    frequency_penalty=0.5,
    presence_penalty=0.3,
    instructions="""
    Provide high-quality, comprehensive responses.
    Use clear, well-structured language.
    Include relevant details and examples.
    """
)
```

---

## 🎛️ Configuration Templates

### Predefined Configurations

```python
from google_adk import ModelConfig

# Customer service configuration
customer_service_config = ModelConfig(
    model="chat-bison@001",
    temperature=0.3,
    max_tokens=300,
    top_p=0.8,
    frequency_penalty=0.5,
    instructions="""
    You are a customer service agent.
    Be polite, professional, and helpful.
    Provide clear, actionable solutions.
    """
)

# Code generation configuration
code_config = ModelConfig(
    model="code-bison@001",
    temperature=0.1,
    max_tokens=800,
    top_p=0.5,
    instructions="""
    You are a code generation assistant.
    Write clean, efficient, well-documented code.
    Follow best practices and coding standards.
    """
)

# Creative writing configuration
creative_config = ModelConfig(
    model="gemini-pro",
    temperature=0.9,
    max_tokens=1024,
    top_p=0.95,
    top_k=100,
    presence_penalty=0.8,
    instructions="""
    You are a creative writing assistant.
    Be imaginative, original, and engaging.
    Use rich vocabulary and varied sentence structures.
    """
)

# Use configurations
customer_agent = Agent(
    name="customer_agent",
    config=customer_service_config
)

code_agent = Agent(
    name="code_agent",
    config=code_config
)

creative_agent = Agent(
    name="creative_agent",
    config=creative_config
)
```

---

## 🧪 Model Testing and Validation

### A/B Testing Models
Compare different configurations

```python
from google_adk import ModelTester

# Test different temperatures
temperature_test = ModelTester(
    base_config={
        "model": "text-bison@001",
        "max_tokens": 200
    },
    test_variables={
        "temperature": [0.1, 0.5, 0.9]
    },
    test_prompt="Write a short story about a robot."
)

# Run test
results = temperature_test.run()
print(f"Best temperature: {results.best_config['temperature']}")

# Test different models
model_test = ModelTester(
    base_config={
        "temperature": 0.7,
        "max_tokens": 300
    },
    test_variables={
        "model": ["text-bison@001", "chat-bison@001", "gemini-pro"]
    },
    test_prompt="Explain quantum computing in simple terms."
)

model_results = model_test.run()
print(f"Best model: {model_results.best_config['model']}")
```

### Performance Monitoring
Track model performance

```python
from google_adk import PerformanceMonitor

# Monitor agent performance
monitor = PerformanceMonitor(
    metrics=["response_time", "token_usage", "cost", "quality_score"],
    log_file="model_performance.log"
)

# Agent with monitoring
monitored_agent = Agent(
    name="monitored_agent",
    model="text-bison@001",
    temperature=0.7,
    performance_monitor=monitor,
    instructions="Provide helpful responses."
)

# Track performance over time
for input_text in test_inputs:
    response = monitored_agent.run(input_text)
    monitor.log_interaction(input_text, response)
```

---

## 📚 Best Practices

### 1. **Model Selection**
- **Match Model to Task**: Use specialized models for specific tasks
- **Consider Budget**: Balance cost and performance
- **Test Different Models**: Find best fit for your use case
- **Monitor Performance**: Track effectiveness over time

### 2. **Parameter Tuning**
- **Start with Defaults**: Use baseline parameters first
- **Adjust Gradually**: Make small parameter changes
- **Test Systematically**: Use A/B testing
- **Consider Context**: Adjust based on input type

### 3. **Cost Management**
- **Optimize Token Usage**: Limit unnecessary output
- **Use Caching**: Cache common responses
- **Choose Right Model**: Balance cost and capability
- **Monitor Usage**: Track costs in real-time

### 4. **Quality Assurance**
- **Validate Outputs**: Check response quality
- **Use Consistency**: Maintain consistent behavior
- **Test Edge Cases**: Handle unusual inputs
- **Gather Feedback**: Improve based on user input

---

## 📚 Next Steps

1. **Master Tools in ADK** → `05-tools-in-adk.md`
2. **Build Configured Agents** → Create agents with optimized settings
3. **Test Performance** → Compare different configurations
4. **Deploy to Production** → Use production-ready configurations

---

**⚙️ Optimize your models for peak performance!**
