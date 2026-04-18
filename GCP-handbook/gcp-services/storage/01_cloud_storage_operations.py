#!/usr/bin/env python3
"""
01_cloud_storage_operations.py
Cloud Storage basic operations example

This example demonstrates how to:
- Create and manage buckets
- Upload and download files
- Set bucket configurations
- Implement lifecycle policies
- Use signed URLs for secure access
"""

import os
import datetime
from google.cloud import storage
from google.cloud.storage import transfer_manager
from typing import List, Optional

class CloudStorageManager:
    """
    A comprehensive Cloud Storage management class
    """
    
    def __init__(self, project_id: str):
        """
        Initialize the Cloud Storage client
        
        Args:
            project_id: GCP project ID
        """
        self.client = storage.Client(project=project_id)
        
    def create_bucket(self, bucket_name: str, location: str = "US", 
                     storage_class: str = "STANDARD") -> storage.Bucket:
        """
        Create a new Cloud Storage bucket
        
        Args:
            bucket_name: Name of the bucket (must be globally unique)
            location: Bucket location
            storage_class: Storage class (STANDARD, NEARLINE, COLDLINE, ARCHIVE)
        
        Returns:
            Bucket object
        """
        
        print(f"Creating bucket '{bucket_name}' in {location}...")
        
        try:
            bucket = self.client.create_bucket(
                bucket_name,
                location=location,
                storage_class=storage_class
            )
            
            print(f"✅ Bucket '{bucket_name}' created successfully!")
            print(f"   Location: {bucket.location}")
            print(f"   Storage Class: {bucket.storage_class}")
            
            return bucket
            
        except Exception as error:
            print(f"❌ Error creating bucket: {error}")
            return None
    
    def list_buckets(self) -> List[storage.Bucket]:
        """
        List all buckets in the project
        
        Returns:
            List of bucket objects
        """
        
        print("Listing buckets...")
        
        try:
            buckets = list(self.client.list_buckets())
            
            print(f"📋 Found {len(buckets)} buckets:")
            for bucket in buckets:
                print(f"   - {bucket.name} ({bucket.location}, {bucket.storage_class})")
            
            return buckets
            
        except Exception as error:
            print(f"❌ Error listing buckets: {error}")
            return []
    
    def upload_file(self, bucket_name: str, source_file_path: str, 
                   destination_blob_name: Optional[str] = None) -> storage.Blob:
        """
        Upload a file to Cloud Storage
        
        Args:
            bucket_name: Name of the bucket
            source_file_path: Path to the source file
            destination_blob_name: Destination blob name (defaults to filename)
        
        Returns:
            Blob object
        """
        
        if destination_blob_name is None:
            destination_blob_name = os.path.basename(source_file_path)
        
        print(f"Uploading '{source_file_path}' to '{bucket_name}/{destination_blob_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            
            # Upload file
            blob.upload_from_filename(source_file_path)
            
            print(f"✅ File uploaded successfully!")
            print(f"   Size: {blob.size} bytes")
            print(f"   Content Type: {blob.content_type}")
            print(f"   Public URL: {blob.public_url}")
            
            return blob
            
        except Exception as error:
            print(f"❌ Error uploading file: {error}")
            return None
    
    def upload_from_string(self, bucket_name: str, content: str, 
                          destination_blob_name: str) -> storage.Blob:
        """
        Upload string content to Cloud Storage
        
        Args:
            bucket_name: Name of the bucket
            content: String content to upload
            destination_blob_name: Destination blob name
        
        Returns:
            Blob object
        """
        
        print(f"Uploading content to '{bucket_name}/{destination_blob_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            
            # Upload content
            blob.upload_from_string(content, content_type='text/plain')
            
            print(f"✅ Content uploaded successfully!")
            print(f"   Size: {len(content)} bytes")
            print(f"   Public URL: {blob.public_url}")
            
            return blob
            
        except Exception as error:
            print(f"❌ Error uploading content: {error}")
            return None
    
    def download_file(self, bucket_name: str, blob_name: str, 
                     destination_file_path: str) -> bool:
        """
        Download a file from Cloud Storage
        
        Args:
            bucket_name: Name of the bucket
            blob_name: Name of the blob
            destination_file_path: Path to save the downloaded file
        
        Returns:
            True if successful, False otherwise
        """
        
        print(f"Downloading '{bucket_name}/{blob_name}' to '{destination_file_path}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            
            # Download file
            blob.download_to_filename(destination_file_path)
            
            print(f"✅ File downloaded successfully!")
            print(f"   Size: {os.path.getsize(destination_file_path)} bytes")
            
            return True
            
        except Exception as error:
            print(f"❌ Error downloading file: {error}")
            return False
    
    def list_blobs(self, bucket_name: str, prefix: Optional[str] = None) -> List[storage.Blob]:
        """
        List blobs in a bucket
        
        Args:
            bucket_name: Name of the bucket
            prefix: Prefix to filter blobs
        
        Returns:
            List of blob objects
        """
        
        print(f"Listing blobs in '{bucket_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blobs = list(bucket.list_blobs(prefix=prefix))
            
            print(f"📋 Found {len(blobs)} blobs:")
            for blob in blobs:
                size_mb = blob.size / (1024 * 1024) if blob.size else 0
                print(f"   - {blob.name} ({size_mb:.2f} MB, {blob.updated})")
            
            return blobs
            
        except Exception as error:
            print(f"❌ Error listing blobs: {error}")
            return []
    
    def delete_blob(self, bucket_name: str, blob_name: str) -> bool:
        """
        Delete a blob from Cloud Storage
        
        Args:
            bucket_name: Name of the bucket
            blob_name: Name of the blob to delete
        
        Returns:
            True if successful, False otherwise
        """
        
        print(f"Deleting '{bucket_name}/{blob_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.delete()
            
            print(f"✅ Blob deleted successfully!")
            return True
            
        except Exception as error:
            print(f"❌ Error deleting blob: {error}")
            return False
    
    def enable_versioning(self, bucket_name: str) -> bool:
        """
        Enable versioning for a bucket
        
        Args:
            bucket_name: Name of the bucket
        
        Returns:
            True if successful, False otherwise
        """
        
        print(f"Enabling versioning for '{bucket_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            bucket.versioning_enabled = True
            bucket.patch()
            
            print(f"✅ Versioning enabled successfully!")
            return True
            
        except Exception as error:
            print(f"❌ Error enabling versioning: {error}")
            return False
    
    def set_lifecycle_rule(self, bucket_name: str, age_days: int, 
                          action: str = "Delete") -> bool:
        """
        Set lifecycle rule for a bucket
        
        Args:
            bucket_name: Name of the bucket
            age_days: Age in days for the rule
            action: Action to take (Delete, SetStorageClass)
        
        Returns:
            True if successful, False otherwise
        """
        
        print(f"Setting lifecycle rule for '{bucket_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            
            # Define lifecycle rule
            rule = {
                "action": {"type": action},
                "condition": {"age": age_days}
            }
            
            if action == "SetStorageClass":
                rule["action"]["storageClass"] = "NEARLINE"
            
            bucket.lifecycle_rules = [rule]
            bucket.patch()
            
            print(f"✅ Lifecycle rule set successfully!")
            print(f"   Action: {action}")
            print(f"   Age: {age_days} days")
            
            return True
            
        except Exception as error:
            print(f"❌ Error setting lifecycle rule: {error}")
            return False
    
    def generate_signed_url(self, bucket_name: str, blob_name: str, 
                          expiration_minutes: int = 15,
                          method: str = "GET") -> Optional[str]:
        """
        Generate a signed URL for a blob
        
        Args:
            bucket_name: Name of the bucket
            blob_name: Name of the blob
            expiration_minutes: URL expiration time in minutes
            method: HTTP method (GET, PUT, DELETE)
        
        Returns:
            Signed URL string or None if failed
        """
        
        print(f"Generating signed URL for '{bucket_name}/{blob_name}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            
            # Generate signed URL
            url = blob.generate_signed_url(
                version="v4",
                expiration=datetime.timedelta(minutes=expiration_minutes),
                method=method
            )
            
            print(f"✅ Signed URL generated successfully!")
            print(f"   URL: {url}")
            print(f"   Expires in: {expiration_minutes} minutes")
            
            return url
            
        except Exception as error:
            print(f"❌ Error generating signed URL: {error}")
            return None
    
    def upload_directory(self, bucket_name: str, source_dir: str, 
                        destination_prefix: str = "") -> bool:
        """
        Upload an entire directory to Cloud Storage
        
        Args:
            bucket_name: Name of the bucket
            source_dir: Source directory path
            destination_prefix: Destination prefix in bucket
        
        Returns:
            True if successful, False otherwise
        """
        
        print(f"Uploading directory '{source_dir}' to '{bucket_name}/{destination_prefix}'...")
        
        try:
            bucket = self.client.bucket(bucket_name)
            
            # Use transfer manager for efficient uploads
            results = transfer_manager.upload_many_from_filenames(
                bucket=bucket,
                source_directory=source_dir,
                blob_name_prefix=destination_prefix,
                max_workers=8
            )
            
            # Check results
            successful = sum(1 for result in results if result[0] is not None)
            total = len(results)
            
            print(f"✅ Directory upload completed!")
            print(f"   Successfully uploaded: {successful}/{total} files")
            
            return successful == total
            
        except Exception as error:
            print(f"❌ Error uploading directory: {error}")
            return False

def main():
    """Main function to demonstrate Cloud Storage operations"""
    
    # Configuration
    PROJECT_ID = "your-project-id"  # Replace with your project ID
    BUCKET_NAME = f"my-demo-bucket-{int(datetime.datetime.now().timestamp())}"
    
    print("🚀 Google Cloud Storage - Operations Example")
    print("=" * 50)
    
    # Initialize storage manager
    storage_manager = CloudStorageManager(PROJECT_ID)
    
    # Create bucket
    bucket = storage_manager.create_bucket(BUCKET_NAME)
    
    if bucket:
        # Upload a text file
        test_content = """
Hello, Cloud Storage!

This is a test file uploaded using the Python client library.
It demonstrates basic Cloud Storage operations.

Features demonstrated:
- Bucket creation
- File upload
- File download
- Listing blobs
- Lifecycle management
- Signed URLs

Enjoy using Google Cloud Storage!
        """.strip()
        
        blob = storage_manager.upload_from_string(
            BUCKET_NAME, 
            test_content, 
            "test-files/sample.txt"
        )
        
        # List blobs
        storage_manager.list_blobs(BUCKET_NAME)
        
        # Enable versioning
        storage_manager.enable_versioning(BUCKET_NAME)
        
        # Set lifecycle rule (delete files after 30 days)
        storage_manager.set_lifecycle_rule(BUCKET_NAME, 30, "Delete")
        
        # Generate signed URL
        if blob:
            signed_url = storage_manager.generate_signed_url(BUCKET_NAME, blob.name)
        
        # Download file
        storage_manager.download_file(BUCKET_NAME, "test-files/sample.txt", "downloaded_sample.txt")
        
        # List all buckets
        storage_manager.list_buckets()
        
        print("\n🎉 Example completed successfully!")
        print("\n📚 What was demonstrated:")
        print("1. ✅ Bucket creation with configuration")
        print("2. ✅ File upload from string")
        print("3. ✅ Blob listing")
        print("4. ✅ Versioning enablement")
        print("5. ✅ Lifecycle rule configuration")
        print("6. ✅ Signed URL generation")
        print("7. ✅ File download")
        print("8. ✅ Bucket listing")
        
        print(f"\n📁 Files created:")
        print(f"- downloaded_sample.txt")
        print(f"- Bucket: {BUCKET_NAME}")
        
        print("\n🧹 Clean up:")
        print(f"To delete the bucket, run:")
        print(f"gsutil rm -r gs://{BUCKET_NAME}")
        
    else:
        print("\n❌ Example failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
