#!/usr/bin/env python3
"""
02_gke_cluster.py
Google Kubernetes Engine example: Create and manage GKE cluster

This example demonstrates how to:
- Create a GKE cluster
- Configure node pools
- Deploy a sample application
- Scale the deployment
- Clean up resources
"""

import time
from google.cloud import container_v1
from google.api_core import operation
import yaml

def create_gke_cluster(project_id: str, location: str, cluster_name: str):
    """
    Create a GKE cluster
    
    Args:
        project_id: GCP project ID
        location: Region or zone for the cluster
        cluster_name: Name of the GKE cluster
    
    Returns:
        Cluster object or None if failed
    """
    
    # Initialize GKE client
    client = container_v1.ClusterManagerClient()
    
    # Define cluster configuration
    cluster = {
        "name": cluster_name,
        "initial_node_count": 1,  # Ignored when using node pools
        "remove_default_node_pool": True,
        "node_pools": [
            {
                "name": "default-pool",
                "initial_node_count": 3,
                "config": {
                    "machine_type": "e2-medium",
                    "disk_size_gb": 20,
                    "oauth_scopes": [
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring",
                        "https://www.googleapis.com/auth/devstorage.read_only"
                    ]
                },
                "autoscaling": {
                    "enabled": True,
                    "min_node_count": 1,
                    "max_node_count": 5
                },
                "management": {
                    "auto_repair": True,
                    "auto_upgrade": True
                }
            }
        ],
        "networking": {
            "type": "VPC_NATIVE",
            "ip_allocation_policy": {
                "use_ip_aliases": True
            }
        },
        "addons_config": {
            "http_load_balancing": {"disabled": False},
            "horizontal_pod_autoscaling": {"disabled": False},
            "network_policy_config": {"disabled": True}
        }
    }
    
    print(f"Creating GKE cluster '{cluster_name}' in location '{location}'...")
    
    try:
        # Create the cluster
        operation = client.create_cluster(
            request={
                "project_id": project_id,
                "location": location,
                "cluster": cluster
            }
        )
        
        print(f"Operation started: {operation.operation.name}")
        print("Waiting for cluster creation to complete...")
        
        # Wait for operation to complete
        result = operation.result()
        
        print(f"✅ GKE cluster '{cluster_name}' created successfully!")
        
        # Display cluster information
        print(f"📋 Cluster Details:")
        print(f"   Name: {result.name}")
        print(f"   Location: {result.location}")
        print(f"   Status: {result.status.name}")
        print(f"   Node Count: {result.current_node_count}")
        print(f"   Kubernetes Version: {result.master_version}")
        
        return result
        
    except Exception as error:
        print(f"❌ Error creating cluster: {error}")
        return None

