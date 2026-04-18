# Storage Services Use Cases

## 🎯 Real-World Applications and Examples

### 1. Media and Content Management Platform

#### Scenario: Video Streaming Service
**Services Used**: Cloud Storage + Cloud CDN + Cloud Functions

**Architecture**:
```
Upload → Cloud Function → Cloud Storage (Original)
                              ↓
                        Cloud Function (Transcoding)
                              ↓
                        Cloud Storage (Processed)
                              ↓
                        Cloud CDN → Users
```

**Implementation**:
```python
# Cloud Function for video processing
import functions_framework
from google.cloud import storage
import subprocess

@functions_framework.cloud_event
def process_video(cloud_event):
    data = cloud_event.data
    bucket_name = data['bucket']
    file_name = data['name']
    
    # Download video
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.download_to_filename('/tmp/input.mp4')
    
    # Transcode video (using FFmpeg)
    subprocess.run([
        'ffmpeg', '-i', '/tmp/input.mp4',
        '-vf', 'scale=1280:720',
        '-c:v', 'libx264',
        '-preset', 'medium',
        '/tmp/output_720p.mp4'
    ])
    
    # Upload processed video
    output_blob = bucket.blob(f'processed/{file_name}')
    output_blob.upload_from_filename('/tmp/output_720p.mp4')
    
    # Make public
    output_blob.make_public()
    
    return f"Video processed: {file_name}"
```

**Benefits**:
- Automatic video transcoding
- Global content delivery
- Scalable storage for media files
- Cost-effective with lifecycle management

### 2. E-commerce Platform Backend

#### Scenario: Online Shopping Platform
**Services Used**: Cloud SQL + Cloud Storage + Memorystore

**Architecture**:
```
Users → App Servers → Cloud SQL (Products, Orders)
                      ↓
                Cloud Storage (Product Images)
                      ↓
                Memorystore (Shopping Carts)
```

**Implementation**:
```python
# Product management with Cloud SQL
import sqlalchemy
from google.cloud import storage
from google.cloud import sql

class ProductManager:
    def __init__(self):
        self.engine = self.create_db_connection()
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket('product-images')
    
    def create_db_connection(self):
        # Cloud SQL connection
        db_user = 'app-user'
        db_pass = 'password'
        db_name = 'ecommerce'
        db_socket_dir = '/cloudsql'
        instance_connection_name = 'project:region:instance'
        
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{db_user}:{db_pass}@/'
            f'{db_name}?unix_socket={db_socket_dir}/{instance_connection_name}/mysql.sock'
        )
        return engine
    
    def add_product(self, name, description, price, image_file):
        # Upload image to Cloud Storage
        image_blob = self.bucket.blob(f'products/{image_file.filename}')
        image_blob.upload_from_file(image_file)
        image_url = image_blob.public_url
        
        # Save product to Cloud SQL
        with self.engine.connect() as conn:
            result = conn.execute(
                sqlalchemy.text(
                    "INSERT INTO products (name, description, price, image_url) "
                    "VALUES (:name, :description, :price, :image_url)"
                ),
                {
                    'name': name,
                    'description': description,
                    'price': price,
                    'image_url': image_url
                }
            )
            return result.lastrowid
    
    def get_products(self, limit=50):
        with self.engine.connect() as conn:
            result = conn.execute(
                sqlalchemy.text(
                    "SELECT * FROM products ORDER BY created_at DESC LIMIT :limit"
                ),
                {'limit': limit}
            )
            return [dict(row) for row in result]
```

**Benefits**:
- ACID transactions for order processing
- Scalable image storage
- Fast product searches with SQL queries
- Automatic backups and high availability

### 3. Real-time Analytics Dashboard

#### Scenario: IoT Monitoring System
**Services Used**: Bigtable + BigQuery + Dataflow

**Architecture**:
```
IoT Devices → Pub/Sub → Dataflow → Bigtable (Real-time)
                              ↓
                        BigQuery (Analytics)
                              ↓
                        Dashboard (Data Studio)
```

