# Compute Services Setup Guide

## 🚀 Prerequisites

1. **Google Cloud Account**: Create account at [cloud.google.com](https://cloud.google.com)
2. **Enable Billing**: Add payment method to your account
3. **Install Google Cloud SDK**: Download from [cloud.google.com/sdk](https://cloud.google.com/sdk/docs/install)

## 📥 Initial Setup

### 1. Install Google Cloud SDK

#### macOS
```bash
# Using Homebrew
brew install google-cloud-sdk

# Initialize gcloud
gcloud init
```

#### Linux
```bash
# Download and install
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

#### Windows
```powershell
# Download installer from cloud.google.com/sdk
# Run installer and restart PowerShell
gcloud init
```

### 2. Authenticate
```bash
# Login to your Google Account
gcloud auth login

# Set up application default credentials
gcloud auth application-default login
```

### 3. Configure Project
```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Set default region and zone
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

## 🖥️ Compute Engine Setup

### 1. Enable API
```bash
gcloud services enable compute.googleapis.com
```

### 2. Create Network (Optional)
```bash
# Create custom VPC
gcloud compute networks create my-network --subnet-mode=custom

# Create subnet
gcloud compute networks subnets create my-subnet \
  --network=my-network \
  --range=10.0.0.0/24 \
  --region=us-central1
```

### 3. Create SSH Keys
```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"

# Add SSH key to metadata
gcloud compute project-info add-metadata \
  --metadata-from-file ssh-keys=~/.ssh/id_rsa.pub
```

### 4. Create First Instance
```bash
# Create VM with startup script
gcloud compute instances create my-first-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=20GB \
  --network-interface=network=default,address= \
  --tags=http-server,https-server \
  --metadata=startup-script='#!/bin/bash
    apt-get update
    apt-get install -y nginx
    systemctl start nginx
    systemctl enable nginx'
```

### 5. Configure Firewall
```bash
# Allow HTTP traffic
gcloud compute firewall-rules create allow-http \
  --allow tcp:80 \
  --source-ranges 0.0.0.0/0 \
  --target-tags=http-server \
  --description="Allow HTTP traffic"

# Allow HTTPS traffic
gcloud compute firewall-rules create allow-https \
  --allow tcp:443 \
  --source-ranges 0.0.0.0/0 \
  --target-tags=https-server \
  --description="Allow HTTPS traffic"
```

## ☸️ Google Kubernetes Engine (GKE) Setup

### 1. Enable Required APIs
```bash
gcloud services enable container.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### 2. Install kubectl
```bash
# Install kubectl
gcloud components install kubectl

# Verify installation
kubectl version --client
```

### 3. Create GKE Cluster
```bash
# Create standard cluster
gcloud container clusters create my-gke-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-medium \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=10 \
  --enable-autorepair \
  --enable-autoupgrade

# Get cluster credentials
gcloud container clusters get-credentials my-gke-cluster \
  --zone=us-central1-a
```

### 4. Deploy Sample Application
```bash
# Create deployment
kubectl create deployment hello-server \
  --image=gcr.io/google-samples/hello-app:1.0

# Expose service
kubectl expose deployment hello-server \
  --type=LoadBalancer \
  --port=80 \
  --target-port=8080

# Check status
kubectl get service hello-server
```

## 🏃 Cloud Run Setup

### 1. Enable APIs
```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

### 2. Create Artifact Registry Repository
```bash
# Create repository
gcloud artifacts repositories create my-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker repository"

# Configure Docker authentication
gcloud auth configure-docker us-central1-docker.pkg.dev
```

### 3. Create Sample Application
```python
# main.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "main.py"]
```

```text
# requirements.txt
Flask==2.0.1
```

### 4. Build and Deploy
```bash
# Build and push image
gcloud builds submit --tag us-central1-docker.pkg.dev/PROJECT-ID/my-repo/my-app .

# Deploy to Cloud Run
gcloud run deploy my-service \
  --image=us-central1-docker.pkg.dev/PROJECT-ID/my-repo/my-app \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated
```

## 📱 App Engine Setup

### 1. Enable API
```bash
gcloud services enable appengine.googleapis.com
```

### 2. Create App Engine Application
```bash
# Create app (choose region when prompted)
gcloud app create
```

### 3. Create Sample Application
```python
# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, App Engine!'

if __name__ == '__main__':
    app.run()
```

```yaml
# app.yaml
runtime: python39
instance_class: F2

handlers:
- url: /.*
  script: auto
```

```text
# requirements.txt
Flask==2.0.1
```

### 4. Deploy Application
```bash
# Deploy to App Engine
gcloud app deploy

# Browse application
gcloud app browse
```

## ⚡ Cloud Functions Setup

### 1. Enable APIs
```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### 2. Create Sample Function
```python
# main.py
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    
    return f'Hello, {name}!'
```

```json
// package.json
{
  "name": "hello-function",
  "version": "1.0.0",
  "dependencies": {
    "functions-framework": "^3.0.0"
  }
}
```

### 3. Deploy Function
```bash
# Deploy HTTP function
gcloud functions deploy hello-http \
  --runtime=python39 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point=hello-http \
  --region=us-central1
```

## 🔧 Development Tools Setup

### 1. Cloud Shell
- Access via [console.cloud.google.com](https://console.cloud.google.com)
- Pre-installed with all necessary tools
- No local setup required

### 2. IDE Integration
```bash
# Install Cloud Code for VS Code
# Search "Cloud Code" in VS Code extensions

# Install IntelliJ plugin
# File > Settings > Plugins > Search "Google Cloud"
```

### 3. Local Development
```bash
# Install Docker for local testing
# Download from docker.com

# Install Minikube for local Kubernetes
# Follow instructions at kubernetes.io/docs/tasks/tools/
```

## 📊 Monitoring and Logging Setup

### 1. Enable Monitoring
```bash
gcloud services enable monitoring.googleapis.com
gcloud services enable logging.googleapis.com
```

### 2. Create Dashboards
```bash
# Use Cloud Console > Monitoring > Dashboards
# Create custom dashboards for your services
```

### 3. Set Up Alerts
```bash
# Use Cloud Console > Monitoring > Alerting
# Create notification channels and alerting policies
```

## 🧹 Cleanup Commands

```bash
# Delete Compute Engine instance
gcloud compute instances delete my-first-vm --zone=us-central1-a

# Delete GKE cluster
gcloud container clusters delete my-gke-cluster --zone=us-central1-a

# Delete Cloud Run service
gcloud run services delete my-service --region=us-central1

# Delete App Engine version
gcloud app versions delete VERSION_ID

# Delete Cloud Function
gcloud functions delete hello-http --region=us-central1
```

## 🆘 Troubleshooting

### Common Issues
1. **Permission denied**: Run `gcloud auth login`
2. **API not enabled**: Enable required APIs
3. **Quota exceeded**: Request quota increase
4. **Network issues**: Check firewall rules

### Debug Commands
```bash
# Check gcloud configuration
gcloud config list

# Verify APIs are enabled
gcloud services list --enabled

# Check project permissions
gcloud projects get-iam-policy PROJECT_ID
```

---

*For quick commands, see [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)*
*For service overview, see [README.md](./README.md)*
