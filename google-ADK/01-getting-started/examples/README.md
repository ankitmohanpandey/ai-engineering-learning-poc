# Google ADK Examples

> **Hands-on examples to learn Google ADK**

This directory contains practical examples that demonstrate key ADK concepts and patterns. Start with the basics and progress to more complex scenarios.

---

## 📚 Learning Path

### 🌱 **Beginner Examples**
1. **[Hello World Agent](./01_hello_world_agent.py)** - Your first ADK agent
2. **[Simple Chat Agent](./02_simple_chat_agent.py)** - Basic conversation agent
3. **[Agent with Memory](./03_agent_with_memory.py)** - Adding conversation memory
4. **[Tool-using Agent](./04_tool_using_agent.py)** - Agent with external tools

### 🚀 **Intermediate Examples**
5. **[Multi-tool Agent](./05_multi_tool_agent.py)** - Agent with multiple tools
6. **[ReAct Pattern Agent](./06_react_pattern_agent.py)** - Reasoning + Acting pattern
7. **[Custom Tool Agent](./07_custom_tool_agent.py)** - Building custom tools
8. **[Data Analysis Agent](./08_data_analysis_agent.py)** - Agent for data tasks

### 🏆 **Advanced Examples**
9. **[Multi-Agent System](./09_multi_agent_system.py)** - Multiple collaborating agents
10. **[Workflow Orchestrator](./10_workflow_orchestrator.py)** - Complex workflows
11. **[Production Agent](./11_production_agent.py)** - Production-ready agent
12. **[Enterprise Agent](./12_enterprise_agent.py)** - Enterprise-scale implementation

---

## 🎯 Example Categories

### **Basic Concepts**
- Agent creation and configuration
- Simple tool integration
- Basic memory systems
- Input/output handling

### **Intermediate Patterns**
- Complex tool chains
- Memory strategies
- Error handling
- Performance optimization

### **Advanced Architectures**
- Multi-agent systems
- Workflow orchestration
- Production deployment
- Enterprise features

---

## 🚀 Quick Start

### Run Your First Example
```bash
# Navigate to examples directory
cd 01-getting-started/examples

# Run the hello world example
python 01_hello_world_agent.py

# Run with environment variables
ADK_LOG_LEVEL=DEBUG python 01_hello_world_agent.py
```

### Expected Output
```
🤖 Hello World Agent
====================

User: Hello, how are you?
Agent: Hello! I'm doing well, thank you for asking. I'm a simple ADK agent designed to greet users and have basic conversations. How can I help you today?

User: What can you do?
Agent: I can help you with basic conversations, answer simple questions, and demonstrate how Google ADK works. I'm currently equipped with basic conversational capabilities and can use tools when needed.

✅ Agent execution completed successfully!
```

---

## 📋 Prerequisites for Examples

### Required Setup
1. **Complete ADK Installation** → `../02-installation-setup/`
2. **Set Environment Variables** → `.env file configured`
3. **Google Cloud Project** → APIs enabled
4. **Service Account** → Proper permissions

### Environment Variables
```bash
# Required for all examples
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"

# Optional for advanced examples
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
```

### Python Dependencies
```bash
# Install all required dependencies
pip install -r ../02-installation-setup/requirements.txt

# Additional dependencies for examples
pip install matplotlib pandas numpy requests
```

---

## 🏗️ Example Structure

Each example follows this structure:

```python
#!/usr/bin/env python3
"""
Example: [Title]
Description: [What this example demonstrates]
Concepts: [ADK concepts covered]
Difficulty: [Beginner/Intermediate/Advanced]
"""

import os
from dotenv import load_dotenv
from google_adk import Agent, Tool

# Load environment variables
load_dotenv()

def main():
    """Main example execution"""
    pass

if __name__ == "__main__":
    main()
```

---

## 📖 Example Details

### 01. Hello World Agent
**Concepts**: Basic agent creation, simple responses
**Time**: 5 minutes
**What you'll learn**:
- Create your first ADK agent
- Configure basic agent properties
- Handle simple user inputs
- Generate responses

### 02. Simple Chat Agent
**Concepts**: Conversation handling, turn-taking
**Time**: 10 minutes
**What you'll learn**:
- Implement chat loops
- Handle conversation state
- Manage user interactions
- Basic error handling

### 03. Agent with Memory
**Concepts**: Memory systems, context management
**Time**: 15 minutes
**What you'll learn**:
- Add working memory to agents
- Store conversation history
- Retrieve relevant context
- Memory configuration

### 04. Tool-using Agent
**Concepts**: Tool integration, function calling
**Time**: 20 minutes
**What you'll learn**:
- Create and register tools
- Handle tool execution
- Process tool results
- Error handling for tools

