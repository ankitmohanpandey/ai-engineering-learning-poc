# Compute Services Use Cases

## 🎯 Real-World Applications and Examples

### 1. Web Application Hosting

#### Scenario: E-commerce Platform
**Services Used**: Compute Engine + Cloud Load Balancer + Cloud SQL

**Architecture**:
```
Internet → Cloud Load Balancer → Compute Engine Instances (Web Servers)
                                      ↓
                              Cloud SQL (Database)
```

**Implementation**:
```bash
# Create instance group for web servers
gcloud compute instance-groups managed create web-servers \
  --zone=us-central1-a \
  --size=3 \
  --template=web-server-template

# Create load balancer
gcloud compute forwarding-rules create web-lb \
  --global \
  --load-balancing-scheme=EXTERNAL \
  --ports=80 \
  --target-pool=web-pool
```

**Benefits**:
- High availability with multiple instances
- Automatic scaling based on traffic
- Managed database with automatic backups
- Global load balancing for better performance

### 2. Microservices Architecture

#### Scenario: Social Media Application
**Services Used**: GKE + Cloud Run + Cloud Functions

**Architecture**:
```
User → API Gateway → Cloud Run (User Service)
                     → GKE (Post Service)
                     → Cloud Functions (Notification Service)
```

**Implementation**:
```yaml
# Kubernetes deployment for post service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: post-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: post-service
  template:
    metadata:
      labels:
        app: post-service
    spec:
      containers:
      - name: post-service
        image: gcr.io/project/post-service:latest
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
```

**Benefits**:
- Independent scaling of services
- Technology diversity (different runtimes)
- Fault isolation
- Faster deployment cycles

### 3. Batch Processing

#### Scenario: Data Analytics Pipeline
**Services Used**: Compute Engine + Cloud Storage + Cloud Functions

**Architecture**:
```
Cloud Storage (Raw Data) → Cloud Function (Trigger) → Compute Engine (Processing)
                                                              ↓
                                                      Cloud Storage (Processed Data)
```

**Implementation**:
```python
# Cloud Function to trigger processing
import functions_framework
from google.cloud import compute_v1

@functions_framework.cloud_event
def process_data(cloud_event):
    data = cloud_event.data
    file_name = data['name']
    bucket_name = data['bucket']
    
    # Start processing VM
    compute_client = compute_v1.InstancesClient()
    
    instance = compute_v1.Instance()
    instance.name = f"processor-{file_name.replace('/', '-')}"
    instance.machine_type = "zones/us-central1-a/machineTypes/e2-medium"
    
    # Configure instance with startup script
    instance.metadata = {
        "items": [
            {
                "key": "startup-script",
                "value": f"""
                gsutil cp gs://{bucket_name}/{file_name} /tmp/input.csv
                python3 /app/process.py /tmp/input.csv /tmp/output.csv
                gsutil cp /tmp/output.csv gs://{bucket_name}/processed/{file_name}
                gcloud compute instances delete {instance.name} --zone=us-central1-a
                """
            }
        ]
    }
    
    # Create instance
    operation = compute_client.insert(
        project="your-project",
        zone="us-central1-a",
        instance_resource=instance
    )
    
    return f"Started processing for {file_name}"
```

**Benefits**:
- Cost-effective (pay only when processing)
- Scalable for large datasets
- Event-driven architecture
- Automatic cleanup

### 4. Development and Testing Environments

#### Scenario: CI/CD Pipeline
**Services Used**: Cloud Build + Compute Engine + GKE

**Architecture**:
```
Git Push → Cloud Build → Docker Build → Deploy to GKE (Staging)
                                      ↓
                              Automated Tests
                                      ↓
                              Deploy to Production
```

**Implementation**:
```yaml
# cloudbuild.yaml
steps:
  # Build Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-app:$BUILD_ID', '.']
  
  # Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/my-app:$BUILD_ID']
  
  # Deploy to staging
  - name: 'gcr.io/cloud-builders/kubectl'
    args:
      - 'set'
      - 'image'
      - 'deployment/my-app'
      - 'my-app=gcr.io/$PROJECT_ID/my-app:$BUILD_ID'
    env:
      - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'
      - 'CLOUDSDK_CONTAINER_CLUSTER=staging-cluster'
  
  # Run tests
  - name: 'gcr.io/cloud-builders/curl'
    args:
      - '-f'
      - 'http://staging.example.com/health'
  
  # Deploy to production (manual approval)
  - name: 'gcr.io/cloud-builders/kubectl'
    args:
      - 'set'
      - 'image'
      - 'deployment/my-app'
      - 'my-app=gcr.io/$PROJECT_ID/my-app:$BUILD_ID'
    env:
      - 'CLOUDSDK_COMPUTE_ZONE=us-central1-a'
      - 'CLOUDSDK_CONTAINER_CLUSTER=prod-cluster'
```

**Benefits**:
- Automated testing and deployment
- Consistent environments
- Fast feedback loops
- Rollback capabilities

### 5. IoT Data Processing

#### Scenario: Smart Home Analytics
**Services Used**: Cloud Functions + Cloud Run + BigQuery

**Architecture**:
```
IoT Devices → Pub/Sub → Cloud Functions (Data Validation)
                              ↓
                        Cloud Run (Processing)
                              ↓
                        BigQuery (Analytics)
```

