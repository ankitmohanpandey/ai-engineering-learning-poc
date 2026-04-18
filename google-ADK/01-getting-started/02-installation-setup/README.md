# Google ADK Installation & Setup

> **Complete guide to installing and configuring Google Agent Development Kit**

This guide will walk you through installing Google ADK, setting up your development environment, and verifying your installation with a simple test agent.

---

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher (recommended: 3.9+)
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 10GB free disk space

### Google Cloud Requirements
- **Google Cloud Account** with billing enabled
- **Google Cloud Project** created
- **Required APIs enabled**:
  - Cloud AI Platform API
  - Vertex AI API
  - Cloud Storage API
  - Cloud Functions API

### Development Tools
- **Git** for version control
- **Code Editor** (VS Code, PyCharm, or similar)
- **Terminal/Command Prompt** with administrator privileges

---

## 🔧 Step 1: Google Cloud Setup

### 1.1 Create Google Cloud Project
```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize gcloud
gcloud init

# Create new project (replace with your project name)
gcloud projects create my-adk-project --set-as-default

# Set your project ID
export GOOGLE_CLOUD_PROJECT=my-adk-project
```

### 1.2 Enable Required APIs
```bash
# Enable Cloud AI Platform API
gcloud services enable aiplatform.googleapis.com

# Enable Vertex AI API
gcloud services enable vertexai.googleapis.com

# Enable Cloud Storage API
gcloud services enable storage.googleapis.com

# Enable Cloud Functions API
gcloud services enable cloudfunctions.googleapis.com
```

### 1.3 Create Service Account
```bash
# Create service account
gcloud iam service-accounts create adk-service-account \
    --display-name="ADK Service Account" \
    --description="Service account for Google ADK development"

# Grant necessary roles
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
    --member="serviceAccount:adk-service-account@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
    --member="serviceAccount:adk-service-account@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

# Download service account key
gcloud iam service-accounts keys create ~/adk-service-account.json \
    --iam-account=adk-service-account@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com
```

---

## 🐍 Step 2: Python Environment Setup

### 2.1 Install Python (if not already installed)
```bash
# Check Python version
python3 --version

# Install Python 3.9+ (macOS with Homebrew)
brew install python@3.9

# Install Python 3.9+ (Ubuntu/Debian)
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-pip

# Install Python 3.9+ (Windows)
# Download from https://python.org and run installer
```

### 2.2 Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv adk-env

# Activate virtual environment
# macOS/Linux:
source adk-env/bin/activate

# Windows:
adk-env\Scripts\activate
```

### 2.3 Upgrade Package Manager
```bash
# Upgrade pip
pip install --upgrade pip

# Install wheel and setuptools
pip install wheel setuptools
```

---

## 📦 Step 3: Install Google ADK

### 3.1 Install ADK Package
```bash
# Install Google ADK
pip install google-adk

# Install additional dependencies for development
pip install google-adk[dev]

# Install optional dependencies for specific features
pip install google-adk[vertex,storage,functions]
```

### 3.2 Verify Installation
```bash
# Check ADK version
python -c "import google_adk; print(google_adk.__version__)"

# List installed packages
pip list | grep google
```

---

## 🔑 Step 4: Environment Configuration

### 4.1 Set Up Authentication
```bash
# Set service account key path
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/adk-service-account.json"

# Add to your shell profile for persistence
echo 'export GOOGLE_APPLICATION_CREDENTIALS="$HOME/adk-service-account.json"' >> ~/.bashrc
echo 'export GOOGLE_APPLICATION_CREDENTIALS="$HOME/adk-service-account.json"' >> ~/.zshrc
```

### 4.2 Create Environment File
Create a `.env` file in your project directory:

```bash
# Create .env file
touch .env
```

Add the following content to `.env`:
```env
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=my-adk-project
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/adk-service-account.json

# ADK Configuration
ADK_LOG_LEVEL=INFO
ADK_CACHE_DIR=./.adk_cache