**Implementation**:
```python
# Dataflow pipeline for IoT data processing
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import bigtable
from google.cloud import bigquery

class ProcessIoTData(beam.DoFn):
    def process(self, element):
        # Parse IoT data
        device_id = element['device_id']
        timestamp = element['timestamp']
        metrics = element['metrics']
        
        # Transform for Bigtable
        row_key = f"{device_id}#{timestamp}"
        
        # Transform for BigQuery
        bq_row = {
            'device_id': device_id,
            'timestamp': timestamp,
            'temperature': metrics.get('temperature'),
            'humidity': metrics.get('humidity'),
            'pressure': metrics.get('pressure')
        }
        
        yield {
            'bigtable': {
                'row_key': row_key,
                'data': metrics
            },
            'bigquery': bq_row
        }

def run_pipeline():
    options = PipelineOptions()
    
    with beam.Pipeline(options=options) as p:
        (p
         | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription='projects/project/subscriptions/iot-data')
         | 'ParseJSON' >> beam.Map(lambda x: json.loads(x.decode('utf-8')))
         | 'ProcessData' >> beam.ParDo(ProcessIoTData())
         | 'WriteToBigtable' >> beam.io.WriteToBigTable(
             project_id='project',
             instance_id='iot-instance',
             table_id='sensor-data'
         )
         | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
             table='project:iot_dataset.sensor_data',
             schema='device_id:STRING, timestamp:TIMESTAMP, temperature:FLOAT, humidity:FLOAT, pressure:FLOAT',
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))
```

**Benefits**:
- Real-time data ingestion and processing
- Millisecond latency for recent data
- Long-term analytics with BigQuery
- Scalable to millions of IoT devices

### 4. Mobile Application Backend

#### Scenario: Social Media App
**Services Used**: Firestore + Cloud Storage + Cloud Functions

**Architecture**:
```
Mobile Apps → Firestore (User Data, Posts)
               ↓
         Cloud Storage (Media)
               ↓
         Cloud Functions (Processing)
```

**Implementation**:
```python
# Firestore data model for social media
from google.cloud import firestore
from google.cloud import storage

class SocialMediaBackend:
    def __init__(self):
        self.db = firestore.Client()
        self.storage = storage.Client()
        self.bucket = self.storage.bucket('social-media-content')
    
    def create_post(self, user_id, content, media_files=None):
        # Upload media files
        media_urls = []
        if media_files:
            for file in media_files:
                blob = self.bucket.blob(f'posts/{user_id}/{file.filename}')
                blob.upload_from_file(file)
                media_urls.append(blob.public_url)
        
        # Create post document
        post_data = {
            'user_id': user_id,
            'content': content,
            'media_urls': media_urls,
            'likes': 0,
            'comments': [],
            'created_at': firestore.SERVER_TIMESTAMP,
            'updated_at': firestore.SERVER_TIMESTAMP
        }
        
        # Add to Firestore
        doc_ref = self.db.collection('posts').document()
        doc_ref.set(post_data)
        
        # Update user's posts
        self.db.collection('users').document(user_id).update({
            'posts': firestore.ArrayUnion([doc_ref.id])
        })
        
        return doc_ref.id
    
    def get_feed(self, user_id, limit=20):
        # Get user's following list
        user_doc = self.db.collection('users').document(user_id).get()
        following = user_doc.to_dict().get('following', [])
        
        # Add user to following list
        following.append(user_id)
        
        # Query posts from followed users
        posts_ref = self.db.collection('posts')
        query = posts_ref.where('user_id', 'in', following).order_by('created_at', direction='DESCENDING').limit(limit)
        
        posts = []
        for doc in query.stream():
            post_data = doc.to_dict()
            post_data['post_id'] = doc.id
            
            # Get user info
            user_info = self.db.collection('users').document(post_data['user_id']).get().to_dict()
            post_data['user_info'] = {
                'name': user_info.get('name'),
                'avatar_url': user_info.get('avatar_url')
            }
            
            posts.append(post_data)
        
        return posts
    
    def like_post(self, user_id, post_id):
        # Add like to post
        post_ref = self.db.collection('posts').document(post_id)
        post_ref.update({
            'likes': firestore.Increment(1),
            'liked_by': firestore.ArrayUnion([user_id])
        })
        
        # Create notification
        notification_data = {
            'user_id': user_id,
            'post_id': post_id,
            'type': 'like',
            'created_at': firestore.SERVER_TIMESTAMP,
            'read': False
        }
        
        self.db.collection('notifications').add(notification_data)
```

