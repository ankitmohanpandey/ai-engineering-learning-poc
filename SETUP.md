# AI Engineering Setup Guide

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher (3.10+ recommended)
- **pip**: Latest version
- **Git**: For version control
- **Text Editor/IDE**: VS Code, PyCharm, or similar
- **API Keys**: At least one LLM provider (Gemini, OpenAI, etc.)

### Check Python Version
```bash
python --version
# or
python3 --version

# Should show Python 3.8 or higher
```

### Install Python (if needed)
```bash
# macOS (using Homebrew)
brew install python@3.11

# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip

# Windows
# Download from https://www.python.org/downloads/
```

---

## Installation Steps

### Step 1: Navigate to Repository

```bash
cd "/Users/5149844/windsurf/personal learning/learning/ai-engineering-learning-poc"
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Set Up Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your API keys
# Use your preferred text editor:
nano .env
# or
code .env
# or
vim .env
```

**Add your API keys to `.env`:**
```bash
# Google Gemini
GEMINI_API_KEY=your_gemini_api_key_here

# OpenAI (optional)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic Claude (optional)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Vector Database (optional)
PINECONE_API_KEY=your_pinecone_key_here
PINECONE_ENVIRONMENT=your_environment_here
```

### Step 5: Verify Setup

```bash
# Test environment loading
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key loaded:', bool(os.getenv('GEMINI_API_KEY')))"

# Should print: API Key loaded: True
```

---

## Getting API Keys

### Google Gemini API Key

1. **Visit**: https://makersuite.google.com/app/apikey
2. **Sign in** with Google account
3. **Click** "Create API Key"
4. **Copy** the key
5. **Add** to `.env` file

**Free Tier:**
- 60 requests per minute
- 1,500 requests per day
- Free to use

### OpenAI API Key (Optional)