def get_cluster_credentials(project_id: str, location: str, cluster_name: str):
    """
    Get cluster credentials for kubectl
    
    Args:
        project_id: GCP project ID
        location: Region or zone for the cluster
        cluster_name: Name of the GKE cluster
    """
    
    import subprocess
    
    print(f"Getting credentials for cluster '{cluster_name}'...")
    
    try:
        cmd = [
            "gcloud", "container", "clusters", "get-credentials",
            cluster_name,
            "--location", location,
            "--project", project_id
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Credentials configured successfully!")
            return True
        else:
            print(f"❌ Error getting credentials: {result.stderr}")
            return False
            
    except Exception as error:
        print(f"❌ Error getting credentials: {error}")
        return False

def deploy_sample_app():
    """
    Deploy a sample web application to the cluster
    """
    
    import subprocess
    
    # Sample deployment manifest
    deployment_manifest = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app
  labels:
    app: hello-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-app
  template:
    metadata:
      labels:
        app: hello-app
    spec:
      containers:
      - name: hello-app
        image: gcr.io/google-samples/hello-app:2.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 200m
            memory: 256Mi
---
apiVersion: v1
kind: Service
metadata:
  name: hello-app-service
spec:
  selector:
    app: hello-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
"""
    
    print("Deploying sample application...")
    
    try:
        # Write manifest to file
        with open("hello-app.yaml", "w") as f:
            f.write(deployment_manifest)
        
        # Apply manifest
        cmd = ["kubectl", "apply", "-f", "hello-app.yaml"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Application deployed successfully!")
            print(result.stdout)
            return True
        else:
            print(f"❌ Error deploying application: {result.stderr}")
            return False
            
    except Exception as error:
        print(f"❌ Error deploying application: {error}")
        return False

def check_deployment_status():
    """
    Check the status of the deployed application
    """
    
    import subprocess
    
    print("Checking deployment status...")
    
    try:
        # Check pods
        cmd = ["kubectl", "get", "pods", "-l", "app=hello-app"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("📋 Pod Status:")
            print(result.stdout)
        
        # Check service
        cmd = ["kubectl", "get", "service", "hello-app-service"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("📋 Service Status:")
            print(result.stdout)
            
            # Extract external IP
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                if len(parts) > 4:
                    external_ip = parts[4]
                    if external_ip and external_ip != "<pending>":
                        print(f"🌐 Access the application at: http://{external_ip}")
            
        return True
        
    except Exception as error:
        print(f"❌ Error checking deployment status: {error}")
        return False

def scale_deployment(replicas: int):
    """
    Scale the deployment to specified number of replicas
    
    Args:
        replicas: Number of replicas to scale to
    """
    
    import subprocess
    
    print(f"Scaling deployment to {replicas} replicas...")
    
    try:
        cmd = ["kubectl", "scale", "deployment", "hello-app", f"--replicas={replicas}"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Deployment scaled to {replicas} replicas!")
            return True
        else:
            print(f"❌ Error scaling deployment: {result.stderr}")
            return False
            
    except Exception as error:
        print(f"❌ Error scaling deployment: {error}")
        return False

def delete_cluster(project_id: str, location: str, cluster_name: str):
    """
    Delete the GKE cluster
    
    Args:
        project_id: GCP project ID
        location: Region or zone for the cluster
        cluster_name: Name of the GKE cluster
    """
    
    client = container_v1.ClusterManagerClient()
    
    print(f"Deleting GKE cluster '{cluster_name}'...")
    
    try:
        operation = client.delete_cluster(
            request={
                "project_id": project_id,
                "location": location,
                "cluster_id": cluster_name
            }
        )
        
        print(f"Deletion operation started: {operation.operation.name}")
        print("Waiting for cluster deletion to complete...")
        
        # Wait for operation to complete
        operation.result()
        
        print(f"✅ GKE cluster '{cluster_name}' deleted successfully!")
        return True
        
    except Exception as error:
        print(f"❌ Error deleting cluster: {error}")
        return False

def main():
    """Main function to demonstrate GKE cluster management"""
    
    # Configuration
    PROJECT_ID = "your-project-id"  # Replace with your project ID
    LOCATION = "us-central1-a"
    CLUSTER_NAME = "my-gke-cluster"
    
    print("🚀 Google Kubernetes Engine - Cluster Management Example")
    print("=" * 60)
    
    # Create GKE cluster
    cluster = create_gke_cluster(PROJECT_ID, LOCATION, CLUSTER_NAME)
    
    if cluster:
        # Get credentials for kubectl
        if get_cluster_credentials(PROJECT_ID, LOCATION, CLUSTER_NAME):
            
            # Wait a bit for cluster to be ready
            print("⏳ Waiting for cluster to be ready...")
            time.sleep(30)
            
            # Deploy sample application
            if deploy_sample_app():
                
                # Wait for deployment
                print("⏳ Waiting for deployment to be ready...")
                time.sleep(60)
                
                # Check deployment status
                check_deployment_status()
                
                # Scale deployment
                print("\n🔄 Scaling deployment...")
                scale_deployment(5)
                
                # Wait for scaling
                time.sleep(30)
                
                # Check status after scaling
                check_deployment_status()
                
                print("\n🎉 Example completed successfully!")
                print("\n📚 Next steps:")
                print("1. Access the application using the external IP shown above")
                print("2. Try scaling the deployment: kubectl scale deployment hello-app --replicas=10")
                print("3. Check logs: kubectl logs -l app=hello-app")
                print("4. Explore the cluster: kubectl get nodes")
                
                # Clean up (uncomment to delete cluster)
                # print("\n🧹 Cleaning up...")
                # delete_cluster(PROJECT_ID, LOCATION, CLUSTER_NAME)
                
    else:
        print("\n❌ Example failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