**Benefits**:
- Real-time synchronization across devices
- Offline support for mobile clients
- Automatic scaling with user growth
- Rich query capabilities

### 5. Financial Trading Platform

#### Scenario: High-Frequency Trading System
**Services Used**: Cloud Spanner + Memorystore + Cloud Load Balancer

**Architecture**:
```
Trading Clients → Load Balancer → Trading Servers → Cloud Spanner
                                          ↓
                                    Memorystore (Cache)
                                          ↓
                                    Risk Engine (Cloud Functions)
```

**Implementation**:
```python
# Trading system with Cloud Spanner
from google.cloud import spanner
import redis
import uuid
from decimal import Decimal

class TradingEngine:
    def __init__(self):
        self.spanner_client = spanner.Client()
        self.database = self.spanner_client.instance('trading-instance').database('trading_db')
        self.redis_client = redis.from_url('redis://memorystore-ip:6379')
    
    def place_order(self, user_id, symbol, side, quantity, price, order_type='market'):
        # Generate order ID
        order_id = str(uuid.uuid4())
        
        # Validate user balance (check cache first)
        balance_key = f"balance:{user_id}"
        cached_balance = self.redis_client.get(balance_key)
        
        if not cached_balance:
            # Get from Spanner
            with self.database.snapshot() as snapshot:
                result = snapshot.execute_sql(
                    "SELECT balance FROM accounts WHERE user_id = @user_id",
                    params={'user_id': user_id}
                )
                balance = list(result)[0][0]
                self.redis_client.setex(balance_key, 60, str(balance))
        else:
            balance = Decimal(cached_balance.decode())
        
        # Calculate required amount
        required_amount = Decimal(quantity) * Decimal(price)
        
        if balance < required_amount:
            raise ValueError("Insufficient balance")
        
        # Create order in Spanner
        with self.database.batch() as batch:
            # Insert order
            batch.insert(
                table='orders',
                columns=('order_id', 'user_id', 'symbol', 'side', 'quantity', 'price', 'order_type', 'status', 'created_at'),
                values=[(order_id, user_id, symbol, side, quantity, price, order_type, 'pending', spanner.COMMIT_TIMESTAMP)]
            )
            
            # Update account balance
            batch.update(
                table='accounts',
                columns=('user_id', 'balance'),
                values=[(user_id, balance - required_amount)]
            )
        
        # Invalidate cache
        self.redis_client.delete(balance_key)
        
        # Trigger matching engine
        self.match_order(order_id)
        
        return order_id
    
    def match_order(self, order_id):
        # Get order details
        with self.database.snapshot() as snapshot:
            result = snapshot.execute_sql(
                "SELECT * FROM orders WHERE order_id = @order_id",
                params={'order_id': order_id}
            )
            order = dict(zip(['order_id', 'user_id', 'symbol', 'side', 'quantity', 'price', 'order_type', 'status', 'created_at'], list(result)[0]))
        
        # Find matching orders (simplified)
        with self.database.snapshot() as snapshot:
            result = snapshot.execute_sql(
                """
                SELECT order_id, price, quantity 
                FROM orders 
                WHERE symbol = @symbol AND side = @opposite_side AND status = 'pending'
                AND (side = 'buy' AND price <= @price OR side = 'sell' AND price >= @price)
                ORDER BY created_at ASC
                LIMIT 10
                """,
                params={
                    'symbol': order['symbol'],
                    'opposite_side': 'sell' if order['side'] == 'buy' else 'buy',
                    'price': order['price']
                }
            )
            
            for match_order in result:
                # Execute trade
                self.execute_trade(order_id, match_order[0], order['quantity'])
                break
    
    def execute_trade(self, buy_order_id, sell_order_id, quantity):
        trade_id = str(uuid.uuid4())
        
        with self.database.batch() as batch:
            # Insert trade record
            batch.insert(
                table='trades',
                columns=('trade_id', 'buy_order_id', 'sell_order_id', 'quantity', 'price', 'executed_at'),
                values=[(trade_id, buy_order_id, sell_order_id, quantity, 0, spanner.COMMIT_TIMESTAMP)]
            )
            
            # Update order statuses
            batch.update(
                table='orders',
                columns=('order_id', 'status'),
                values=[(buy_order_id, 'filled'), (sell_order_id, 'filled')]
            )
```

