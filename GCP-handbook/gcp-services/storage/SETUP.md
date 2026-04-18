# Storage Services Setup Guide

## 🚀 Prerequisites

1. **Google Cloud Account**: Create account at [cloud.google.com](https://cloud.google.com)
2. **Enable Billing**: Add payment method to your account
3. **Install Google Cloud SDK**: Download from [cloud.google.com/sdk](https://cloud.google.com/sdk/docs/install)
4. **Install Required Tools**: Based on services you plan to use

## 📥 Initial Setup

### 1. Install Google Cloud SDK and Tools

#### macOS
```bash
# Install Google Cloud SDK
brew install google-cloud-sdk

# Install additional tools
brew install mysql-client  # For Cloud SQL
pip install google-cloud-firestore  # For Firestore
pip install google-cloud-bigtable  # For Bigtable
pip install google-cloud-spanner  # For Spanner

# Initialize gcloud
gcloud init
```

#### Linux
```bash
# Download and install Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Install Python packages
pip install google-cloud-firestore google-cloud-bigtable google-cloud-spanner

# Initialize gcloud
gcloud init
```

### 2. Authenticate and Configure
```bash
# Login to your Google Account
gcloud auth login

# Set up application default credentials
gcloud auth application-default login

# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Set default region
gcloud config set compute/region us-central1
```

## 🪣 Cloud Storage Setup

### 1. Enable API
```bash
gcloud services enable storage.googleapis.com
gcloud services enable storage-component.googleapis.com
```

### 2. Install gsutil (Included with Cloud SDK)
```bash
# Verify gsutil installation
gsutil version

# Configure gsutil
gsutil config
```

### 3. Create Your First Bucket
```bash
# Create bucket (must be globally unique)
gsutil mb gs://your-unique-bucket-name-$(date +%s)

# Verify bucket creation
gsutil ls
```

### 4. Configure Bucket Settings
```bash
# Set storage class
gsutil storage buckets update gs://your-bucket \
  --storage-class=STANDARD

# Enable versioning
gsutil versioning set on gs://your-bucket

# Create lifecycle configuration
cat > lifecycle.json << EOF
{
  "rule": [
    {
      "action": {"type": "SetStorageClass", "storage_class": "NEARLINE"},
      "condition": {"age": 30}
    },
    {
      "action": {"type": "Delete"},
      "condition": {"age": 365}
    }
  ]
}
EOF

# Apply lifecycle rules
gsutil lifecycle set lifecycle.json gs://your-bucket
```

### 5. Test Upload and Download
```bash
# Create test file
echo "Hello, Cloud Storage!" > test.txt

# Upload file
gsutil cp test.txt gs://your-bucket/

# List contents
gsutil ls gs://your-bucket/

# Download file
gsutil cp gs://your-bucket/test.txt downloaded-test.txt

# Verify content
cat downloaded-test.txt
```

## 🗄️ Cloud SQL Setup

### 1. Enable APIs
```bash
gcloud services enable sqladmin.googleapis.com
gcloud services enable sql-component.googleapis.com
```

### 2. Create Service Account
```bash
# Create service account
gcloud iam service-accounts create cloudsql-admin \
  --description="Service account for Cloud SQL administration" \
  --display-name="Cloud SQL Admin"

# Grant permissions
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:cloudsql-admin@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudsql.admin"

# Download service account key
gcloud iam service-accounts keys create ~/cloudsql-key.json \
  --iam-account=cloudsql-admin@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

### 3. Create MySQL Instance
```bash
# Create MySQL instance
gcloud sql instances create my-mysql-db \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-1 \
  --region=us-central1 \
  --storage-auto-increase \
  --storage-size=20GB \
  --backup-start-time=02:00 \
  --retained-backups-count=7 \
  --enable-bin-log \
  --assign-ip

# Wait for instance creation
gcloud sql instances list
```

### 4. Configure Database
```bash
# Set root password
gcloud sql users set-password root \
  --instance=my-mysql-db \
  --password=YOUR_ROOT_PASSWORD

# Create database
gcloud sql databases create myapp \
  --instance=my-mysql-db

# Create application user
gcloud sql users create myapp-user \
  --instance=my-mysql-db \
  --password=YOUR_APP_PASSWORD
```

### 5. Connect and Test
```bash
# Connect using Cloud SQL Proxy
# Download proxy
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy

# Start proxy
./cloud_sql_proxy -instances=YOUR_PROJECT_ID:us-central1:mysql-instance=my-mysql-db &

# Connect using mysql client
mysql -u myapp-user -p -h 127.0.0.1 myapp

# In MySQL, create test table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# Insert test data
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');

# Query data
SELECT * FROM users;
```

## 🔥 Firestore Setup

### 1. Enable API
```bash
gcloud services enable firestore.googleapis.com
gcloud services enable firebasestorage.googleapis.com
```

### 2. Create Firestore Database
```bash
# Create Firestore database
gcloud firestore databases create \
  --region=us-central1 \
  --type=firestore-native

# Verify database creation
gcloud firestore databases list
```

### 3. Install Python Client and Test
```python
# test_firestore.py
from google.cloud import firestore
import json

# Initialize client
db = firestore.Client()

# Create test data
test_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30,
    'preferences': {
        'theme': 'dark',
        'notifications': True
    }
}

# Add document
doc_ref = db.collection('users').document('user1')
doc_ref.set(test_data)
print("Document created successfully!")

# Read document
doc = doc_ref.get()
if doc.exists:
    print(f"Document data: {doc.to_dict()}")

# Query collection
users_ref = db.collection('users')
query = users_ref.where('age', '>=', 18).get()
print(f"Found {len(list(query))} users aged 18+")
```

```bash
# Run test
python test_firestore.py
```

### 4. Set Up Security Rules
```bash
# Create security rules file
cat > firestore.rules << EOF
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can read/write their own documents
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Public data is readable by everyone
    match /public/{document=**} {
      allow read: if true;
    }
    
    // Authenticated users can create documents
    match /{document=**} {
      allow create: if request.auth != null;
    }
  }
}
EOF

