# AutoMLOps Quick Reference

> **Quick commands and concepts cheatsheet**

---

## Core Functions

### AutoMLOps.generate()
```python
from google_cloud_automlops import AutoMLOps

AutoMLOps.generate(
    project_id='my-project',              # Required
    pipeline_params=pipeline_params,      # Required
    use_ci=False,                         # Use CI/CD
    naming_prefix='my-pipeline',          # Unique prefix
    provisioning_framework='terraform',   # gcloud | terraform
    deployment_framework='cloud-build',   # cloud-build | github-actions
    orchestration_framework='kfp',        # kfp | tfx | airflow
    pipeline_job_submission_service_type='cloud-functions'  # cloud-functions | cloud-run
)
```

### AutoMLOps.provision()
```python
AutoMLOps.provision(hide_warnings=False)
```

### AutoMLOps.deprovision()
```python
AutoMLOps.deprovision()  # Only works with Terraform
```

### AutoMLOps.deploy()
```python
AutoMLOps.deploy(
    precheck=True,        # Check if resources exist
    hide_warnings=False   # Show permission warnings
)
```

### AutoMLOps.launchAll()
```python
AutoMLOps.launchAll(
    project_id='my-project',
    pipeline_params=pipeline_params,
    use_ci=False,
    naming_prefix='my-pipeline'
)
```

### AutoMLOps.monitor()
```python
AutoMLOps.monitor(
    target_field='prediction',
    model_endpoint='projects/123/locations/us-central1/endpoints/456',
    drift_thresholds={'feature1': 0.05},
    skew_thresholds={'feature1': 0.05},
    training_dataset='gs://bucket/training_data.csv',
    alert_emails=['team@example.com'],
    auto_retraining_params=pipeline_params,
    monitoring_interval=1,  # hours
    sample_rate=0.8
)
```

---

## Component Definition

### Basic Component
```python
@AutoMLOps.component
def my_component(input_param: str, output_param: str):
    """Component description.
    
    Args:
        input_param: Input description.
        output_param: Output description.
    """
    # Import inside function
    import pandas as pd
    
    # Component logic
    df = pd.read_csv(input_param)
    df.to_csv(output_param)
```

### Component with Packages
```python
@AutoMLOps.component(
    packages_to_install=[
        'pandas==2.0.0',
        'scikit-learn>=1.3.0',
        'google-cloud-bigquery'
    ]
)
def my_component(param: str):
    """Component with specific packages."""
    import pandas as pd
    # Logic here
```

---

## Pipeline Definition

### Basic Pipeline
```python
@AutoMLOps.pipeline
def my_pipeline(param1: str, param2: str):
    """Pipeline description."""
    
    task1 = component1(input=param1)
    
    task2 = component2(
        input=param2
    ).after(task1)
    
    task3 = component3(
        input=param2
    ).after(task2)
```

### Pipeline with Parameters
```python
pipeline_params = {
    'project_id': 'my-project',
    'region': 'us-central1',
    'bucket': 'gs://my-bucket',
    'bq_table': 'project.dataset.table',
    'model_path': 'gs://my-bucket/model'
}
```

---

## Generate Parameters

### Tooling Options

```python
# Provisioning Framework
provisioning_framework='gcloud'      # Default
provisioning_framework='terraform'   # Recommended for production

# Deployment Framework
deployment_framework='github-actions'  # Default
deployment_framework='cloud-build'
deployment_framework='gitlab-ci'       # Coming soon
deployment_framework='bitbucket-pipelines'  # Coming soon

# Orchestration Framework
orchestration_framework='kfp'         # Default (Kubeflow Pipelines)
orchestration_framework='tfx'         # Coming soon
orchestration_framework='airflow'     # Coming soon

# Submission Service
pipeline_job_submission_service_type='cloud-functions'  # Default
pipeline_job_submission_service_type='cloud-run'

# Source Repository
source_repo_type='github'   # Default
source_repo_type='gitlab'
source_repo_type='bitbucket'
```

### Common Parameters

```python
AutoMLOps.generate(
    # Required
    project_id='my-project',
    pipeline_params=pipeline_params,
    
    # Naming
    naming_prefix='my-pipeline',
    
    # Locations
    artifact_repo_location='us-central1',
    pipeline_job_location='us-central1',
    storage_bucket_location='us-central1',
    
    # CI/CD
    use_ci=False,
    source_repo_name='username/repo',
    source_repo_branch='main',
    
    # Scheduling
    schedule_pattern='0 */12 * * *',  # Cron format
    
    # Monitoring
    setup_model_monitoring=False,
    
    # Compute
    base_image='python:3.9-slim',
    custom_training_job_specs=[{
        'component_spec': 'train_model',
        'machine_type': 'n1-standard-4',
        'accelerator_type': 'NVIDIA_TESLA_T4',
        'accelerator_count': 1
    }],
    
    # Networking
    vpc_connector='my-vpc-connector',
    
    # Service Accounts
    pipeline_job_runner_service_account='sa@project.iam.gserviceaccount.com'
)
```