**Benefits**:
- Global consistency for financial data
- High availability with 99.999% SLA
- Horizontal scaling for high throughput
- ACID transactions for trading operations

### 6. Healthcare Data Platform

#### Scenario: Electronic Health Records (EHR)
**Services Used**: Cloud SQL + Cloud Storage + Cloud KMS

**Architecture**:
```
Healthcare Providers → App Servers → Cloud SQL (Patient Records)
                                   ↓
                             Cloud Storage (Medical Images)
                                   ↓
                             Cloud KMS (Encryption)
```

**Implementation**:
```python
# HIPAA-compliant EHR system
from google.cloud import storage
from google.cloud import kms_v1
from google.cloud import sql
import cryptography.fernet
import base64

class EHRSystem:
    def __init__(self):
        self.storage_client = storage.Client()
        self.kms_client = kms_v1.KeyManagementServiceClient()
        self.bucket = self.storage_client.bucket('ehr-secure-data')
        self.key_name = 'projects/project/locations/global/keyRings/ehr/cryptoKeys/ehr-data'
        
    def encrypt_data(self, data):
        # Encrypt with Cloud KMS
        response = self.kms_client.encrypt(
            request={'name': self.key_name, 'plaintext': data.encode()}
        )
        return response.ciphertext
    
    def decrypt_data(self, ciphertext):
        # Decrypt with Cloud KMS
        response = self.kms_client.decrypt(
            request={'name': self.key_name, 'ciphertext': ciphertext}
        )
        return response.plaintext.decode()
    
    def store_medical_record(self, patient_id, record_data, medical_images=None):
        # Encrypt sensitive data
        encrypted_data = self.encrypt_data(str(record_data))
        
        # Store in Cloud SQL (metadata)
        with self.db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO medical_records 
                (patient_id, record_type, encrypted_data, created_at) 
                VALUES (%s, %s, %s, NOW())
                """,
                (patient_id, 'clinical', encrypted_data)
            )
            record_id = cursor.lastrowid
        
        # Store medical images in Cloud Storage
        if medical_images:
            for image_name, image_data in medical_images.items():
                # Encrypt image
                encrypted_image = self.encrypt_data(image_data)
                
                # Store encrypted image
                blob = self.bucket.blob(f'patients/{patient_id}/records/{record_id}/{image_name}')
                blob.upload_from_string(encrypted_image)
        
        return record_id
    
    def retrieve_medical_record(self, patient_id, record_id):
        # Get record metadata from Cloud SQL
        with self.db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT encrypted_data, record_type, created_at 
                FROM medical_records 
                WHERE patient_id = %s AND id = %s
                """,
                (patient_id, record_id)
            )
            result = cursor.fetchone()
        
        if not result:
            return None
        
        # Decrypt data
        decrypted_data = self.decrypt_data(result[0])
        
        # Get medical images
        image_blobs = self.bucket.list_blobs(prefix=f'patients/{patient_id}/records/{record_id}/')
        images = {}
        for blob in image_blobs:
            encrypted_image = blob.download_as_bytes()
            decrypted_image = self.decrypt_data(encrypted_image)
            images[blob.name.split('/')[-1]] = decrypted_image
        
        return {
            'data': decrypted_data,
            'type': result[1],
            'created_at': result[2],
            'images': images
        }
```

**Benefits**:
- HIPAA compliance with encryption
- Secure storage of medical images
- Audit trails and access controls
- Disaster recovery capabilities

### 7. Gaming Leaderboard System

#### Scenario: Multiplayer Game Rankings
**Services Used**: Firestore + Cloud Functions + Cloud Memorystore

**Architecture**:
```
Game Clients → Firestore (Player Data) → Cloud Functions (Score Processing)
                                         ↓
                                   Memorystore (Live Rankings)
                                         ↓
                                   CDN (Leaderboard Distribution)
```

