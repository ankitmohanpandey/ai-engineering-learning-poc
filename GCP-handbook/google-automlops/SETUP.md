# Google AutoMLOps Setup Guide

> **Complete installation and configuration guide for Google AutoMLOps**

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [GCP Project Setup](#gcp-project-setup)
4. [Authentication](#authentication)
5. [First Pipeline](#first-pipeline)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

**Required**:
- Python 3.7, 3.8, 3.9, or 3.10
- Git installed and configured
- Google Cloud SDK ≥ 407.0.0
- Active GCP project with billing enabled

**Recommended**:
- 8GB+ RAM
- 20GB+ disk space
- Linux/Mac (or WSL on Windows)

### Software Requirements

#### 1. Python (Required)

```bash
# Check Python version
python --version  # Should be 3.7-3.10

# Create virtual environment
python -m venv automlops-env
source automlops-env/bin/activate  # Linux/Mac
# OR
automlops-env\Scripts\activate  # Windows
```

#### 2. Google Cloud SDK (Required)

```bash
# Install gcloud CLI
# macOS
brew install google-cloud-sdk

# Ubuntu/Debian
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt update && sudo apt install google-cloud-sdk

# Verify installation
gcloud --version  # Should be ≥ 407.0.0

# Install beta components
gcloud components install beta
```

#### 3. Terraform (Optional, but Recommended)

```bash
# macOS
brew install terraform

# Ubuntu/Debian
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# Verify
terraform --version  # Should be ≥ v1.5.6
```

#### 4. Git Configuration (Required for CI/CD)

```bash
# Configure git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Verify
git config --list
```

---

## Installation

### Step 1: Install AutoMLOps Package

```bash
# Activate virtual environment
source automlops-env/bin/activate

# Install AutoMLOps
pip install google-cloud-automlops

# Verify installation
python -c "from google_cloud_automlops import AutoMLOps; print('AutoMLOps installed successfully!')"
```

### Step 2: Install Additional Dependencies

```bash
# Install required packages
pip install kfp>=2.0.0
pip install google-cloud-aiplatform
pip install google-cloud-pipeline-components
pip install google-cloud-storage
pip install pyyaml

# Or install from requirements.txt
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
# Check installed packages
pip list | grep google-cloud-automlops
pip list | grep kfp
pip list | grep google-cloud-aiplatform
```

---

## GCP Project Setup

### Step 1: Create or Select GCP Project

```bash
# List existing projects
gcloud projects list

# Create new project (optional)
gcloud projects create my-automlops-project --name="AutoMLOps Learning"

# Set default project
gcloud config set project my-automlops-project

# Verify
gcloud config get-value project
```

### Step 2: Enable Billing

```bash
# Link billing account (replace with your billing account ID)
gcloud beta billing projects link my-automlops-project \
  --billing-account=BILLING_ACCOUNT_ID

# Verify billing is enabled
gcloud beta billing projects describe my-automlops-project
```

### Step 3: Enable Required APIs

AutoMLOps will enable these automatically during `provision()`, but you can enable them manually:

```bash
# Enable all required APIs
gcloud services enable \
  aiplatform.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  cloudfunctions.googleapis.com \
  cloudresourcemanager.googleapis.com \
  cloudscheduler.googleapis.com \
  compute.googleapis.com \
  iam.googleapis.com \
  iamcredentials.googleapis.com \
  logging.googleapis.com \
  pubsub.googleapis.com \
  run.googleapis.com \
  storage.googleapis.com

# Verify enabled APIs
gcloud services list --enabled
```

### Step 4: Set Up Service Accounts

```bash
# Create service account for Vertex AI Pipelines
gcloud iam service-accounts create vertex-pipelines \
  --display-name="Vertex AI Pipelines Service Account"

# Grant necessary roles
PROJECT_ID=$(gcloud config get-value project)

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:vertex-pipelines@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:vertex-pipelines@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:vertex-pipelines@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:vertex-pipelines@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.user"
```

---

## Authentication

### Method 1: Application Default Credentials (Recommended)

```bash
# Login with your user account
gcloud auth application-default login

# Set account
gcloud config set account your-email@example.com

# Verify authentication
gcloud auth list
```

### Method 2: Service Account Key (For CI/CD)

```bash
# Create service account key
gcloud iam service-accounts keys create ~/automlops-key.json \
  --iam-account=vertex-pipelines@$PROJECT_ID.iam.gserviceaccount.com

# Set environment variable
export GOOGLE_APPLICATION_CREDENTIALS=~/automlops-key.json

# Verify
gcloud auth application-default print-access-token
```

### Method 3: Workload Identity Federation (For GitHub Actions)

See [GitHub Actions Integration Guide](https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines) for setting up Workload Identity Federation.

---

## First Pipeline

### Step 1: Create Project Directory

```bash
# Create project directory
mkdir my-first-automlops-pipeline
cd my-first-automlops-pipeline

# Create Python file
touch pipeline.py
```

### Step 2: Define Components and Pipeline

```python
# pipeline.py
from google_cloud_automlops import AutoMLOps

# Define component
@AutoMLOps.component
def hello_world(message: str):
    """Simple hello world component."""
    print(f"Hello from AutoMLOps: {message}")

# Define pipeline
@AutoMLOps.pipeline
def hello_pipeline(message: str):
    """Simple hello world pipeline."""
    hello_task = hello_world(message=message)

# Pipeline parameters
pipeline_params = {
    'message': 'My first AutoMLOps pipeline!'
}

# Generate, provision, and deploy
PROJECT_ID = 'my-automlops-project'  # Replace with your project ID

AutoMLOps.launchAll(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=False,
    naming_prefix='hello-world',
    provisioning_framework='gcloud'
)
```

### Step 3: Run the Pipeline

```bash
# Run the pipeline
python pipeline.py
```

This will:
1. Generate MLOps code under `AutoMLOps/` directory
2. Provision GCP infrastructure
3. Build and deploy the pipeline
4. Submit a PipelineJob to Vertex AI

### Step 4: View Pipeline in Vertex AI

```bash
# Open Vertex AI Pipelines in browser
echo "https://console.cloud.google.com/vertex-ai/pipelines?project=$PROJECT_ID"

# Or use gcloud to list pipeline jobs
gcloud ai pipelines list --region=us-central1
```

---

## Verification

### Check Generated Files

```bash
# List generated files
ls -la AutoMLOps/

# Expected structure:
# AutoMLOps/
# ├── components/
# ├── configs/
# ├── pipelines/
# ├── provision/
# ├── scripts/
# └── services/
```

### Verify GCP Resources

```bash
# Check Artifact Registry
gcloud artifacts repositories list

# Check Cloud Storage buckets
gsutil ls

# Check Cloud Functions
gcloud functions list

# Check Pub/Sub topics
gcloud pubsub topics list

# Check Cloud Scheduler jobs
gcloud scheduler jobs list
```

### Test Pipeline Execution

```bash
# Manually trigger pipeline
cd AutoMLOps/scripts
./run_all.sh

# Or publish to Pub/Sub topic
./publish_to_topic.sh
```

---

## Troubleshooting

### Issue 1: Import Error

**Symptoms**: `ModuleNotFoundError: No module named 'google_cloud_automlops'`

**Solution**:
```bash
# Ensure virtual environment is activated
source automlops-env/bin/activate

# Reinstall package
pip uninstall google-cloud-automlops
pip install google-cloud-automlops

# Verify
python -c "import google_cloud_automlops"
```

### Issue 2: Authentication Error

**Symptoms**: `google.auth.exceptions.DefaultCredentialsError`

**Solution**:
```bash
# Re-authenticate
gcloud auth application-default login

# Set project
gcloud config set project PROJECT_ID

# Verify
gcloud auth list
```

### Issue 3: API Not Enabled

**Symptoms**: `API [service] is not enabled for project [project-id]`

**Solution**:
```bash
# Enable the specific API
gcloud services enable SERVICE_NAME.googleapis.com

# Example: Enable Vertex AI
gcloud services enable aiplatform.googleapis.com
```

### Issue 4: Permission Denied

**Symptoms**: `Permission denied` or `403 Forbidden`

**Solution**:
```bash
# Check current user
gcloud config get-value account

# Add required roles
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:YOUR_EMAIL" \
  --role="roles/aiplatform.admin"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:YOUR_EMAIL" \
  --role="roles/storage.admin"
```

### Issue 5: Terraform State Issues

**Symptoms**: Terraform state conflicts

**Solution**:
```bash
# Check state bucket
gsutil ls gs://PROJECT_ID-bucket-tfstate/

# Remove lock if stuck
gsutil rm gs://PROJECT_ID-bucket-tfstate/default.tflock

# Reinitialize
cd AutoMLOps/provision
terraform init -reconfigure
```

### Issue 6: Pipeline Fails to Submit

**Symptoms**: Pipeline job submission fails

**Solution**:
```bash
# Check if resources are provisioned
python -c "
from google_cloud_automlops import AutoMLOps
AutoMLOps.deploy(precheck=True)
"

# Re-provision if needed
python -c "
from google_cloud_automlops import AutoMLOps
AutoMLOps.provision()
"

# Check service account permissions
gcloud projects get-iam-policy PROJECT_ID \
  --flatten="bindings[].members" \
  --filter="bindings.members:vertex-pipelines@*"
```

### Issue 7: Component Build Fails

**Symptoms**: Docker build fails or component image not found

**Solution**:
```bash
# Check Artifact Registry
gcloud artifacts repositories list

# Manually build component
cd AutoMLOps/scripts
./build_components.sh

# Check build logs
gcloud builds list --limit=5
```

---

## Configuration Options

### Using Terraform (Recommended for Production)

```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    provisioning_framework='terraform',  # Use Terraform
    deployment_framework='cloud-build'
)
```

### Using GitHub Actions

```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=True,
    deployment_framework='github-actions',
    source_repo_type='github',
    source_repo_name='username/repo-name',
    workload_identity_pool='projects/123/locations/global/workloadIdentityPools/pool',
    workload_identity_provider='projects/123/locations/global/workloadIdentityPools/pool/providers/provider',
    workload_identity_service_account='sa@project.iam.gserviceaccount.com'
)
```

### Using Cloud Run (Instead of Cloud Functions)

```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    pipeline_job_submission_service_type='cloud-run'
)
```

---

## Environment Variables

Create a `.env` file for local development:

```bash
# .env
PROJECT_ID=my-automlops-project
PROJECT_NUMBER=123456789
REGION=us-central1
BUCKET_NAME=my-automlops-bucket
ARTIFACT_REGISTRY=my-artifact-repo
SERVICE_ACCOUNT=vertex-pipelines@my-project.iam.gserviceaccount.com
```

Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
```

---

## Next Steps

1. **Explore Examples**: Check `01_basics/examples/`
2. **Build Components**: Learn in `02_components/`
3. **Create Pipelines**: Study `03_pipelines/`
4. **Deploy to Production**: Follow `05_deployment/`
5. **Set Up Monitoring**: Configure in `06_monitoring/`

---

## Additional Resources

- [AutoMLOps GitHub](https://github.com/GoogleCloudPlatform/automlops)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)

---

**Setup Complete! Ready to build MLOps pipelines! 🚀**
