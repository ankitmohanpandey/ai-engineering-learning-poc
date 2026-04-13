# AI Agent POC Setup - Learning Resources & Implementation Guide

> **Comprehensive resource guide for setting up AI Agent Proof of Concept with LLM platforms**

---

## 📚 Table of Contents

1. [LLM Platform Evaluation](#llm-platform-evaluation)
2. [Architecture Patterns](#architecture-patterns)
3. [API Integration & Authentication](#api-integration--authentication)
4. [Security & Secrets Management](#security--secrets-management)
5. [Environment Setup & Validation](#environment-setup--validation)
6. [Testing & Validation](#testing--validation)
7. [Implementation Checklist](#implementation-checklist)

---

## LLM Platform Evaluation

### Google Gemini

#### Official Documentation
- **[Gemini API Documentation](https://ai.google.dev/docs)** - Complete Gemini API docs
- **[Gemini API Quickstart](https://ai.google.dev/tutorials/python_quickstart)** - Python quickstart guide
- **[Gemini Models Overview](https://ai.google.dev/models/gemini)** - Available models and capabilities
- **[Gemini API Pricing](https://ai.google.dev/pricing)** - Pricing and rate limits
- **[Gemini Safety Settings](https://ai.google.dev/docs/safety_setting_gemini)** - Content safety configuration

#### Getting Started
- **[Get API Key](https://makersuite.google.com/app/apikey)** - Generate your Gemini API key
- **[Google AI Studio](https://makersuite.google.com/)** - Test prompts in browser
- **[Gemini Python SDK](https://github.com/google/generative-ai-python)** - Official Python library

#### Tutorials & Guides
- **[Gemini API Cookbook](https://github.com/google-gemini/cookbook)** - Code examples and recipes
- **[Building with Gemini](https://ai.google.dev/tutorials)** - Step-by-step tutorials
- **[Gemini Pro vs Ultra](https://ai.google.dev/models/gemini#model-variations)** - Model comparison

---

### OpenAI (GPT-4, GPT-3.5)

#### Official Documentation
- **[OpenAI API Documentation](https://platform.openai.com/docs)** - Complete API reference
- **[OpenAI API Quickstart](https://platform.openai.com/docs/quickstart)** - Getting started guide
- **[GPT-4 Documentation](https://platform.openai.com/docs/models/gpt-4)** - GPT-4 capabilities
- **[OpenAI Pricing](https://openai.com/pricing)** - Pricing calculator
- **[Rate Limits](https://platform.openai.com/docs/guides/rate-limits)** - Rate limit guidelines

#### Getting Started
- **[Get API Key](https://platform.openai.com/api-keys)** - Generate OpenAI API key
- **[OpenAI Playground](https://platform.openai.com/playground)** - Test prompts
- **[Python Library](https://github.com/openai/openai-python)** - Official Python SDK

#### Tutorials
- **[OpenAI Cookbook](https://github.com/openai/openai-cookbook)** - Code examples
- **[Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)** - Tool use patterns
- **[Best Practices](https://platform.openai.com/docs/guides/production-best-practices)** - Production guidelines

---

### Anthropic Claude

#### Official Documentation
- **[Claude API Documentation](https://docs.anthropic.com/)** - Complete API docs
- **[Claude Models](https://docs.anthropic.com/claude/docs/models-overview)** - Model comparison
- **[Claude API Reference](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)** - API reference
- **[Pricing](https://www.anthropic.com/pricing)** - Claude pricing

#### Getting Started
- **[Get API Access](https://console.anthropic.com/)** - Request API access
- **[Python SDK](https://github.com/anthropics/anthropic-sdk-python)** - Official Python library
- **[Prompt Engineering](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)** - Prompting guide

---

### Platform Comparison

| Feature | Gemini Pro | GPT-4 | Claude 3 |
|---------|-----------|-------|----------|
| **Context Window** | 32K tokens | 128K tokens | 200K tokens |
| **Multimodal** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Function Calling** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Streaming** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Free Tier** | ✅ Yes | ❌ No | ❌ No |
| **Best For** | Cost-effective | General purpose | Long context |

#### Decision Framework
- **[LLM Comparison Guide](https://artificialanalysis.ai/)** - Independent LLM benchmarks
- **[Choosing an LLM](https://www.latent.space/p/llm-selection)** - Selection criteria
- **[LLM Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)** - Community rankings

---

## Architecture Patterns

### AI Agent Architecture

#### Official Resources
- **[LangChain Agents](https://python.langchain.com/docs/modules/agents/)** - Agent framework
- **[AutoGen Framework](https://microsoft.github.io/autogen/)** - Multi-agent systems
- **[ReAct Pattern](https://arxiv.org/abs/2210.03629)** - Reasoning + Acting paper
- **[Agent Architecture Guide](https://www.promptingguide.ai/research/llm-agents)** - Comprehensive guide

#### Architecture Patterns

**1. Simple Agent Pattern**
```
User Input → LLM → Response
```
- **[Building Your First Agent](https://python.langchain.com/docs/modules/agents/quick_start)** - LangChain quickstart
- **[Simple Agent Example](https://github.com/langchain-ai/langchain/blob/master/cookbook/simple_agent.ipynb)** - Notebook

**2. ReAct Agent Pattern**
```
User Input → LLM (Reasoning) → Tool Selection → Tool Execution → LLM (Action) → Response
```
- **[ReAct Paper](https://arxiv.org/abs/2210.03629)** - Original research
- **[ReAct Implementation](https://python.langchain.com/docs/modules/agents/agent_types/react)** - LangChain guide
- **[ReAct Tutorial](https://www.promptingguide.ai/techniques/react)** - Step-by-step

**3. Multi-Agent Pattern**
```
Orchestrator → Agent 1 (Research) → Agent 2 (Analysis) → Agent 3 (Summary) → Response
```
- **[AutoGen Multi-Agent](https://microsoft.github.io/autogen/docs/tutorial/introduction)** - Multi-agent tutorial
- **[CrewAI Framework](https://github.com/joaomdmoura/crewAI)** - Role-based agents
- **[Multi-Agent Design Patterns](https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation/)** - Research paper

**4. RAG (Retrieval-Augmented Generation) Pattern**
```
User Input → Vector Search → Context Retrieval → LLM + Context → Response
```
- **[RAG Guide](https://python.langchain.com/docs/use_cases/question_answering/)** - LangChain RAG
- **[RAG Paper](https://arxiv.org/abs/2005.11401)** - Original research
- **[Building RAG Systems](https://www.pinecone.io/learn/retrieval-augmented-generation/)** - Comprehensive guide

#### Architecture Diagrams & Examples
- **[AI Agent Architecture Patterns](https://github.com/microsoft/autogen/blob/main/notebook/agentchat_planning.ipynb)** - Visual examples
- **[LangChain Architecture](https://python.langchain.com/docs/get_started/introduction)** - Framework overview
- **[Agent Design Patterns](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)** - DeepLearning.AI course

---

## API Integration & Authentication

### API Key Management

#### Best Practices Documentation
- **[Google Cloud API Keys](https://cloud.google.com/docs/authentication/api-keys)** - API key best practices
- **[OpenAI API Keys](https://platform.openai.com/docs/api-reference/authentication)** - Authentication guide
- **[API Security Best Practices](https://owasp.org/www-project-api-security/)** - OWASP guidelines

#### Getting API Keys

**Google Gemini**
```bash
# Get API key from: https://makersuite.google.com/app/apikey
export GOOGLE_API_KEY='your-api-key-here'
```
- **[Gemini API Key Setup](https://ai.google.dev/tutorials/setup)** - Setup guide

**OpenAI**
```bash
# Get API key from: https://platform.openai.com/api-keys
export OPENAI_API_KEY='your-api-key-here'
```
- **[OpenAI Authentication](https://platform.openai.com/docs/api-reference/authentication)** - Auth guide

**Anthropic Claude**
```bash
# Get API key from: https://console.anthropic.com/
export ANTHROPIC_API_KEY='your-api-key-here'
```
- **[Claude Authentication](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)** - Setup guide

### Environment Variables

#### Documentation
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management
- **[12-Factor App Config](https://12factor.net/config)** - Configuration best practices
- **[Environment Variables Guide](https://www.twilio.com/blog/environment-variables-python)** - Python guide

#### Implementation
```python
# Install python-dotenv
pip install python-dotenv

# .env file
GOOGLE_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key
PROJECT_ID=your-gcp-project

# Load in Python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
```

### API Integration Examples

#### Gemini Integration
```python
import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize model
model = genai.GenerativeModel('gemini-pro')

# Generate response
response = model.generate_content('Hello, world!')
print(response.text)
```
- **[Gemini Python Quickstart](https://ai.google.dev/tutorials/python_quickstart)** - Complete guide
- **[Gemini API Examples](https://github.com/google-gemini/cookbook)** - Code samples

#### OpenAI Integration
```python
from openai import OpenAI
import os

# Initialize client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Generate response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello, world!"}]
)
print(response.choices[0].message.content)
```
- **[OpenAI Python Library](https://github.com/openai/openai-python)** - Documentation
- **[OpenAI Examples](https://github.com/openai/openai-cookbook)** - Code samples

### Service Account Authentication (GCP)

#### Documentation
- **[GCP Service Accounts](https://cloud.google.com/iam/docs/service-accounts)** - Overview
- **[Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)** - ADC guide
- **[Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)** - Key management

#### Setup
```bash
# Create service account
gcloud iam service-accounts create ai-agent-poc \
  --display-name="AI Agent POC"

# Grant roles
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:ai-agent-poc@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Create key
gcloud iam service-accounts keys create key.json \
  --iam-account=ai-agent-poc@PROJECT_ID.iam.gserviceaccount.com

# Set environment variable
export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
```

---

## Security & Secrets Management

### Secrets Management Solutions

#### Google Cloud Secret Manager
- **[Secret Manager Documentation](https://cloud.google.com/secret-manager/docs)** - Complete guide
- **[Secret Manager Python](https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#secretmanager-create-secret-python)** - Python examples
- **[Best Practices](https://cloud.google.com/secret-manager/docs/best-practices)** - Security guidelines

**Implementation**:
```python
from google.cloud import secretmanager

def access_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# Usage
api_key = access_secret("my-project", "gemini-api-key")
```

#### AWS Secrets Manager
- **[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)** - Documentation
- **[Python SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html)** - Boto3 guide

#### HashiCorp Vault
- **[Vault Documentation](https://www.vaultproject.io/docs)** - Complete guide
- **[Vault Python Client](https://hvac.readthedocs.io/)** - Python library
- **[Getting Started](https://learn.hashicorp.com/vault)** - Tutorials

### Security Best Practices

#### Official Guidelines
- **[OWASP API Security](https://owasp.org/www-project-api-security/)** - API security top 10
- **[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)** - Security standards
- **[Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)** - GCP security

#### Key Principles
1. **Never hardcode secrets** - Use environment variables or secret managers
2. **Rotate keys regularly** - Implement key rotation policies
3. **Principle of least privilege** - Grant minimum necessary permissions
4. **Audit access** - Log and monitor secret access
5. **Encrypt in transit and at rest** - Use TLS/SSL and encryption

#### Implementation Checklist
- **[Security Checklist](https://github.com/OWASP/API-Security/blob/master/2019/en/dist/owasp-api-security-top-10.pdf)** - OWASP checklist
- **[Cloud Security Checklist](https://cloud.google.com/security/compliance/offerings)** - GCP compliance

### Code Security

#### Tools & Resources
- **[Bandit](https://github.com/PyCQA/bandit)** - Python security linter
- **[Safety](https://github.com/pyupio/safety)** - Dependency vulnerability scanner
- **[GitGuardian](https://www.gitguardian.com/)** - Secret detection in code
- **[Gitleaks](https://github.com/gitleaks/gitleaks)** - Secret scanning

**Usage**:
```bash
# Install security tools
pip install bandit safety

# Scan code for security issues
bandit -r .

# Check dependencies for vulnerabilities
safety check
```

---

## Environment Setup & Validation

### Development Environment Setup

#### Python Environment
- **[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)** - Official guide
- **[Poetry](https://python-poetry.org/docs/)** - Dependency management
- **[Conda](https://docs.conda.io/en/latest/)** - Environment management

**Setup**:
```bash
# Create virtual environment
python -m venv ai-agent-env
source ai-agent-env/bin/activate  # Linux/Mac
# ai-agent-env\Scripts\activate  # Windows

# Install dependencies
pip install google-generativeai openai python-dotenv langchain
```

#### Required Packages
```txt
# requirements.txt
google-generativeai>=0.3.0
openai>=1.0.0
anthropic>=0.7.0
langchain>=0.1.0
python-dotenv>=1.0.0
requests>=2.31.0
pydantic>=2.0.0
```

### Connectivity Validation

#### Testing LLM Connectivity

**Gemini Test**:
```python
import google.generativeai as genai
import os

def test_gemini_connection():
    try:
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content('Say "Connection successful"')
        print(f"✅ Gemini: {response.text}")
        return True
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return False

test_gemini_connection()
```

**OpenAI Test**:
```python
from openai import OpenAI
import os

def test_openai_connection():
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Connection successful'"}]
        )
        print(f"✅ OpenAI: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ OpenAI Error: {e}")
        return False

test_openai_connection()
```

#### Network & Firewall Configuration
- **[GCP Firewall Rules](https://cloud.google.com/vpc/docs/firewalls)** - Firewall setup
- **[Proxy Configuration](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)** - HTTP proxy setup
- **[SSL/TLS Verification](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification)** - Certificate handling

### Internal API Integration

#### REST API Integration
- **[Requests Library](https://requests.readthedocs.io/)** - HTTP library
- **[API Integration Guide](https://realpython.com/api-integration-in-python/)** - Python tutorial
- **[Authentication Patterns](https://requests.readthedocs.io/en/latest/user/authentication/)** - Auth methods

**Example**:
```python
import requests
import os

def test_internal_api():
    headers = {
        'Authorization': f'Bearer {os.getenv("INTERNAL_API_TOKEN")}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(
            'https://internal-api.company.com/health',
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        print(f"✅ Internal API: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Internal API Error: {e}")
        return False
```

---

## Testing & Validation

### Testing Frameworks

#### Unit Testing
- **[pytest](https://docs.pytest.org/)** - Testing framework
- **[unittest](https://docs.python.org/3/library/unittest.html)** - Built-in testing
- **[pytest-mock](https://pytest-mock.readthedocs.io/)** - Mocking library

**Example**:
```python
import pytest
from unittest.mock import Mock, patch

def test_llm_response():
    with patch('google.generativeai.GenerativeModel') as mock_model:
        mock_model.return_value.generate_content.return_value.text = "Test response"
        
        # Your test logic
        response = call_llm("test prompt")
        assert response == "Test response"
```

#### Integration Testing
- **[Integration Testing Guide](https://realpython.com/python-integration-testing/)** - Best practices
- **[API Testing](https://realpython.com/testing-third-party-apis-with-mocks/)** - Mock external APIs

### Validation Checklist

#### Access Validation
```python
def validate_access():
    checks = {
        'gemini_api': test_gemini_connection(),
        'openai_api': test_openai_connection(),
        'internal_api': test_internal_api(),
        'secrets_loaded': check_environment_variables()
    }
    
    print("\n=== Access Validation ===")
    for check, status in checks.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {check}: {'PASS' if status else 'FAIL'}")
    
    return all(checks.values())

def check_environment_variables():
    required_vars = ['GOOGLE_API_KEY', 'OPENAI_API_KEY', 'PROJECT_ID']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"❌ Missing environment variables: {missing}")
        return False
    return True
```

### Monitoring & Logging

#### Logging Best Practices
- **[Python Logging](https://docs.python.org/3/howto/logging.html)** - Official guide
- **[Logging Best Practices](https://realpython.com/python-logging/)** - Tutorial
- **[Structured Logging](https://www.structlog.org/)** - Structured logs

**Implementation**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ai_agent.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def call_llm(prompt):
    logger.info(f"Calling LLM with prompt: {prompt[:50]}...")
    try:
        response = model.generate_content(prompt)
        logger.info("LLM response received successfully")
        return response.text
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        raise
```

---

## Implementation Checklist

### Phase 1: Access & Setup ✅

- [ ] **Platform Selection**
  - [ ] Evaluate LLM platforms (Gemini, OpenAI, Claude)
  - [ ] Review pricing and rate limits
  - [ ] Select primary LLM provider
  
- [ ] **API Key Provisioning**
  - [ ] Generate Gemini API key
  - [ ] Generate OpenAI API key (if needed)
  - [ ] Document key rotation policy
  
- [ ] **Environment Setup**
  - [ ] Create Python virtual environment
  - [ ] Install required packages
  - [ ] Create `.env` file
  - [ ] Add `.env` to `.gitignore`

### Phase 2: Security & Secrets ✅

- [ ] **Secrets Management**
  - [ ] Choose secrets management solution (Secret Manager, Vault, etc.)
  - [ ] Store API keys in secrets manager
  - [ ] Implement secret retrieval in code
  - [ ] Verify no hardcoded secrets
  
- [ ] **Security Validation**
  - [ ] Run security scanner (Bandit)
  - [ ] Check dependency vulnerabilities (Safety)
  - [ ] Review IAM permissions
  - [ ] Enable audit logging

### Phase 3: Connectivity & Validation ✅

- [ ] **LLM Connectivity**
  - [ ] Test Gemini API connection
  - [ ] Test OpenAI API connection (if applicable)
  - [ ] Validate streaming responses
  - [ ] Test error handling
  
- [ ] **Internal API Integration**
  - [ ] Identify required internal APIs
  - [ ] Obtain API tokens/credentials
  - [ ] Test API connectivity
  - [ ] Implement retry logic
  
- [ ] **Environment Validation**
  - [ ] Run connectivity tests
  - [ ] Validate all environment variables
  - [ ] Test from development environment
  - [ ] Document any network/firewall requirements

### Phase 4: Architecture & Patterns ✅

- [ ] **Architecture Review**
  - [ ] Review agent architecture patterns
  - [ ] Select appropriate pattern (ReAct, RAG, etc.)
  - [ ] Design component interactions
  - [ ] Document architecture decisions
  
- [ ] **Dependencies Identification**
  - [ ] List all required APIs
  - [ ] Identify vector database needs (if RAG)
  - [ ] Determine monitoring requirements
  - [ ] Plan for scalability

### Phase 5: Testing & Documentation ✅

- [ ] **Testing**
  - [ ] Write unit tests
  - [ ] Write integration tests
  - [ ] Test error scenarios
  - [ ] Validate rate limiting
  
- [ ] **Documentation**
  - [ ] Document setup process
  - [ ] Create runbook for common issues
  - [ ] Document API endpoints used
  - [ ] Create architecture diagram

---

## Quick Start Template

### Complete Setup Script

```python
#!/usr/bin/env python3
"""
AI Agent POC - Setup Validation Script
Validates all prerequisites and connectivity
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

# Load environment variables
load_dotenv()

def check_environment_variables():
    """Check all required environment variables are set"""
    required_vars = [
        'GOOGLE_API_KEY',
        'PROJECT_ID'
    ]
    
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        return False
    
    print("✅ All environment variables loaded")
    return True

def test_gemini_connection():
    """Test Gemini API connectivity"""
    try:
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content('Say "Connection successful"')
        print(f"✅ Gemini API: {response.text}")
        return True
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return False

def test_openai_connection():
    """Test OpenAI API connectivity (optional)"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  OpenAI API key not configured (optional)")
        return True
    
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Connection successful'"}]
        )
        print(f"✅ OpenAI API: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return False

def main():
    """Run all validation checks"""
    print("=" * 50)
    print("AI Agent POC - Setup Validation")
    print("=" * 50)
    
    checks = {
        'Environment Variables': check_environment_variables(),
        'Gemini API': test_gemini_connection(),
        'OpenAI API': test_openai_connection()
    }
    
    print("\n" + "=" * 50)
    print("Validation Summary")
    print("=" * 50)
    
    for check, status in checks.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {check}: {'PASS' if status else 'FAIL'}")
    
    all_passed = all(checks.values())
    
    if all_passed:
        print("\n🎉 All checks passed! Ready to build AI Agent POC")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please review errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Usage**:
```bash
# Save as validate_setup.py
python validate_setup.py
```

---

## Additional Resources

### Courses & Tutorials
- **[DeepLearning.AI - Building Systems with ChatGPT](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/)** - Free course
- **[LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)** - Free course
- **[Building AI Agents](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)** - Free course
- **[Google Cloud Skills Boost - Generative AI](https://www.cloudskillsboost.google/paths/118)** - Learning path

### Books
- **"Building LLM Apps"** - [Free online book](https://www.oreilly.com/library/view/building-llm-apps/9781098150952/)
- **"Prompt Engineering Guide"** - [Free guide](https://www.promptingguide.ai/)
- **"LangChain Documentation"** - [Complete docs](https://python.langchain.com/docs/get_started/introduction)

### Community & Support
- **[LangChain Discord](https://discord.gg/langchain)** - Community support
- **[r/LangChain](https://www.reddit.com/r/LangChain/)** - Reddit community
- **[AI Stack Exchange](https://ai.stackexchange.com/)** - Q&A forum

---

**Good luck with your AI Agent POC! 🚀**

*This guide covers all aspects of setting up a secure, validated AI Agent POC environment.*