**Implementation**:
```python
# Cloud Function for data validation
import functions_framework
import json
from google.cloud import pubsub_v1

@functions_framework.cloud_event
def validate_iot_data(cloud_event):
    data = cloud_event.data
    device_id = data.get('device_id')
    sensor_data = data.get('sensor_data')
    
    # Validate data
    if not device_id or not sensor_data:
        print("Invalid data format")
        return
    
    # Publish to processing topic
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('your-project', 'process-iot-data')
    
    future = publisher.publish(topic_path, json.dumps(data).encode())
    return future.result()
```

```python
# Cloud Run service for processing
import os
from flask import Flask, request
from google.cloud import bigquery

app = Flask(__name__)
bigquery_client = bigquery.Client()

@app.route('/', methods=['POST'])
def process_iot_data():
    data = request.get_json()
    device_id = data['device_id']
    sensor_data = data['sensor_data']
    
    # Process and aggregate data
    processed_data = {
        'device_id': device_id,
        'timestamp': sensor_data['timestamp'],
        'temperature': sensor_data['temperature'],
        'humidity': sensor_data['humidity'],
        'processed_at': bigquery.timestamp()
    }
    
    # Insert into BigQuery
    table_id = 'your-project.iot_dataset.sensor_data'
    errors = bigquery_client.insert_rows_json(table_id, [processed_data])
    
    if errors:
        return f"Errors: {errors}", 500
    
    return "Data processed successfully"
```

**Benefits**:
- Real-time data processing
- Scalable for millions of devices
- Serverless architecture
- Rich analytics capabilities

### 6. Gaming Backend

#### Scenario: Multiplayer Game Server
**Services Used**: Compute Engine + Cloud Load Balancer + Memorystore

**Architecture**:
```
Players → Cloud Load Balancer → Game Servers (Compute Engine)
                              ↓
                      Memorystore (Redis Cache)
```

**Implementation**:
```python
# Game server using Flask
from flask import Flask, jsonify
import redis
import random

app = Flask(__name__)
redis_client = redis.from_url('redis://10.0.0.5:6379')

@app.route('/game/join')
def join_game():
    player_id = request.args.get('player_id')
    
    # Find available game session
    game_session = find_or_create_game_session()
    
    # Add player to session
    redis_client.sadd(f'game:{game_session}:players', player_id)
    
    return jsonify({
        'session_id': game_session,
        'players': list(redis_client.smembers(f'game:{game_session}:players'))
    })

def find_or_create_game_session():
    # Look for session with available slots
    for session_id in range(100):
        player_count = redis_client.scard(f'game:{session_id}:players')
        if player_count < 4:  # Max 4 players per game
            return session_id
    
    # Create new session
    new_session_id = random.randint(1000, 9999)
    return new_session_id
```

**Benefits**:
- Low latency with Redis cache
- Auto-scaling based on player count
- High availability
- Global distribution

### 7. Machine Learning Inference

#### Scenario: Image Recognition Service
**Services Used**: Cloud Run + Vertex AI + Cloud Storage

**Architecture**:
```
Client → Cloud Run (API) → Vertex AI (Model Prediction)
                              ↓
                        Cloud Storage (Images)
```

**Implementation**:
```python
# Cloud Run inference service
import functions_framework
from google.cloud import aiplatform
from google.cloud import storage
import base64
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get image from request
    image_data = request.files['image'].read()
    
    # Upload to Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('model-inputs')
    blob = bucket.blob(f'images/{uuid.uuid4()}.jpg')
    blob.upload_from_string(image_data, content_type='image/jpeg')
    
    # Make prediction
    aiplatform.init(project='your-project', location='us-central1')
    model = aiplatform.Model('projects/your-project/locations/us-central1/models/your-model-id')
    
    endpoint = model.deploy(machine_type='n1-standard-4')
    prediction = endpoint.predict(instances=[{'image': blob.public_url}])
    
    return jsonify({
        'prediction': prediction.predictions[0],
        'confidence': max(prediction.predictions[0])
    })
```

**Benefits**:
- Scalable inference
- Cost-effective (pay per request)
- Easy model updates
- High availability

## 📊 Performance Considerations

### Compute Engine
- **Machine Types**: Choose based on workload (CPU vs Memory optimized)
- **Preemptible VMs**: Up to 80% cost savings for fault-tolerant workloads
- **Custom Images**: Pre-configure instances for faster deployment

### GKE
- **Node Pools**: Separate workloads by node pools
- **Autoscaling**: Configure horizontal pod autoscaling
- **Resource Limits**: Set proper requests and limits

### Cloud Run
- **Concurrency**: Configure based on your application
- **Memory/CPU**: Optimize based on profiling
- **Min/Max Instances**: Control scaling behavior

## 💰 Cost Optimization

### General Tips
1. **Use sustained use discounts** for long-running workloads
2. **Leverage preemptible VMs** for batch processing
3. **Implement autoscaling** to match demand
4. **Use committed use discounts** for predictable workloads
5. **Monitor and optimize** resource utilization

### Service-Specific Optimization
- **Compute Engine**: Use right-sizing and machine type recommendations
- **GKE**: Use node auto-provisioning and cluster autoscaling
- **Cloud Run**: Optimize cold start times and concurrency settings
- **App Engine**: Use instance classes and automatic scaling

---

*For quick commands, see [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)*
*For setup instructions, see [SETUP.md](./SETUP.md)*
