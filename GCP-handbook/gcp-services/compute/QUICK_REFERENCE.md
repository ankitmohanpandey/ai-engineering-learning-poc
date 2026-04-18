# Compute Services Quick Reference

## 🚀 Common Commands

### Compute Engine

#### Instance Management
```bash
# Create VM instance
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud

# List instances
gcloud compute instances list

# SSH into instance
gcloud compute ssh my-vm --zone=us-central1-a

# Stop instance
gcloud compute instances stop my-vm --zone=us-central1-a

# Start instance
gcloud compute instances start my-vm --zone=us-central1-a

# Delete instance
gcloud compute instances delete my-vm --zone=us-central1-a
```

#### Firewall Rules
```bash
# Create firewall rule
gcloud compute firewall-rules create allow-http \
  --allow tcp:80 \
  --source-ranges 0.0.0.0/0 \
  --target-tags http-server

# List firewall rules
gcloud compute firewall-rules list
```

### Google Kubernetes Engine (GKE)

#### Cluster Management
```bash
# Create GKE cluster
gcloud container clusters create my-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-medium

# Get cluster credentials
gcloud container clusters get-credentials my-cluster \
  --zone=us-central1-a

# List clusters
gcloud container clusters list

# Delete cluster
gcloud container clusters delete my-cluster \
  --zone=us-central1-a
```

#### Kubernetes Commands
```bash
# Deploy application
kubectl apply -f deployment.yaml

# Get pods
kubectl get pods

# Get services
kubectl get services

# Scale deployment
kubectl scale deployment my-app --replicas=3

# Port forward
kubectl port-forward service/my-service 8080:80
```

### Cloud Run

#### Deployment
```bash
# Deploy service
gcloud run deploy my-service \
  --image=gcr.io/PROJECT-ID/my-image \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated

# List services
gcloud run services list

# Update service
gcloud run services update my-service \
  --image=gcr.io/PROJECT-ID/new-image \
  --region=us-central1

# Delete service
gcloud run services delete my-service --region=us-central1
```

### App Engine

#### Application Management
```bash
# Deploy application
gcloud app deploy

# Browse application
gcloud app browse

# View application logs
gcloud app logs tail -s default

# List versions
gcloud app versions list
```

### Cloud Functions

#### Function Management
```bash
# Deploy function
gcloud functions deploy my-function \
  --runtime=python39 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point=hello_world

# List functions
gcloud functions list

# Call function
gcloud functions call my-function --data='{"name":"World"}'

# Delete function
gcloud functions delete my-function
```

## 📊 Resource Limits

### Compute Engine
- **Instances per region**: 7500 (default)
- **CPUs per region**: 48000 (default)
- **Persistent disks**: 1000 (default)
- **External IP addresses**: 250 (default)

### GKE
- **Clusters per region**: 10 (default)
- **Nodes per cluster**: 5000 (default)
- **Pods per node**: 110 (default)
- **Services per cluster**: 5000 (default)

### Cloud Run
- **Container instances**: 1000 (default)
- **Memory per container**: 32 GiB (max)
- **CPU per container**: 8 vCPU (max)
- **Request timeout**: 60 minutes (max)

## 🔧 Configuration Files

### Compute Engine Startup Script
```bash
#!/bin/bash
# Install dependencies
apt-get update
apt-get install -y nginx

# Start service
systemctl start nginx
systemctl enable nginx
```

### Kubernetes Deployment YAML
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: gcr.io/PROJECT-ID/my-image
        ports:
        - containerPort: 80
```

### Cloud Function (Python)
```python
import functions_framework

@functions_framework.http
def hello_world(request):
    """HTTP Cloud Function."""
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'
```

## 🏷️ Machine Types

### Compute Engine
- **E2**: Cost-effective, general purpose
- **N2**: Balanced performance and price
- **N2D**: AMD-based, cost-effective
- **C2**: Compute-optimized
- **M2**: Memory-optimized
- **A2**: Accelerator-optimized (GPU)

### GKE Machine Types
- **E2-standard**: General purpose workloads
- **N1-standard**: Balanced workloads
- **N2-standard**: Latest generation
- **E2-highmem**: Memory-intensive
- **E2-highcpu**: Compute-intensive

## 🔍 Monitoring Commands

```bash
# Check instance status
gcloud compute instances describe my-vm --zone=us-central1-a

# View resource usage
gcloud monitoring metrics list

# Check cluster status
kubectl cluster-info

# View function logs
gcloud functions logs read my-function
```

## 📞 Support Commands

```bash
# Get help
gcloud compute instances create --help

# Check configuration
gcloud config list

# Set project
gcloud config set project PROJECT-ID

# Set region
gcloud config set compute/region us-central1
```

---

*For detailed setup instructions, see [SETUP.md](./SETUP.md)*
*For service overview, see [README.md](./README.md)*
