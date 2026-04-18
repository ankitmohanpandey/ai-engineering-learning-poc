# Compute Services

Google Cloud Platform provides a comprehensive suite of compute services to run your applications and workloads at scale.

## 🚀 Services Overview

### 1. Compute Engine
**Virtual Machines on Google Infrastructure**

- **Description**: Scalable virtual machines running in Google's data centers
- **Use Cases**: 
  - Web applications and APIs
  - Development and testing environments
  - High-performance computing
  - Database servers
- **Key Features**:
  - Predefined and custom machine types
  - Live migration
  - Autoscaling
  - Global load balancing
- **Pricing**: Pay-per-second billing, sustained use discounts
- **Documentation**: [Compute Engine Docs](https://cloud.google.com/compute/docs)

### 2. Google Kubernetes Engine (GKE)
**Managed Kubernetes Service**

- **Description**: Fully managed Kubernetes container orchestration
- **Use Cases**:
  - Microservices architecture
  - Containerized applications
  - CI/CD pipelines
  - Hybrid cloud deployments
- **Key Features**:
  - Automated upgrades and repairs
  - Node auto-repair
  - Cluster autoscaling
  - Multi-cluster management
- **Pricing**: Free tier available, pay for cluster management and nodes
- **Documentation**: [GKE Docs](https://cloud.google.com/kubernetes-engine/docs)

### 3. Cloud Run
**Serverless Container Platform**

- **Description**: Run containers without managing infrastructure
- **Use Cases**:
  - HTTP-based microservices
  - Event-driven applications
  - API backends
  - Web applications
- **Key Features**:
  - Automatic scaling to zero
  - Pay-per-request pricing
  - Traffic splitting
  - Binary authorization
- **Pricing**: Pay only for CPU, memory, and requests used
- **Documentation**: [Cloud Run Docs](https://cloud.google.com/run/docs)

### 4. App Engine
**Platform as a Service (PaaS)**

- **Description**: Fully managed platform for building and deploying applications
- **Use Cases**:
  - Web applications
  - Mobile backends
  - API services
  - Business applications
- **Key Features**:
  - Automatic scaling
  - Built-in services (memcache, task queues)
  - Version management
  - Traffic splitting
- **Pricing**: Free tier available, pay for resources used
- **Documentation**: [App Engine Docs](https://cloud.google.com/appengine/docs)

### 5. Cloud Functions
**Serverless Functions**

- **Description**: Event-driven serverless compute functions
- **Use Cases**:
  - Data processing
  - Real-time file processing
  - IoT data processing
  - Webhook endpoints
- **Key Features**:
  - Event-driven execution
  - Multiple language support
  - Automatic scaling
  - Pay-per-invocation pricing
- **Pricing**: Free tier, pay per invocation and execution time
- **Documentation**: [Cloud Functions Docs](https://cloud.google.com/functions/docs)

## 📊 Comparison Table

| Service | Management Level | Scaling | Pricing Model | Best For |
|---------|------------------|---------|---------------|----------|
| Compute Engine | IaaS | Manual/Auto | Per-second | Full control, legacy apps |
| GKE | CaaS | Automatic | Per-node | Container orchestration |
| Cloud Run | Serverless | Automatic | Per-request | HTTP services |
| App Engine | PaaS | Automatic | Per-resource | Web applications |
| Cloud Functions | FaaS | Automatic | Per-invocation | Event-driven tasks |

## 🛠️ Getting Started

1. **Choose your service** based on your use case and management preferences
2. **Set up authentication** with Google Cloud SDK
3. **Follow the setup guide** for your chosen service
4. **Deploy your first application** using the quick start guides

## 📚 Learning Resources

- [Compute Quick Start](https://cloud.google.com/compute/docs/quickstart)
- [GKE Quick Start](https://cloud.google.com/kubernetes-engine/docs/quickstart)
- [Cloud Run Quick Start](https://cloud.google.com/run/docs/quickstart)
- [App Engine Quick Start](https://cloud.google.com/appengine/docs/standard/python/quickstart)
- [Cloud Functions Quick Start](https://cloud.google.com/functions/docs/quickstart)

## 🔗 Related Services

- **Cloud Load Balancing** - Distribute traffic across instances
- **Cloud CDN** - Content delivery network
- **VPC Network** - Networking infrastructure
- **Cloud Monitoring** - Performance monitoring
- **Cloud Logging** - Log management

---

*For detailed setup instructions, see [SETUP.md](./SETUP.md)*
*For quick commands and reference, see [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)*
