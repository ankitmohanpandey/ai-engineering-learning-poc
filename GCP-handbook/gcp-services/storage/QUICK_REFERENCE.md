# Storage Services Quick Reference

## 🗄️ Common Commands

### Cloud Storage

#### Bucket Management
```bash
# Create bucket
gsutil mb gs://my-unique-bucket-name

# List buckets
gsutil ls

# List bucket contents
gsutil ls gs://my-bucket/

# Copy files
gsutil cp file.txt gs://my-bucket/
gsutil cp gs://my-bucket/file.txt ./local-file.txt

# Sync directories
gsutil rsync -r ./local-dir gs://my-bucket/remote-dir

# Delete bucket
gsutil rm -r gs://my-bucket
```

#### Bucket Configuration
```bash
# Set storage class
gsutil storage buckets update gs://my-bucket --storage-class=NEARLINE

# Enable versioning
gsutil versioning set on gs://my-bucket

# Set lifecycle rule
cat > lifecycle.json << EOF
{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 30}
    }
  ]
}
EOF
gsutil lifecycle set lifecycle.json gs://my-bucket

# Make bucket public
gsutil iam ch allUsers:objectViewer gs://my-bucket
```

#### Signed URLs
```bash
# Generate signed URL for upload
gsutil signurl -d 10m service-account.json gs://my-bucket/file.txt

# Generate signed URL for download
gsutil signurl -m GET -d 1h service-account.json gs://my-bucket/file.txt
```

### Cloud SQL

#### Instance Management
```bash
# Create MySQL instance
gcloud sql instances create my-mysql-instance \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-1 \
  --region=us-central1 \
  --storage-auto-increase \
  --backup-start-time=02:00

# Create PostgreSQL instance
gcloud sql instances create my-postgres-instance \
  --database-version=POSTGRES_14 \
  --tier=db-n1-standard-1 \
  --region=us-central1

# List instances
gcloud sql instances list

# Connect to instance
gcloud sql connect my-mysql-instance --user=root

# Delete instance
gcloud sql instances delete my-mysql-instance
```

#### Database Management
```bash
# Create database
gcloud sql databases create my-database --instance=my-mysql-instance

# List databases
gcloud sql databases list --instance=my-mysql-instance

# Create user
gcloud sql users create my-user --instance=my-mysql-instance --password=mypassword

# Export database
gcloud sql export sql my-mysql-instance gs://my-bucket/backup.sql \
  --database=my-database

# Import database
gcloud sql import sql my-mysql-instance gs://my-bucket/backup.sql \
  --database=my-database
```

#### Backup and Restore
```bash
# Create backup
gcloud sql backups create --instance=my-mysql-instance

# List backups
gcloud sql backups list --instance=my-mysql-instance

# Restore from backup
gcloud sql backups restore BACKUP_ID --instance=my-mysql-instance
```

### Firestore

#### Database Management
```bash
# Create Firestore database
gcloud firestore databases create --region=us-central1

# List databases
gcloud firestore databases list

# Import data
gcloud firestore import gs://my-bucket/firestore-export/

# Export data
gcloud firestore export gs://my-bucket/firestore-export/ \
  --collection-ids=users,products
```

#### Python Client Usage
```python
from google.cloud import firestore

# Initialize client
db = firestore.Client()

# Add document
doc_ref = db.collection('users').document('user1')
doc_ref.set({
    'name': 'John Doe',
    'email': 'john@example.com',
    'created_at': firestore.SERVER_TIMESTAMP
})

# Get document
doc = doc_ref.get()
if doc.exists:
    print(doc.to_dict())

# Query collection
users_ref = db.collection('users')
query = users_ref.where('age', '>=', 18).get()
for doc in query:
    print(doc.to_dict())

# Update document
doc_ref.update({'email': 'newemail@example.com'})

# Delete document
doc_ref.delete()
```

### Cloud Bigtable

#### Instance Management
```bash
# Create Bigtable instance
gcloud bigtable instances create my-bigtable-instance \
  --cluster-config=id=my-cluster,zone=us-central1-a,nodes=3 \
  --display-name="My Bigtable Instance"

# List instances
gcloud bigtable instances list

# Create table
cbt -instance=my-bigtable-instance createtable my-table

# List tables
cbt -instance=my-bigtable-instance ls

# Delete instance
gcloud bigtable instances delete my-bigtable-instance
```

#### Python Client Usage
```python
from google.cloud import bigtable

# Initialize client
client = bigtable.Client(project='my-project', admin=True)
instance = client.instance('my-bigtable-instance')
table = instance.table('my-table')

# Create column family
column_family = table.column_family('cf1')
column_family.create()

# Write data
row_key = 'row1'.encode()
row = table.direct_row(row_key)
row.set_cell(
    column_family_id='cf1',
    column='column1'.encode(),
    value='value1'.encode(),
    timestamp=None
)
row.commit()

# Read data
row_data = table.read_row(row_key)
for column_family, columns in row_data.cells.items():
    for column, cells in columns.items():
        for cell in cells:
            print(f"Value: {cell.value.decode()}")
```

