# Google AutoMLOps Learning Repository

> **Comprehensive guide to learning Google AutoMLOps - Build MLOps Pipelines in Minutes**

A structured learning repository for mastering AutoMLOps, building production ML pipelines, and deploying models on Google Cloud Platform.

---

## 📚 Table of Contents

1. [What is AutoMLOps?](#what-is-automlops)
2. [Repository Structure](#repository-structure)
3. [Core Concepts](#core-concepts)
4. [Quick Start](#quick-start)
5. [Learning Path](#learning-path)
6. [Examples](#examples)
7. [Official Documentation](#official-documentation)
8. [Resources](#resources)

---

## What is AutoMLOps?

**Google AutoMLOps** is a tool that automatically generates production-ready MLOps pipelines on Google Cloud Platform. It allows you to build end-to-end ML pipelines with minimal configuration, using pure Python without requiring deep knowledge of underlying technologies.

### Key Features

- **Automated Pipeline Generation**: Define components and pipelines in pure Python
- **Infrastructure as Code**: Automatically provisions GCP resources
- **CI/CD Integration**: Built-in support for GitHub Actions, Cloud Build, GitLab CI
- **Flexible Orchestration**: Supports Kubeflow Pipelines, TFX, Airflow, and more
- **Model Monitoring**: Automated model monitoring and retraining capabilities
- **Multi-Tool Support**: Choose your preferred tools (Terraform, gcloud, etc.)

### Why Use AutoMLOps?

✅ **Good For**:
- Rapid MLOps pipeline development
- Standardizing ML workflows across teams
- Automating infrastructure provisioning
- Production ML deployments on GCP
- Teams without deep MLOps expertise
- Continuous training and monitoring

❌ **Not Ideal For**:
- Non-GCP cloud platforms
- Highly customized ML workflows
- Legacy on-premise systems
- Simple one-off ML experiments

### AutoMLOps vs Traditional MLOps

| Aspect | Traditional MLOps | AutoMLOps |
|--------|-------------------|-----------|
| **Setup Time** | Days/Weeks | Minutes |
| **Code Required** | Extensive | Minimal (Python only) |
| **Infrastructure** | Manual provisioning | Auto-provisioned |
| **CI/CD** | Manual setup | Auto-generated |
| **Learning Curve** | Steep | Gentle |
| **Flexibility** | High | Moderate |

---

## Repository Structure

```
google-automlops/
│
├── README.md                          # This file
├── SETUP.md                           # Installation & setup guide
├── QUICK_REFERENCE.md                # Commands & concepts cheatsheet
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore patterns
│
├── 01_basics/                        # AutoMLOps Fundamentals
│   ├── README.md                     # Basic concepts
│   ├── architecture.md               # Architecture overview
│   ├── workflow.md                   # Development workflow
│   └── examples/
│       ├── simple_component.py      # Basic component
│       ├── simple_pipeline.py       # Basic pipeline
│       └── generate_example.py      # Generate function
│
├── 02_components/                    # Component Development
│   ├── README.md                     # Component guide
│   ├── component_patterns.py        # Common patterns
│   ├── data_processing.py           # Data components
│   ├── training.py                  # Training components
│   └── examples/
│       ├── bigquery_component.py    # BigQuery integration
│       ├── gcs_component.py         # GCS operations
│       └── custom_training.py       # Custom training
│
├── 03_pipelines/                     # Pipeline Development
│   ├── README.md                     # Pipeline guide
│   ├── pipeline_patterns.py         # Common patterns
│   ├── parameter_handling.py        # Pipeline parameters
│   └── examples/
│       ├── training_pipeline.py     # Training pipeline
│       ├── batch_prediction.py      # Batch prediction
│       └── continuous_training.py   # Continuous training
│
├── 04_provisioning/                  # Infrastructure Provisioning
│   ├── README.md                     # Provisioning guide
│   ├── gcloud_provisioning.md       # Using gcloud
│   ├── terraform_provisioning.md    # Using Terraform
│   └── examples/
│       ├── provision_gcloud.py      # gcloud example
│       ├── provision_terraform.py   # Terraform example
│       └── custom_resources.tf      # Custom Terraform
│
├── 05_deployment/                    # Deployment Strategies
│   ├── README.md                     # Deployment guide
│   ├── cloud_build.md               # Cloud Build deployment
│   ├── github_actions.md            # GitHub Actions
│   ├── gitlab_ci.md                 # GitLab CI
│   └── examples/
│       ├── deploy_local.py          # Local deployment
│       ├── deploy_ci.py             # CI/CD deployment
│       └── scheduled_runs.py        # Scheduled pipelines
│
├── 06_monitoring/                    # Model Monitoring
│   ├── README.md                     # Monitoring guide
│   ├── drift_detection.md           # Data drift
│   ├── skew_detection.md            # Data skew
│   ├── auto_retraining.md           # Automatic retraining
│   └── examples/
│       ├── setup_monitoring.py      # Basic monitoring
│       ├── drift_alerts.py          # Drift detection
│       └── auto_retrain.py          # Auto-retraining
│
├── 07_advanced/                      # Advanced Topics
│   ├── README.md                     # Advanced guide
│   ├── custom_images.md             # Custom containers
│   ├── gpu_training.md              # GPU acceleration
│   ├── vpc_connector.md             # VPC networking
│   └── examples/
│       ├── gpu_training.py          # GPU example
│       ├── custom_base_image.py     # Custom image
│       └── vpc_setup.py             # VPC configuration
│
├── 08_integration/                   # Integration Patterns
│   ├── README.md                     # Integration guide
│   ├── bigquery_integration.md      # BigQuery
│   ├── vertex_ai_experiments.md     # Experiments tracking
│   ├── cloud_storage.md             # GCS integration
│   └── examples/
│       ├── bq_to_vertex.py          # BigQuery → Vertex AI
│       ├── experiments_tracking.py  # Track experiments
│       └── data_pipeline.py         # Full data pipeline
│
├── 09_best_practices/                # Best Practices
│   ├── README.md                     # Best practices guide
│   ├── component_design.md          # Component patterns
│   ├── pipeline_design.md           # Pipeline patterns
│   ├── security.md                  # Security practices
│   └── examples/
│       ├── modular_components.py    # Modular design
│       ├── error_handling.py        # Error handling
│       └── testing_pipelines.py     # Testing strategies
│
├── 10_real_world_projects/           # Complete Projects
│   ├── README.md                     # Projects overview
│   ├── image_classification/        # Image classification
│   ├── text_classification/         # Text classification
│   ├── recommendation_system/       # Recommendation engine
│   ├── time_series_forecasting/     # Time series
│   └── fraud_detection/             # Fraud detection
│
└── docs/                             # Additional Documentation
    ├── troubleshooting.md           # Common issues
    ├── faq.md                       # Frequently asked questions
    ├── migration_guide.md           # Migration strategies
    └── glossary.md                  # Terms and definitions
```

---

## Core Concepts

### 1. AutoMLOps Workflow

```
┌─────────────────────────────────────────────────────┐
│              AutoMLOps Workflow                      │
│                                                      │
│  1. Define Components (@AutoMLOps.component)        │
│           ↓                                          │
│  2. Define Pipeline (@AutoMLOps.pipeline)           │
│           ↓                                          │
│  3. Generate MLOps Code (AutoMLOps.generate())      │
│           ↓                                          │
│  4. Provision Infrastructure (AutoMLOps.provision())│
│           ↓                                          │
│  5. Deploy Pipeline (AutoMLOps.deploy())            │
│           ↓                                          │
│  6. Monitor Models (AutoMLOps.monitor())            │
└─────────────────────────────────────────────────────┘
```

---

### 2. Component Definition

Components are the building blocks of ML pipelines. Each component is a self-contained piece of code that performs a specific task.

```python
@AutoMLOps.component
def create_dataset(
    bq_table: str,
    data_path: str,
    project_id: str
):
    """Custom component that takes in a BQ table and writes it to GCS.
    
    Args:
        bq_table: The source BigQuery table.
        data_path: The GCS location to write the CSV.
        project_id: The project ID.
    """
    from google.cloud import bigquery
    import pandas as pd
    
    # Component logic here
    client = bigquery.Client(project=project_id)
    df = client.query(f"SELECT * FROM {bq_table}").to_dataframe()
    df.to_csv(data_path, index=False)
```

**Key Points**:
- Use `@AutoMLOps.component` decorator
- Include all imports inside the function
- Specify input parameters with types
- Add docstrings for documentation
- AutoMLOps automatically containerizes your code

---

### 3. Pipeline Definition

Pipelines chain together multiple components to create an end-to-end ML workflow.

```python
@AutoMLOps.pipeline
def training_pipeline(
    bq_table: str,
    model_directory: str,
    data_path: str,
    project_id: str,
    region: str
):
    """Training pipeline that processes data, trains, and deploys a model."""
    
    # Create dataset
    create_dataset_task = create_dataset(
        bq_table=bq_table,
        data_path=data_path,
        project_id=project_id
    )
    
    # Train model (runs after create_dataset)
    train_model_task = train_model(
        model_directory=model_directory,
        data_path=data_path
    ).after(create_dataset_task)
    
    # Deploy model (runs after train_model)
    deploy_model_task = deploy_model(
        model_directory=model_directory,
        project_id=project_id,
        region=region
    ).after(train_model_task)
```

**Key Points**:
- Use `@AutoMLOps.pipeline` decorator
- Chain components with `.after()`
- Pass parameters between components
- Define execution order explicitly

---

### 4. Six Core Functions

#### 1. AutoMLOps.generate()
Generates the MLOps codebase with all necessary files and configurations.

```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=False,
    naming_prefix='my-ml-pipeline',
    provisioning_framework='terraform',
    deployment_framework='cloud-build'
)
```

#### 2. AutoMLOps.provision()
Provisions GCP infrastructure using IaC (gcloud or Terraform).

```python
AutoMLOps.provision(hide_warnings=False)
```

#### 3. AutoMLOps.deprovision()
Tears down infrastructure created during provision.

```python
AutoMLOps.deprovision()
```

#### 4. AutoMLOps.deploy()
Builds containers, compiles pipeline, and submits PipelineJob.

```python
AutoMLOps.deploy(precheck=True, hide_warnings=False)
```

#### 5. AutoMLOps.launchAll()
Runs generate, provision, and deploy in succession.

```python
AutoMLOps.launchAll(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=False
)
```

#### 6. AutoMLOps.monitor()
Sets up model monitoring for deployed endpoints.

```python
AutoMLOps.monitor(
    target_field='prediction',
    model_endpoint='projects/123/locations/us-central1/endpoints/456',
    drift_thresholds={'feature1': 0.05},
    alert_emails=['team@example.com']
)
```

---

### 5. Supported Tools & Technologies

#### Artifact Repositories
- ✅ Artifact Registry

#### Deployment Frameworks
- ✅ Cloud Build
- ✅ GitHub Actions
- 🔜 GitLab CI
- 🔜 Bitbucket Pipelines
- 🔜 Jenkins

#### Orchestration Frameworks
- ✅ Kubeflow Pipelines (KFP) on Vertex AI
- 🔜 TensorFlow Extended (TFX)
- 🔜 Argo Workflows
- 🔜 Airflow on Cloud Composer
- 🔜 Ray

#### Submission Services
- ✅ Cloud Functions
- ✅ Cloud Run

#### Provisioning Frameworks
- ✅ gcloud
- ✅ Terraform
- 🔜 Pulumi

#### Source Repositories
- ✅ GitHub
- ✅ GitLab
- ✅ Bitbucket
- ✅ Cloud Source Repositories

---

## Quick Start

### Prerequisites

- Python 3.7 - 3.10
- Google Cloud SDK ≥ 407.0.0
- Terraform ≥ v1.5.6 (if using Terraform)
- Git configured with credentials

### Installation

```bash
# Install AutoMLOps
pip install google-cloud-automlops

# Import package
from google_cloud_automlops import AutoMLOps
```

### First Example - Simple Pipeline

```python
from google_cloud_automlops import AutoMLOps

# 1. Define a component
@AutoMLOps.component
def process_data(input_path: str, output_path: str):
    """Process data from input to output."""
    import pandas as pd
    
    df = pd.read_csv(input_path)
    # Process data
    df_processed = df.dropna()
    df_processed.to_csv(output_path, index=False)

# 2. Define a pipeline
@AutoMLOps.pipeline
def simple_pipeline(input_path: str, output_path: str):
    """Simple data processing pipeline."""
    process_data_task = process_data(
        input_path=input_path,
        output_path=output_path
    )

# 3. Define pipeline parameters
pipeline_params = {
    'input_path': 'gs://my-bucket/input.csv',
    'output_path': 'gs://my-bucket/output.csv'
}

# 4. Generate, provision, and deploy
AutoMLOps.launchAll(
    project_id='my-gcp-project',
    pipeline_params=pipeline_params,
    use_ci=False,
    naming_prefix='simple-pipeline'
)
```

---

## Learning Path

### 🟢 Week 1-2: Fundamentals

**Objectives**:
- Understand AutoMLOps concepts
- Learn component and pipeline definition
- Run first pipeline

**Topics**:
- AutoMLOps architecture
- Component decorators
- Pipeline decorators
- Basic generate/provision/deploy

**Practice**:
- Install AutoMLOps
- Create simple components
- Build basic pipeline
- Deploy locally

**Resources**: `01_basics/`, `02_components/`

---

### 🟡 Week 3-4: Infrastructure & Deployment

**Objectives**:
- Master infrastructure provisioning
- Learn CI/CD integration
- Understand deployment strategies

**Topics**:
- gcloud vs Terraform provisioning
- Cloud Build integration
- GitHub Actions workflows
- Scheduled pipeline runs

**Practice**:
- Provision with Terraform
- Set up CI/CD pipeline
- Configure scheduled runs
- Deploy with Cloud Build

**Resources**: `04_provisioning/`, `05_deployment/`

---

### 🟡 Week 5-6: Monitoring & Advanced Features

**Objectives**:
- Implement model monitoring
- Use advanced features
- Optimize pipelines

**Topics**:
- Data drift detection
- Data skew detection
- Automatic retraining
- GPU acceleration
- Custom base images

**Practice**:
- Set up monitoring jobs
- Configure drift alerts
- Enable auto-retraining
- Use GPU for training

**Resources**: `06_monitoring/`, `07_advanced/`

---

### 🔴 Week 7-8: Production & Best Practices

**Objectives**:
- Build production pipelines
- Follow best practices
- Complete end-to-end projects

**Topics**:
- Component design patterns
- Pipeline optimization
- Security best practices
- Testing strategies
- Real-world projects

**Practice**:
- Build production pipeline
- Implement testing
- Apply security practices
- Complete project

**Resources**: `09_best_practices/`, `10_real_world_projects/`

---

## Examples

### Example 1: Basic Component & Pipeline

```python
from google_cloud_automlops import AutoMLOps

# Component: Load data from BigQuery
@AutoMLOps.component
def load_data_from_bq(
    bq_table: str,
    output_path: str,
    project_id: str
):
    """Load data from BigQuery to GCS."""
    from google.cloud import bigquery
    
    client = bigquery.Client(project=project_id)
    query = f"SELECT * FROM `{bq_table}`"
    df = client.query(query).to_dataframe()
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

# Component: Train model
@AutoMLOps.component
def train_model(
    data_path: str,
    model_path: str
):
    """Train a simple model."""
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

# Pipeline: Chain components
@AutoMLOps.pipeline
def training_pipeline(
    bq_table: str,
    data_path: str,
    model_path: str,
    project_id: str
):
    """End-to-end training pipeline."""
    
    load_task = load_data_from_bq(
        bq_table=bq_table,
        output_path=data_path,
        project_id=project_id
    )
    
    train_task = train_model(
        data_path=data_path,
        model_path=model_path
    ).after(load_task)

# Pipeline parameters
pipeline_params = {
    'bq_table': 'my-project.dataset.table',
    'data_path': 'gs://my-bucket/data.csv',
    'model_path': 'gs://my-bucket/model.pkl',
    'project_id': 'my-gcp-project'
}

# Generate and deploy
AutoMLOps.generate(
    project_id='my-gcp-project',
    pipeline_params=pipeline_params,
    use_ci=False
)
```

---

### Example 2: GPU Training with Custom Image

```python
@AutoMLOps.component(
    packages_to_install=[
        'tensorflow==2.11.0',
        'tensorflow-datasets'
    ]
)
def train_with_gpu(
    dataset_name: str,
    model_output_path: str,
    epochs: int
):
    """Train model with GPU acceleration."""
    import tensorflow as tf
    import tensorflow_datasets as tfds
    
    # Load dataset
    dataset = tfds.load(dataset_name, split='train')
    
    # Build model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Train
    model.fit(dataset, epochs=epochs)
    model.save(model_output_path)

# Generate with GPU specs
AutoMLOps.generate(
    project_id='my-project',
    pipeline_params=pipeline_params,
    base_image='us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11.py310:latest',
    custom_training_job_specs=[{
        'component_spec': 'train_with_gpu',
        'display_name': 'gpu-training',
        'machine_type': 'a2-highgpu-1g',
        'accelerator_type': 'NVIDIA_TESLA_A100',
        'accelerator_count': 1
    }]
)
```

---

### Example 3: Model Monitoring with Auto-Retraining

```python
# First, deploy a model endpoint
# Then set up monitoring

AutoMLOps.monitor(
    target_field='prediction',
    model_endpoint='projects/my-project/locations/us-central1/endpoints/123456',
    
    # Drift detection
    drift_thresholds={
        'feature_1': 0.05,
        'feature_2': 0.10
    },
    
    # Skew detection
    skew_thresholds={
        'feature_1': 0.05,
        'feature_2': 0.10
    },
    training_dataset='gs://my-bucket/training_data.csv',
    
    # Email alerts
    alert_emails=['ml-team@example.com'],
    
    # Auto-retraining
    auto_retraining_params={
        'bq_table': 'my-project.dataset.table',
        'model_path': 'gs://my-bucket/retrained_model'
    },
    
    # Monitoring config
    monitoring_interval=1,  # hours
    sample_rate=0.8
)
```

---

## Official Documentation

### 📚 Google Cloud Official Documentation

#### AutoMLOps
- **[AutoMLOps GitHub Repository](https://github.com/GoogleCloudPlatform/automlops)** - Official source code and documentation
- **[AutoMLOps PyPI Package](https://pypi.org/project/google-cloud-automlops/)** - Python package page
- **[AutoMLOps User Guide (PDF)](https://github.com/GoogleCloudPlatform/automlops/blob/main/docs/user_guide.pdf)** - Comprehensive user guide

#### Vertex AI
- **[Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)** - Complete Vertex AI docs
- **[Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines)** - Pipeline orchestration
- **[Vertex AI Training](https://cloud.google.com/vertex-ai/docs/training/overview)** - Custom training
- **[Vertex AI Prediction](https://cloud.google.com/vertex-ai/docs/predictions/overview)** - Model serving
- **[Vertex AI Model Monitoring](https://cloud.google.com/vertex-ai/docs/model-monitoring)** - Monitoring guide
- **[Vertex AI Experiments](https://cloud.google.com/vertex-ai/docs/experiments)** - Experiment tracking

#### Kubeflow Pipelines
- **[Kubeflow Pipelines SDK](https://www.kubeflow.org/docs/components/pipelines/)** - KFP documentation
- **[KFP v2 Documentation](https://www.kubeflow.org/docs/components/pipelines/v2/)** - KFP v2 features
- **[Google Cloud Pipeline Components](https://cloud.google.com/vertex-ai/docs/pipelines/components-introduction)** - Pre-built components

### 🛠️ Infrastructure & Deployment

#### Cloud Build
- **[Cloud Build Documentation](https://cloud.google.com/build/docs)** - CI/CD with Cloud Build
- **[Build Configuration](https://cloud.google.com/build/docs/build-config-file-schema)** - cloudbuild.yaml reference
- **[Build Triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers)** - Automated builds

#### Terraform
- **[Terraform Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)** - GCP Terraform docs
- **[Terraform Best Practices](https://cloud.google.com/docs/terraform/best-practices-for-terraform)** - GCP Terraform guide

#### GitHub Actions
- **[GitHub Actions Documentation](https://docs.github.com/en/actions)** - GitHub Actions guide
- **[Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)** - Keyless authentication

### 📊 Google Cloud Services

#### Artifact Registry
- **[Artifact Registry Documentation](https://cloud.google.com/artifact-registry/docs)** - Container registry
- **[Docker Repository](https://cloud.google.com/artifact-registry/docs/docker)** - Docker images

#### Cloud Functions
- **[Cloud Functions Documentation](https://cloud.google.com/functions/docs)** - Serverless functions
- **[Cloud Functions Python](https://cloud.google.com/functions/docs/concepts/python-runtime)** - Python runtime

#### Cloud Run
- **[Cloud Run Documentation](https://cloud.google.com/run/docs)** - Serverless containers
- **[Cloud Run Services](https://cloud.google.com/run/docs/deploying)** - Deploying services

#### Cloud Scheduler
- **[Cloud Scheduler Documentation](https://cloud.google.com/scheduler/docs)** - Cron job service
- **[Cron Syntax](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules)** - Schedule patterns

#### BigQuery
- **[BigQuery Documentation](https://cloud.google.com/bigquery/docs)** - Data warehouse
- **[BigQuery ML](https://cloud.google.com/bigquery-ml/docs)** - ML in BigQuery

#### Cloud Storage
- **[Cloud Storage Documentation](https://cloud.google.com/storage/docs)** - Object storage
- **[GCS Best Practices](https://cloud.google.com/storage/docs/best-practices)** - Storage optimization

### 📖 Learning Resources

#### Google Cloud Training
- **[Google Cloud Skills Boost](https://www.cloudskillsboost.google/)** - Free labs and courses
- **[Vertex AI Qwiklabs](https://www.cloudskillsboost.google/catalog?keywords=vertex%20ai)** - Hands-on labs
- **[MLOps on Google Cloud](https://www.cloudskillsboost.google/paths/17)** - MLOps learning path

#### Codelabs & Tutorials
- **[Vertex AI Codelabs](https://codelabs.developers.google.com/?cat=aiandmachinelearning)** - Step-by-step tutorials
- **[AutoMLOps Examples](https://github.com/GoogleCloudPlatform/automlops/tree/main/examples)** - Official examples

### 🎥 Video Resources

#### YouTube Channels
- **[Google Cloud Tech](https://www.youtube.com/@googlecloudtech)** - Official GCP channel
- **[Google Cloud Platform](https://www.youtube.com/@googlecloud)** - Product updates
- **[Vertex AI Playlist](https://www.youtube.com/playlist?list=PLIivdWyY5sqJdmVMjLI8iCul14XkTRosn)** - Vertex AI videos

### 📝 Blogs & Articles

#### Official Blogs
- **[Google Cloud Blog](https://cloud.google.com/blog)** - Official blog
- **[AI & Machine Learning Blog](https://cloud.google.com/blog/products/ai-machine-learning)** - ML-focused posts
- **[Vertex AI Blog Posts](https://cloud.google.com/blog/topics/developers-practitioners/vertex-ai)** - Vertex AI articles

### 🔬 Research & Papers

- **[MLOps: Continuous delivery and automation pipelines in ML](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)** - Google's MLOps whitepaper
- **[Best practices for implementing machine learning on Google Cloud](https://cloud.google.com/architecture/ml-on-gcp-best-practices)** - Architecture guide

### 🌐 Community & Support

#### Official Community
- **[Google Cloud Community](https://www.googlecloudcommunity.com/)** - Community hub
- **[Stack Overflow - google-cloud-platform](https://stackoverflow.com/questions/tagged/google-cloud-platform)** - Q&A
- **[Stack Overflow - vertex-ai](https://stackoverflow.com/questions/tagged/vertex-ai)** - Vertex AI Q&A
- **[Google Cloud Slack](https://googlecloud-community.slack.com/)** - Community Slack

#### GitHub
- **[AutoMLOps Issues](https://github.com/GoogleCloudPlatform/automlops/issues)** - Report bugs
- **[AutoMLOps Discussions](https://github.com/GoogleCloudPlatform/automlops/discussions)** - Ask questions

### 🛠️ Tools & SDKs

#### Python SDKs
- **[Vertex AI Python SDK](https://cloud.google.com/python/docs/reference/aiplatform/latest)** - Python API reference
- **[KFP Python SDK](https://kubeflow-pipelines.readthedocs.io/)** - KFP SDK docs
- **[Google Cloud Python Client](https://github.com/googleapis/google-cloud-python)** - Python clients

#### CLI Tools
- **[gcloud CLI Reference](https://cloud.google.com/sdk/gcloud/reference)** - gcloud commands
- **[gcloud AI Platform](https://cloud.google.com/sdk/gcloud/reference/ai-platform)** - AI Platform commands

---

## Best Practices

### Component Design

1. **Single Responsibility**: Each component should do one thing well
2. **Explicit Dependencies**: Include all imports inside functions
3. **Type Annotations**: Always specify parameter types
4. **Documentation**: Add docstrings with parameter descriptions
5. **Error Handling**: Include try-except blocks for robustness

### Pipeline Design

1. **Modular Components**: Reuse components across pipelines
2. **Clear Dependencies**: Use `.after()` to specify execution order
3. **Parameter Management**: Use pipeline parameters for flexibility
4. **Naming Conventions**: Use descriptive names for components and pipelines
5. **Testing**: Test components individually before integration

### Infrastructure

1. **Use Terraform**: For production, use Terraform over gcloud
2. **Version Control**: Keep generated code in source control
3. **Naming Prefix**: Use unique prefixes to avoid conflicts
4. **Resource Cleanup**: Use `deprovision()` to clean up resources
5. **Cost Monitoring**: Monitor GCP costs regularly

### Security

1. **Service Accounts**: Use least-privilege service accounts
2. **Secrets Management**: Use Secret Manager for sensitive data
3. **VPC Networking**: Use VPC connectors for private resources
4. **Workload Identity**: Use Workload Identity Federation for GitHub Actions
5. **IAM Policies**: Review and audit IAM permissions regularly

---

## Common Use Cases

### 1. Continuous Training Pipeline
```python
# Scheduled retraining every 12 hours
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=True,
    schedule_pattern='0 */12 * * *'
)
```

### 2. Batch Prediction Pipeline
```python
# Process large datasets for predictions
@AutoMLOps.pipeline
def batch_prediction_pipeline(
    input_data: str,
    model_endpoint: str,
    output_path: str
):
    # Load data, run predictions, save results
    pass
```

### 3. Model Monitoring & Retraining
```python
# Auto-retrain on drift detection
AutoMLOps.monitor(
    target_field='prediction',
    model_endpoint=endpoint,
    drift_thresholds={'feature': 0.05},
    auto_retraining_params=pipeline_params
)
```

---

## Troubleshooting

### Common Issues

**Import Error: No module named 'google_cloud_automlops'**:
```bash
pip install google-cloud-automlops
```

**Permission Denied**:
```bash
# Check IAM permissions
gcloud projects get-iam-policy PROJECT_ID

# Add required roles
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL" \
  --role="roles/aiplatform.user"
```

**Pipeline Fails to Submit**:
```bash
# Check if resources are provisioned
AutoMLOps.deploy(precheck=True)

# Re-provision if needed
AutoMLOps.provision()
```

**Terraform State Issues**:
```bash
# Check state bucket
gsutil ls gs://PROJECT_ID-bucket-tfstate/

# Reinitialize if needed
cd AutoMLOps/provision
terraform init -reconfigure
```

---

## Next Steps

1. **Setup AutoMLOps**: Follow [SETUP.md](SETUP.md)
2. **Learn Basics**: Start with `01_basics/`
3. **Build Components**: Work through `02_components/`
4. **Create Pipelines**: Study `03_pipelines/`
5. **Deploy to Production**: Complete `10_real_world_projects/`

---

## Contributing

Add your own:
- Component patterns
- Pipeline examples
- Best practices
- Real-world use cases

---

## License

This is a learning repository. Use freely for educational purposes.

---

**Happy Learning! 🚀**

*AutoMLOps - Build MLOps Pipelines in Minutes on Google Cloud Platform*