# Apply security rules
gcloud firestore rules update firestore.rules
```

## 📊 Cloud Bigtable Setup

### 1. Enable API
```bash
gcloud services enable bigtable.googleapis.com
gcloud services enable bigtableadmin.googleapis.com
```

### 2. Create Bigtable Instance
```bash
# Create instance
gcloud bigtable instances create my-bigtable-instance \
  --cluster-config=id=my-cluster,zone=us-central1-a,nodes=3 \
  --display-name="My Bigtable Instance"

# Verify instance creation
gcloud bigtable instances list
```

### 3. Create Table and Column Families
```bash
# Use cbt CLI
echo "project = your-project-id" > ~/.cbtrc
echo "instance = my-bigtable-instance" >> ~/.cbtrc

# Create table
cbt createtable sensor-data

# Create column families
cbt createfamily sensor-data cf-metrics
cbt createfamily sensor-data cf-metadata

# Verify table
cbt ls
```

### 4. Test with Python Client
```python
# test_bigtable.py
from google.cloud import bigtable
from google.cloud.bigtable.row_set import RowSet
import time

# Initialize client
client = bigtable.Client(project='your-project-id', admin=True)
instance = client.instance('my-bigtable-instance')
table = instance.table('sensor-data')

# Write test data
row_key = f'sensor1#{int(time.time())}'.encode()
row = table.direct_row(row_key)

# Add metrics
row.set_cell(
    column_family_id='cf-metrics',
    column='temperature'.encode(),
    value=b'23.5',
    timestamp=None
)

row.set_cell(
    column_family_id='cf-metrics',
    column='humidity'.encode(),
    value=b'65.2',
    timestamp=None
)

# Add metadata
row.set_cell(
    column_family_id='cf-metadata',
    column='location'.encode(),
    value=b'room1',
    timestamp=None
)

# Commit row
row.commit()
print("Data written to Bigtable!")

# Read data
row_data = table.read_row(row_key)
if row_data:
    for column_family, columns in row_data.cells.items():
        for column, cells in columns.items():
            for cell in cells:
                print(f"{column.decode()}: {cell.value.decode()}")
```

```bash
# Run test
python test_bigtable.py
```

## 🌐 Cloud Spanner Setup

### 1. Enable API
```bash
gcloud services enable spanner.googleapis.com
gcloud services enable spanneradmin.googleapis.com
```

### 2. Create Spanner Instance
```bash
# Create instance
gcloud spanner instances create my-spanner-instance \
  --config=regional-us-central1 \
  --nodes=1 \
  --description="My Spanner Instance"

# Create database
gcloud spanner databases create my-database \
  --instance=my-spanner-instance
```

### 3. Define Schema
```sql
-- schema.sql
CREATE TABLE users (
  id STRING(36) NOT NULL,
  name STRING(255) NOT NULL,
  email STRING(255) NOT NULL,
  created_at TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true),
) PRIMARY KEY (id);

CREATE TABLE posts (
  id STRING(36) NOT NULL,
  user_id STRING(36) NOT NULL,
  title STRING(500) NOT NULL,
  content STRING(MAX) NOT NULL,
  created_at TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true),
) PRIMARY KEY (id),
  INTERLEAVE IN PARENT users ON DELETE CASCADE;