# Vertex AI Configuration
VERTEX_AI_REGION=us-central1
VERTEX_AI_MODEL=text-bison@001

# Optional: API Keys for external services
# OPENAI_API_KEY=your_openai_key_here
# ANTHROPIC_API_KEY=your_anthropic_key_here
```

### 4.3 Install Python Dependencies
Create a `requirements.txt` file:

```txt
# Core ADK dependencies
google-adk>=0.1.0
google-cloud-aiplatform>=1.25.0
google-cloud-storage>=2.10.0
google-cloud-functions>=1.10.0

# Development dependencies
python-dotenv>=1.0.0
jupyter>=1.0.0
pytest>=7.0.0
black>=23.0.0
flake8>=6.0.0

# Optional: Additional AI libraries
openai>=1.0.0
anthropic>=0.5.0
langchain>=0.0.300
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ✅ Step 5: Verify Installation

### 5.1 Create Test Script
Create a file named `test_adk_installation.py`:

```python
#!/usr/bin/env python3
"""
Test script to verify Google ADK installation
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import google_adk
        print("✅ google_adk imported successfully")
        print(f"   Version: {google_adk.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import google_adk: {e}")
        return False
    
    try:
        from google.cloud import aiplatform
        print("✅ google.cloud.aiplatform imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import aiplatform: {e}")
        return False
    
    return True

def test_environment():
    """Test if environment variables are set correctly"""
    required_vars = [
        'GOOGLE_CLOUD_PROJECT',
        'GOOGLE_APPLICATION_CREDENTIALS'
    ]
    
    all_set = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var} is set")
        else:
            print(f"❌ {var} is not set")
            all_set = False
    
    return all_set

def test_gcloud_authentication():
    """Test Google Cloud authentication"""
    try:
        from google.cloud import aiplatform
        
        # Initialize Vertex AI
        aiplatform.init(
            project=os.getenv('GOOGLE_CLOUD_PROJECT'),
            location=os.getenv('VERTEX_AI_REGION', 'us-central1')
        )
        
        print("✅ Google Cloud authentication successful")
        return True
    except Exception as e:
        print(f"❌ Google Cloud authentication failed: {e}")
        return False

def test_basic_adk_functionality():
    """Test basic ADK functionality"""
    try:
        from google_adk import Agent
        
        # Create a simple agent
        agent = Agent(
            name="test_agent",
            description="A simple test agent",
            model="text-bison@001"
        )
        
        print("✅ Basic ADK agent creation successful")
        return True
    except Exception as e:
        print(f"❌ Basic ADK functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Testing Google ADK Installation...")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Environment Test", test_environment),
        ("Authentication Test", test_gcloud_authentication),
        ("Basic ADK Test", test_basic_adk_functionality)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    if all(results):
        print("🎉 All tests passed! ADK is ready to use.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 5.2 Run Test Script
```bash
# Make the script executable
chmod +x test_adk_installation.py

# Run the test
python test_adk_installation.py
```

### Expected Output:
```
🔍 Testing Google ADK Installation...
==================================================

📋 Import Test:
✅ google_adk imported successfully
   Version: 0.1.0
✅ google.cloud.aiplatform imported successfully

📋 Environment Test:
✅ GOOGLE_CLOUD_PROJECT is set
✅ GOOGLE_APPLICATION_CREDENTIALS is set

📋 Authentication Test:
✅ Google Cloud authentication successful

📋 Basic ADK Test:
✅ Basic ADK agent creation successful

==================================================
📊 Test Results:
🎉 All tests passed! ADK is ready to use.
```

---

## 🛠️ Step 6: Development Environment Setup

### 6.1 VS Code Setup (Recommended)
Install these VS Code extensions:
- **Python** (Microsoft)
- **Google Cloud Code** (Google)
- **Jupyter** (Microsoft)
- **GitLens** (GitKraken)

### 6.2 Create Project Structure
```bash
# Create project directories
mkdir -p {agents,tools,workflows,tests,notebooks,data}
mkdir -p agents/{simple,advanced,multi-agent}
mkdir -p tools/{custom,built-in}
mkdir -p workflows/{sequential,parallel,conditional}