### 05. Multi-tool Agent
**Concepts**: Multiple tools, tool selection
**Time**: 25 minutes
**What you'll learn**:
- Integrate multiple tools
- Tool selection logic
- Parallel tool execution
- Tool composition

### 06. ReAct Pattern Agent
**Concepts**: ReAct pattern, reasoning loops
**Time**: 30 minutes
**What you'll learn**:
- Implement ReAct pattern
- Reasoning before acting
- Observation handling
- Iterative problem solving

### 07. Custom Tool Agent
**Concepts**: Custom tool development
**Time**: 35 minutes
**What you'll learn**:
- Build custom tools
- Tool validation
- Parameter handling
- Tool documentation

### 08. Data Analysis Agent
**Concepts**: Data processing, analysis tools
**Time**: 40 minutes
**What you'll learn**:
- Process data with agents
- Generate insights
- Create visualizations
- Data tool integration

### 09. Multi-Agent System
**Concepts**: Multiple agents, agent communication
**Time**: 45 minutes
**What you'll learn**:
- Create multiple agents
- Agent communication
- Task delegation
- Agent coordination

### 10. Workflow Orchestrator
**Concepts**: Workflow design, orchestration
**Time**: 50 minutes
**What you'll learn**:
- Design workflows
- Orchestrate complex tasks
- Handle workflow state
- Error recovery

### 11. Production Agent
**Concepts**: Production deployment, monitoring
**Time**: 60 minutes
**What you'll learn**:
- Production configuration
- Monitoring and logging
- Performance optimization
- Deployment strategies

### 12. Enterprise Agent
**Concepts**: Enterprise features, scaling
**Time**: 75 minutes
**What you'll learn**:
- Enterprise security
- Scalability patterns
- Compliance features
- Advanced monitoring

---

## 🛠️ Running Examples

### Basic Execution
```bash
# Run individual examples
python 01_hello_world_agent.py
python 02_simple_chat_agent.py

# Run with debug logging
ADK_LOG_LEVEL=DEBUG python 03_agent_with_memory.py
```

### Interactive Mode
```bash
# Run examples with interactive input
python -c "
import sys
sys.path.append('.')
from examples.interactive_runner import run_interactive
run_interactive('02_simple_chat_agent.py')
"
```

### Batch Execution
```bash
# Run all beginner examples
for file in 0*_*.py; do
    echo "Running $file..."
    python "$file"
    echo "✅ $file completed"
done
```

### Testing Examples
```bash
# Run tests for examples
python -m pytest tests/test_examples.py -v

# Run specific test
python -m pytest tests/test_examples.py::test_hello_world -v
```

---

## 🔧 Customization

### Modify Agent Behavior
```python
# Change model parameters
agent = Agent(
    name="custom_agent",
    model="text-bison@001",
    temperature=0.9,  # More creative
    max_tokens=2048   # Longer responses
)
```

### Add Custom Tools
```python
def custom_tool(input_text: str) -> str:
    """Your custom tool implementation"""
    return f"Processed: {input_text}"

agent.add_tool(Tool(custom_tool, name="custom_tool"))
```

### Configure Memory
```python
# Custom memory configuration
memory_config = {
    "working_memory_size": 2000,
    "episodic_memory_days": 60,
    "semantic_memory_enabled": True
}

agent = Agent(
    name="memory_agent",
    memory_config=memory_config
)
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Authentication Errors
```bash
# Check credentials
gcloud auth activate-service-account \
    --key-file=$GOOGLE_APPLICATION_CREDENTIALS

# Verify project
gcloud config list project
```

#### 2. Import Errors
```bash
# Check ADK installation
pip show google-adk

# Reinstall if needed
pip uninstall google-adk
pip install google-adk
```

#### 3. Memory Issues
```bash
# Increase memory allocation
export ADK_MAX_MEMORY=4096

# Clear cache
rm -rf .adk_cache
```

#### 4. Tool Execution Failures
```python
# Add error handling
try:
    result = agent.run(user_input)
except Exception as e:
    print(f"Error: {e}")
    # Fallback logic
```

---

## 📚 Next Steps

After completing these examples:

1. **Build Your Own Agent** → Create a custom agent for your use case
2. **Explore Advanced Topics** → `../../02-agent-development/`
3. **Learn Workflows** → `../../03-workflows-orchestration/`
4. **Production Deployment** → `../../04-safety-production/`

---

## 🤝 Contributing

Want to contribute examples?

1. **Follow the template** - Use the standard example structure
2. **Add documentation** - Explain concepts clearly
3. **Include tests** - Add test cases for your example
4. **Update README** - Add your example to the index

---

**🚀 Start learning with [01_hello_world_agent.py](./01_hello_world_agent.py)!**