CREATE INDEX posts_by_user ON posts (user_id, created_at DESC);
```

```bash
# Apply schema
gcloud spanner databases ddl update my-database \
  --instance=my-spanner-instance \
  --sql-file=schema.sql
```

### 4. Test with Python Client
```python
# test_spanner.py
from google.cloud import spanner
import uuid

# Initialize client
client = spanner.Client()
instance = client.instance('my-spanner-instance')
database = instance.database('my-database')

# Insert test data
with database.batch() as batch:
    # Insert user
    user_id = str(uuid.uuid4())
    batch.insert(
        table='users',
        columns=('id', 'name', 'email', 'created_at'),
        values=[(user_id, 'John Doe', 'john@example.com', spanner.COMMIT_TIMESTAMP)]
    )
    
    # Insert post
    post_id = str(uuid.uuid4())
    batch.insert(
        table='posts',
        columns=('id', 'user_id', 'title', 'content', 'created_at'),
        values=[(post_id, user_id, 'My First Post', 'Hello, Spanner!', spanner.COMMIT_TIMESTAMP)]
    )

print("Data inserted successfully!")

# Query data
with database.snapshot() as snapshot:
    # Join query
    query = """
        SELECT u.name, p.title, p.created_at
        FROM users u
        JOIN posts p ON u.id = p.user_id
        ORDER BY p.created_at DESC
        LIMIT 10
    """
    
    results = snapshot.execute_sql(query)
    for row in results:
        print(f"{row[0]} wrote: {row[1]} at {row[2]}")
```

```bash
# Run test
python test_spanner.py
```

## 🔧 Development Tools Setup

### 1. Cloud Console Access
- Navigate to [console.cloud.google.com](https://console.cloud.google.com)
- Access all storage services through web interface
- Use built-in query editors and management tools

### 2. IDE Integration
```bash
# Install Cloud Tools for IntelliJ
# File > Settings > Plugins > Google Cloud

# Install Cloud Code for VS Code
# Extensions > Google Cloud Code
```

### 3. Local Development
```bash
# For Cloud SQL - Use Docker
docker run --name mysql-dev -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8.0

# For Bigtable - Use HBase Docker
docker run --name hbase-dev -p 2181:2181 -p 16000:16000 -d harisekhon/hbase

# For Spanner - Use emulator
gcloud emulators spanner start --host-port=localhost:9010
```

## 📊 Monitoring and Logging Setup

### 1. Enable Monitoring APIs
```bash
gcloud services enable monitoring.googleapis.com
gcloud services enable logging.googleapis.com
```

### 2. Set Up Dashboards
```bash
# Use Cloud Console > Monitoring > Dashboards
# Create custom dashboards for:
# - Storage usage
# - Query performance
# - Error rates
# - Latency metrics
```

### 3. Configure Alerts
```bash
# Use Cloud Console > Monitoring > Alerting
# Set up alerts for:
# - High storage usage (>80%)
# - Database connection errors
# - Query timeout rates
# - Backup failures
```

## 🧹 Cleanup Commands

```bash
# Delete Cloud Storage bucket
gsutil rm -r gs://your-bucket

# Delete Cloud SQL instance
gcloud sql instances delete my-mysql-db

# Delete Firestore database
gcloud firestore databases delete --region=us-central1

# Delete Bigtable instance
gcloud bigtable instances delete my-bigtable-instance

# Delete Spanner instance
gcloud spanner instances delete my-spanner-instance
```

## 🆘 Troubleshooting

### Common Issues
1. **Permission denied**: Check IAM roles and service account permissions
2. **API not enabled**: Enable required APIs
3. **Quota exceeded**: Request quota increase
4. **Connection timeouts**: Check firewall rules and network configuration

### Debug Commands
```bash
# Check API status
gcloud services list --enabled

# Verify permissions
gcloud projects get-iam-policy YOUR_PROJECT_ID

# Test connectivity
gsutil ls gs://your-bucket
gcloud sql connect my-mysql-db --user=root
```

### Performance Optimization
1. **Cloud Storage**: Use appropriate storage classes and lifecycle policies
2. **Cloud SQL**: Optimize queries, use read replicas, enable caching
3. **Firestore**: Use compound queries, avoid large documents
4. **Bigtable**: Design row keys for even distribution, use appropriate column families
5. **Spanner**: Use proper indexing, optimize schema design

---

*For quick commands, see [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)*
*For service overview, see [README.md](./README.md)*