# Create initial files
touch agents/__init__.py
touch tools/__init__.py
touch workflows/__init__.py
touch tests/__init__.py
```

### 6.3 Git Initialization
```bash
# Initialize git repository
git init

# Create .gitignore
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv/

# ADK
.adk_cache/
*.log

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Service Account Keys
*.json
!requirements.txt
EOF

# Initial commit
git add .
git commit -m "Initial ADK project setup"
```

---

## 🚀 Step 7: First ADK Agent

Create your first ADK agent in `agents/simple/01_hello_agent.py`:

```python
#!/usr/bin/env python3
"""
Hello World Agent - Your first Google ADK agent
"""

import os
from dotenv import load_dotenv
from google_adk import Agent, Tool

# Load environment variables
load_dotenv()

def create_hello_agent():
    """Create a simple hello world agent"""
    
    # Define a simple tool
    def say_hello(name: str) -> str:
        """Say hello to someone"""
        return f"Hello, {name}! Welcome to Google ADK!"
    
    # Create the agent
    agent = Agent(
        name="hello_agent",
        description="A friendly agent that greets users",
        model="text-bison@001",
        tools=[Tool(say_hello, name="say_hello")],
        instructions="You are a friendly assistant. Use the say_hello tool to greet users."
    )
    
    return agent

def main():
    """Run the hello agent"""
    # Create agent
    agent = create_hello_agent()
    
    # Test the agent
    response = agent.run("Please greet Alice")
    
    print("Agent Response:")
    print(response)

if __name__ == "__main__":
    main()
```

Run your first agent:
```bash
python agents/simple/01_hello_agent.py
```

---

## 🔧 Common Issues & Solutions

### Issue 1: Authentication Errors
**Problem**: `Permission denied` or authentication failures
**Solution**:
```bash
# Verify service account permissions
gcloud auth activate-service-account \
    --key-file=$GOOGLE_APPLICATION_CREDENTIALS

# Check project permissions
gcloud projects get-iam-policy $GOOGLE_CLOUD_PROJECT
```

### Issue 2: Package Installation Failures
**Problem**: `pip install` fails with dependency conflicts
**Solution**:
```bash
# Upgrade pip first
pip install --upgrade pip

# Use virtual environment
python -m venv fresh_env
source fresh_env/bin/activate
pip install -r requirements.txt
```

### Issue 3: API Not Enabled
**Problem**: `API not enabled` errors
**Solution**:
```bash
# Enable all required APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable vertexai.googleapis.com
gcloud services enable storage.googleapis.com
```

### Issue 4: Memory/Resource Issues
**Problem**: Out of memory errors
**Solution**:
```bash
# Increase available memory
export ADK_MAX_MEMORY=4096

# Use smaller model for testing
export VERTEX_AI_MODEL=text-bison@001
```

---

## 📚 Next Steps

1. **Learn ADK Fundamentals** → `../03-adk-fundamentals/`
2. **Explore Examples** → `../examples/`
3. **Build Your First Real Agent** → `../../02-agent-development/`
4. **Read Documentation** → [Google ADK Docs](https://cloud.google.com/adk/docs)

---

## 🆘 Getting Help

- **Google Cloud Support**: [Support Portal](https://cloud.google.com/support)
- **Stack Overflow**: [google-cloud-adk tag](https://stackoverflow.com/questions/tagged/google-cloud-adk)
- **Google Cloud Community**: [Community Forum](https://cloud.google.com/community)
- **Documentation**: [ADK Documentation](https://cloud.google.com/adk/docs)

---

**🎉 Congratulations! You have successfully installed and set up Google ADK!**