**Implementation**:
```python
# Real-time gaming leaderboard
from google.cloud import firestore
import redis
import json
from datetime import datetime

class GameLeaderboard:
    def __init__(self):
        self.db = firestore.Client()
        self.redis_client = redis.from_url('redis://memorystore-ip:6379')
    
    def submit_score(self, player_id, game_mode, score):
        # Update player's best score in Firestore
        player_ref = self.db.collection('players').document(player_id)
        player_doc = player_ref.get()
        
        if player_doc.exists:
            player_data = player_doc.to_dict()
            current_best = player_data.get(f'best_scores.{game_mode}', 0)
        else:
            current_best = 0
        
        if score > current_best:
            # Update Firestore
            player_ref.set({
                f'best_scores.{game_mode}': score,
                'last_played': firestore.SERVER_TIMESTAMP
            }, merge=True)
        
        # Update real-time leaderboard in Redis
        leaderboard_key = f"leaderboard:{game_mode}"
        
        # Add to sorted set (score as key for descending order)
        self.redis_client.zadd(leaderboard_key, {player_id: score})
        
        # Keep only top 1000 players
        self.redis_client.zremrangebyrank(leaderboard_key, 0, -1001)
        
        # Cache player info
        player_info_key = f"player:{player_id}"
        self.redis_client.hset(player_info_key, mapping={
            'name': player_data.get('name', 'Anonymous'),
            'avatar': player_data.get('avatar_url', ''),
            'level': player_data.get('level', 1)
        })
        self.redis_client.expire(player_info_key, 3600)  # 1 hour TTL
        
        return True
    
    def get_leaderboard(self, game_mode, limit=50, offset=0):
        leaderboard_key = f"leaderboard:{game_mode}"
        
        # Get top players from Redis
        top_players = self.redis_client.zrevrange(leaderboard_key, offset, offset + limit - 1, withscores=True)
        
        # Get player info
        leaderboard = []
        for player_id, score in top_players:
            player_info = self.redis_client.hgetall(f"player:{player_id.decode()}")
            
            leaderboard.append({
                'player_id': player_id.decode(),
                'name': player_info.get(b'name', b'Anonymous').decode(),
                'avatar': player_info.get(b'avatar', b'').decode(),
                'level': int(player_info.get(b'level', 1)),
                'score': int(score)
            })
        
        return leaderboard
    
    def get_player_rank(self, player_id, game_mode):
        leaderboard_key = f"leaderboard:{game_mode}"
        rank = self.redis_client.zrevrank(leaderboard_key, player_id)
        
        if rank is not None:
            return rank + 1  # Convert to 1-based ranking
        return None
```

**Benefits**:
- Real-time leaderboard updates
- Low latency with Redis caching
- Scalable to millions of players
- Persistent storage with Firestore

## 📊 Performance Considerations

### Storage Optimization
- **Cloud Storage**: Use appropriate storage classes and lifecycle policies
- **Cloud SQL**: Optimize queries, use read replicas, enable caching
- **Firestore**: Use compound queries, avoid large documents
- **Bigtable**: Design row keys for even distribution
- **Spanner**: Use proper indexing and schema design

### Data Access Patterns
- **Hot data**: Use caching layers (Memorystore)
- **Cold data**: Use archival storage classes
- **Real-time**: Choose databases with low latency
- **Analytics**: Use data warehouses like BigQuery

## 💰 Cost Optimization Strategies

### General Tips
1. **Use lifecycle policies** to automatically transition data to cheaper storage
2. **Implement data retention policies** to delete unnecessary data
3. **Use regional storage** when global access isn't needed
4. **Optimize query patterns** to reduce read/write operations
5. **Leverage free tiers** and sustained use discounts

### Service-Specific Optimization
- **Cloud Storage**: Use appropriate storage classes based on access patterns
- **Cloud SQL**: Use right-sized instances and storage
- **Firestore**: Optimize document structure and query patterns
- **Bigtable**: Choose appropriate node count and storage
- **Spanner**: Optimize instance configuration and query performance

---

*For quick commands, see [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)*
*For setup instructions, see [SETUP.md](./SETUP.md)*