---

## gcloud Commands

### Project Setup
```bash
# Set project
gcloud config set project PROJECT_ID

# Enable APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable storage.googleapis.com

# List enabled APIs
gcloud services list --enabled
```

### Authentication
```bash
# Login
gcloud auth login
gcloud auth application-default login

# Set account
gcloud config set account EMAIL

# List accounts
gcloud auth list
```

### Service Accounts
```bash
# Create service account
gcloud iam service-accounts create vertex-pipelines \
  --display-name="Vertex AI Pipelines"

# Grant roles
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:vertex-pipelines@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Create key
gcloud iam service-accounts keys create key.json \
  --iam-account=vertex-pipelines@PROJECT_ID.iam.gserviceaccount.com
```

### Vertex AI
```bash
# List pipeline jobs
gcloud ai pipelines list --region=us-central1

# Describe pipeline job
gcloud ai pipelines describe PIPELINE_JOB_ID --region=us-central1

# List models
gcloud ai models list --region=us-central1

# List endpoints
gcloud ai endpoints list --region=us-central1
```

### Cloud Storage
```bash
# List buckets
gsutil ls

# Create bucket
gsutil mb -l us-central1 gs://BUCKET_NAME

# Upload file
gsutil cp local_file.txt gs://BUCKET_NAME/

# Download file
gsutil cp gs://BUCKET_NAME/file.txt ./

# List files
gsutil ls gs://BUCKET_NAME/
```

### Artifact Registry
```bash
# List repositories
gcloud artifacts repositories list

# Create repository
gcloud artifacts repositories create REPO_NAME \
  --repository-format=docker \
  --location=us-central1

# List images
gcloud artifacts docker images list us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME
```

### Cloud Build
```bash
# List builds
gcloud builds list --limit=10

# Describe build
gcloud builds describe BUILD_ID

# View logs
gcloud builds log BUILD_ID
```

### Cloud Functions
```bash
# List functions
gcloud functions list

# Describe function
gcloud functions describe FUNCTION_NAME --region=us-central1

# View logs
gcloud functions logs read FUNCTION_NAME --region=us-central1
```

### Cloud Scheduler
```bash
# List jobs
gcloud scheduler jobs list

# Describe job
gcloud scheduler jobs describe JOB_NAME --location=us-central1

# Run job manually
gcloud scheduler jobs run JOB_NAME --location=us-central1
```

---

## Terraform Commands

### Basic Operations
```bash
# Navigate to provision directory
cd AutoMLOps/provision

# Initialize
terraform init

# Plan
terraform plan

# Apply
terraform apply

# Destroy
terraform destroy

# Show state
terraform show

# List resources
terraform state list
```

### State Management
```bash
# Check state bucket
gsutil ls gs://PROJECT_ID-bucket-tfstate/

# Remove lock
gsutil rm gs://PROJECT_ID-bucket-tfstate/default.tflock

# Reinitialize
terraform init -reconfigure
```

---

## Generated Directory Structure

```
AutoMLOps/
├── components/              # Component definitions
│   ├── component_base/      # Base Docker image
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── src/
│   └── component_name/      # Component specs
│       └── component.yaml
├── configs/                 # Configuration files
│   └── defaults.yaml
├── pipelines/              # Pipeline definitions
│   ├── pipeline.py
│   ├── pipeline_runner.py
│   └── requirements.txt
├── provision/              # Infrastructure code
│   ├── provision_resources.sh
│   └── provisioning_configs/
├── scripts/                # Helper scripts
│   ├── build_components.sh
│   ├── build_pipeline_spec.sh
│   ├── run_pipeline.sh
│   ├── run_all.sh
│   └── publish_to_topic.sh
├── services/               # Submission service
│   └── submission_service/
│       ├── Dockerfile
│       ├── main.py
│       └── requirements.txt
└── model_monitoring/       # Monitoring code
    ├── monitor.py
    └── requirements.txt
```

---

## Common Patterns

### BigQuery to GCS
```python
@AutoMLOps.component
def bq_to_gcs(bq_table: str, output_path: str, project_id: str):
    """Export BigQuery table to GCS."""
    from google.cloud import bigquery
    
    client = bigquery.Client(project=project_id)
    df = client.query(f"SELECT * FROM {bq_table}").to_dataframe()
    df.to_csv(output_path, index=False)
```

### Train Model
```python
@AutoMLOps.component
def train_model(data_path: str, model_path: str):
    """Train ML model."""
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, model_path)
```