1. **Visit**: https://platform.openai.com/api-keys
2. **Sign up** or sign in
3. **Create** new secret key
4. **Copy** the key (you won't see it again!)
5. **Add** to `.env` file

**Pricing:**
- Pay-as-you-go
- GPT-3.5: ~$0.002/1K tokens
- GPT-4: ~$0.03/1K tokens

### Anthropic Claude API Key (Optional)

1. **Visit**: https://console.anthropic.com/
2. **Sign up** for account
3. **Navigate** to API Keys
4. **Create** new key
5. **Add** to `.env` file

---

## Running Your First Example

### Test LLM Connection

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Run Gemini integration test
python integrations/gemini_integration.py

# Expected output:
# ✓ Successfully connected to Gemini
# Response: [AI generated response]
```

### Try Simple Chat

```bash
# Run simple chat example
python poc/examples/simple_chat.py

# You should see an interactive chat interface
```

### Explore Basic Prompts

```bash
# Run basic prompt examples
python llm-concepts/examples/basic_prompts.py

# This will demonstrate various prompt patterns
```

---

## Project Structure Setup

All folders are already created. Here's what each contains:

```
ai-engineering-learning-poc/
├── basics/              # AI/ML fundamentals (documentation)
├── llm-concepts/        # LLM concepts and examples
├── architecture/        # System design documentation
├── poc/                 # Your AI agent POC code
├── integrations/        # LLM provider integrations
├── security/            # Security best practices
├── notebooks/           # Jupyter notebooks for experiments
├── docs/                # Additional documentation
└── progress/            # Learning progress tracking
```

---

## Development Workflow

### Daily Workflow

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Pull latest changes (if using Git)
git pull

# 3. Work on your code/learning

# 4. Run tests
python -m pytest tests/  # If you add tests

# 5. Deactivate when done
deactivate
```

### Adding New Dependencies

```bash
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Or manually add to requirements.txt
echo "package-name==version" >> requirements.txt
```

---

## Jupyter Notebook Setup

### Install Jupyter

```bash
# Already included in requirements.txt
# But if needed:
pip install jupyter notebook ipykernel

# Add virtual environment to Jupyter
python -m ipykernel install --user --name=ai-eng-venv
```

### Start Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or Jupyter Lab
jupyter lab

# Navigate to notebooks/ folder
```

### Create New Notebook

1. Click "New" → "Notebook"
2. Select "ai-eng-venv" kernel
3. Start experimenting!

---

## IDE Setup

### VS Code

**Recommended Extensions:**
- Python (Microsoft)
- Pylance
- Jupyter
- Python Docstring Generator
- GitLens

**Settings:**
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### PyCharm

1. **Open** project folder
2. **Configure** Python interpreter:
   - File → Settings → Project → Python Interpreter
   - Add → Existing Environment
   - Select `venv/bin/python`
3. **Mark** directories:
   - Right-click folders → Mark Directory as → Sources Root

---

## Troubleshooting

### Issue 1: ModuleNotFoundError

**Symptom:**
```
ModuleNotFoundError: No module named 'google.generativeai'
```

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Verify installation
pip show google-generativeai
```

### Issue 2: API Key Not Found

**Symptom:**
```
Error: GEMINI_API_KEY not found in environment
```

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify .env content
cat .env

# Ensure python-dotenv is installed
pip install python-dotenv

# Load environment in Python:
from dotenv import load_dotenv
load_dotenv()
```

### Issue 3: Permission Denied

**Symptom:**
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
```bash
# Fix file permissions
chmod +x script_name.py

# Or run with python explicitly
python script_name.py
```

### Issue 4: Rate Limit Exceeded

**Symptom:**
```
RateLimitError: Quota exceeded
```

**Solution:**
```python
# Add rate limiting
import time

def call_with_retry(func, max_retries=3):
    for i in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if i < max_retries - 1:
                time.sleep(2 ** i)  # Exponential backoff
            else:
                raise
```

### Issue 5: SSL Certificate Error

**Symptom:**
```
SSLError: certificate verify failed
```

**Solution:**
```bash
# macOS: Install certificates
/Applications/Python\ 3.11/Install\ Certificates.command

# Or update certifi
pip install --upgrade certifi

# Or disable SSL verification (NOT recommended for production)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

---

## Testing Your Setup

### Run All Tests

```bash
# Create a test script
cat > test_setup.py << 'EOF'
import os
from dotenv import load_dotenv

def test_environment():
    load_dotenv()
    
    # Test 1: Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    assert api_key, "GEMINI_API_KEY not found"
    print("✓ API key loaded")
    
    # Test 2: Import packages
    try:
        import google.generativeai as genai
        print("✓ google-generativeai imported")
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    
    # Test 3: Configure API
    try:
        genai.configure(api_key=api_key)
        print("✓ API configured")
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False
    
    # Test 4: List models
    try:
        models = genai.list_models()
        print(f"✓ Found {len(list(models))} models")
    except Exception as e:
        print(f"✗ API call error: {e}")
        return False
    
    print("\n✅ All tests passed! Setup is complete.")
    return True

if __name__ == "__main__":
    test_environment()
EOF

# Run test
python test_setup.py
```

---

## Environment Management

### Multiple Environments

```bash
# Development
cp .env.example .env.development

# Production
cp .env.example .env.production

# Load specific environment
# In your code:
from dotenv import load_dotenv
load_dotenv('.env.development')
```

### Environment Variables Reference

```bash
# Required
GEMINI_API_KEY=          # Google Gemini API key

# Optional LLM Providers
OPENAI_API_KEY=          # OpenAI API key
ANTHROPIC_API_KEY=       # Anthropic Claude API key

# Vector Databases
PINECONE_API_KEY=        # Pinecone API key
PINECONE_ENVIRONMENT=    # Pinecone environment
QDRANT_URL=              # Qdrant URL
QDRANT_API_KEY=          # Qdrant API key

# Configuration
LOG_LEVEL=INFO           # Logging level
MAX_TOKENS=2048          # Default max tokens
TEMPERATURE=0.7          # Default temperature

# Security
RATE_LIMIT=60            # Requests per minute
TIMEOUT=30               # Request timeout in seconds
```

---

## Production Deployment

### Environment Setup

```bash
# Use production environment
export ENV=production

# Set production API keys
export GEMINI_API_KEY=prod_key_here

# Disable debug mode
export DEBUG=False
```

### Security Checklist

- [ ] Never commit `.env` file
- [ ] Use environment-specific configs
- [ ] Enable rate limiting
- [ ] Implement error handling
- [ ] Add logging
- [ ] Monitor API usage
- [ ] Set up alerts
- [ ] Use HTTPS only

### Monitoring

```python
# Add logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

---

## Updating Dependencies

### Check for Updates

```bash
# List outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update all packages (careful!)
pip install --upgrade -r requirements.txt
```

### Version Pinning

```bash
# Pin exact versions (recommended)
google-generativeai==0.3.2

# Pin minimum version
google-generativeai>=0.3.0

# Pin compatible version
google-generativeai~=0.3.0
```

---

## Cleanup

### Remove Virtual Environment

```bash
# Deactivate first
deactivate

# Remove virtual environment
rm -rf venv

# Recreate if needed
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Clear Cache

```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Clear pip cache
pip cache purge
```

---

## Quick Reference

### Common Commands

```bash
# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run example
python poc/examples/simple_chat.py

# Start Jupyter
jupyter notebook

# Deactivate environment
deactivate
```

### File Locations

- **Virtual Environment**: `venv/`
- **Dependencies**: `requirements.txt`
- **Environment Variables**: `.env`
- **Examples**: `poc/examples/`
- **Documentation**: `docs/`

---

## Next Steps

1. ✅ Complete setup
2. 📚 Read [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md)
3. 💻 Run first example
4. 📝 Start learning!

---

## Support

If you encounter issues:
1. Check [Troubleshooting](#troubleshooting) section
2. Review error messages carefully
3. Check API key validity
4. Verify internet connection
5. Consult official documentation

---

**Setup Complete! Ready to build AI systems! 🚀**