### Cloud Spanner

#### Instance Management
```bash
# Create Spanner instance
gcloud spanner instances create my-spanner-instance \
  --config=regional-us-central1 \
  --nodes=1 \
  --description="My Spanner Instance"

# Create database
gcloud spanner databases create my-database \
  --instance=my-spanner-instance

# List instances
gcloud spanner instances list

# Delete instance
gcloud spanner instances delete my-spanner-instance
```

#### SQL Operations
```bash
# Execute DDL
gcloud spanner databases ddl update my-database \
  --instance=my-spanner-instance \
  --sql="CREATE TABLE users (id STRING(36) NOT NULL, name STRING(255)) PRIMARY KEY (id)"

# Execute query
gcloud spanner databases execute-sql my-database \
  --instance=my-spanner-instance \
  --sql="SELECT * FROM users"
```

#### Python Client Usage
```python
from google.cloud import spanner

# Initialize client
client = spanner.Client()
instance = client.instance('my-spanner-instance')
database = instance.database('my-database')

# Execute query
with database.snapshot() as snapshot:
    results = snapshot.execute_sql('SELECT * FROM users')
    for row in results:
        print(row)

# Insert data
with database.batch() as batch:
    batch.insert(
        table='users',
        columns=('id', 'name'),
        values=[
            ('user1', 'John Doe'),
            ('user2', 'Jane Smith')
        ]
    )
```

## 📊 Storage Classes

### Cloud Storage Classes
| Class | Use Case | Min Storage Duration | Availability |
|-------|----------|---------------------|--------------|
| Standard | Frequently accessed data | None | 99.9% |
| Nearline | Accessed < 1/month | 30 days | 99.9% |
| Coldline | Accessed < 1/quarter | 90 days | 99.9% |
| Archive | Accessed < 1/year | 365 days | 99.9% |

### Cloud SQL Tiers
| Tier | vCPUs | Memory | Storage | Use Case |
|------|-------|--------|---------|----------|
| db-g1-small | 1 | 0.6 GB | 10 GB - 3 TB | Development |
| db-n1-standard-1 | 1 | 3.75 GB | 10 GB - 3 TB | Small production |
| db-n1-standard-2 | 2 | 7.5 GB | 10 GB - 3 TB | Medium production |
| db-n1-standard-4 | 4 | 15 GB | 10 GB - 3 TB | Large production |

## 🔧 Configuration Files

### Cloud Storage Lifecycle
```json
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
```

### Cloud SQL Backup Configuration
```yaml
# backup-config.yaml
backupConfiguration:
  enabled: true
  startTime: "02:00"
  location: us-central1
  pointInTimeRecoveryEnabled: true
  retainedBackupsCount: 30
```

### Firestore Security Rules
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    match /public/{document=**} {
      allow read: if true;
    }
  }
}
```

## 🔍 Monitoring Commands

```bash
# Check Cloud Storage usage
gsutil du -sh gs://my-bucket

# Monitor Cloud SQL operations
gcloud sql operations list --instance=my-mysql-instance

# Check Firestore usage
gcloud firestore databases list --format="value(name,usage)"

# Monitor Bigtable performance
cbt -instance=my-bigtable-instance read my-table

# Check Spanner database stats
gcloud spanner databases execute-sql my-database \
  --instance=my-spanner-instance \
  --sql="SELECT * FROM INFORMATION_SCHEMA.DATABASES"
```

## 🏷️ Pricing Examples

### Cloud Storage (US)
- **Standard**: $0.020 per GB/month
- **Nearline**: $0.010 per GB/month + $0.01 per GB read
- **Coldline**: $0.004 per GB/month + $0.02 per GB read
- **Archive**: $0.0012 per GB/month + $0.05 per GB read

### Cloud SQL (US)
- **db-n1-standard-1**: $52.27/month + storage costs
- **Storage**: $0.085 per GB/month
- **Backup storage**: $0.026 per GB/month

### Firestore (US)
- **Storage**: $0.18 per GB/month
- **Reads**: $0.06 per 100,000 documents
- **Writes**: $0.18 per 100,000 documents
- **Deletes**: $0.02 per 100,000 documents

## 📞 Support Commands

```bash
# Get help for gsutil
gsutil help

# Check gcloud SQL configuration
gcloud config list

# Verify permissions
gcloud projects get-iam-policy PROJECT_ID

# Test connectivity
gcloud sql connect my-mysql-instance --user=root
```

---

*For detailed setup instructions, see [SETUP.md](./SETUP.md)*
*For service overview, see [README.md](./README.md)*