### Deploy Model
```python
@AutoMLOps.component
def deploy_model(model_path: str, endpoint_name: str, project_id: str, region: str):
    """Deploy model to Vertex AI endpoint."""
    from google.cloud import aiplatform
    
    aiplatform.init(project=project_id, location=region)
    
    model = aiplatform.Model.upload(
        display_name=endpoint_name,
        artifact_uri=model_path
    )
    
    endpoint = model.deploy(machine_type='n1-standard-4')
```

---

## Scheduling Patterns

### Cron Format
```python
# Every hour
schedule_pattern='0 * * * *'

# Every 12 hours
schedule_pattern='0 */12 * * *'

# Daily at 2 AM
schedule_pattern='0 2 * * *'

# Weekly on Monday at 9 AM
schedule_pattern='0 9 * * 1'

# Monthly on 1st at midnight
schedule_pattern='0 0 1 * *'
```

---

## GPU Training

### GPU Configuration
```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    base_image='us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-11.py310:latest',
    custom_training_job_specs=[{
        'component_spec': 'train_model',
        'display_name': 'gpu-training',
        'machine_type': 'a2-highgpu-1g',
        'accelerator_type': 'NVIDIA_TESLA_A100',
        'accelerator_count': 1
    }]
)
```

### Available GPU Types
- `NVIDIA_TESLA_K80`
- `NVIDIA_TESLA_P4`
- `NVIDIA_TESLA_P100`
- `NVIDIA_TESLA_V100`
- `NVIDIA_TESLA_T4`
- `NVIDIA_TESLA_A100`

---

## GitHub Actions Integration

### Setup
```python
AutoMLOps.generate(
    project_id=PROJECT_ID,
    pipeline_params=pipeline_params,
    use_ci=True,
    deployment_framework='github-actions',
    project_number='123456789',
    source_repo_type='github',
    source_repo_name='username/repo-name',
    workload_identity_pool='projects/123/locations/global/workloadIdentityPools/pool',
    workload_identity_provider='projects/123/locations/global/workloadIdentityPools/pool/providers/provider',
    workload_identity_service_account='sa@project.iam.gserviceaccount.com'
)
```

---

## Monitoring Configuration

### Drift Detection
```python
drift_thresholds = {
    'feature_1': 0.05,  # 5% threshold
    'feature_2': 0.10,  # 10% threshold
    'feature_3': 0.03   # 3% threshold
}
```

### Skew Detection
```python
skew_thresholds = {
    'feature_1': 0.05,
    'feature_2': 0.10
}

training_dataset = 'gs://my-bucket/training_data.csv'
```

### Auto-Retraining
```python
auto_retraining_params = {
    'bq_table': 'project.dataset.table',
    'model_path': 'gs://bucket/retrained_model',
    'data_path': 'gs://bucket/new_data'
}
```

---

## Troubleshooting

### Check Generated Files
```bash
ls -la AutoMLOps/
tree AutoMLOps/
```

### View Logs
```bash
# Cloud Build logs
gcloud builds log BUILD_ID

# Cloud Functions logs
gcloud functions logs read FUNCTION_NAME

# Pipeline logs (in Vertex AI Console)
# https://console.cloud.google.com/vertex-ai/pipelines
```

### Verify Resources
```bash
# Check Artifact Registry
gcloud artifacts repositories list

# Check Cloud Storage
gsutil ls

# Check Cloud Functions
gcloud functions list

# Check Cloud Scheduler
gcloud scheduler jobs list
```

### Common Issues

**Import Error**:
```bash
pip install google-cloud-automlops
```

**Permission Denied**:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:EMAIL" \
  --role="roles/aiplatform.admin"
```

**API Not Enabled**:
```bash
gcloud services enable SERVICE_NAME.googleapis.com
```

**Terraform State Lock**:
```bash
gsutil rm gs://PROJECT_ID-bucket-tfstate/default.tflock
cd AutoMLOps/provision
terraform init -reconfigure
```

---

## Environment Variables

```bash
# Set in .env file
PROJECT_ID=my-project
PROJECT_NUMBER=123456789
REGION=us-central1
BUCKET_NAME=my-bucket
ARTIFACT_REGISTRY=my-repo
SERVICE_ACCOUNT=vertex-pipelines@project.iam.gserviceaccount.com
```

```python
# Load in Python
from dotenv import load_dotenv
import os

load_dotenv()
PROJECT_ID = os.getenv('PROJECT_ID')
```

---

## Useful Links

- [AutoMLOps GitHub](https://github.com/GoogleCloudPlatform/automlops)
- [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines)
- [KFP Documentation](https://www.kubeflow.org/docs/components/pipelines/)
- [Vertex AI Console](https://console.cloud.google.com/vertex-ai)

---

**Keep this handy while building MLOps pipelines! 🚀**
