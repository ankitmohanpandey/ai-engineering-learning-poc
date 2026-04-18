#!/usr/bin/env python3
"""
01_create_vm_instance.py
Basic example: Create a Compute Engine VM instance

This example demonstrates how to:
- Create a Compute Engine VM instance
- Configure instance settings
- Wait for instance creation
- Verify instance status
"""

import time
from google.cloud import compute_v1
from google.api_core import operation

def create_vm_instance(project_id: str, zone: str, instance_name: str):
    """
    Create a Compute Engine VM instance
    
    Args:
        project_id: GCP project ID
        zone: Zone where the instance will be created
        instance_name: Name of the VM instance
    
    Returns:
        Operation result
    """
    
    # Initialize Compute Engine client
    compute_client = compute_v1.InstancesClient()
    
    # Define machine type
    machine_type = f"zones/{zone}/machineTypes/e2-medium"
    
    # Define disk configuration
    disk = compute_v1.AttachedDisk()
    disk.boot = True
    disk.auto_delete = True
    disk.initialize_params = compute_v1.AttachedDiskInitializeParams()
    disk.initialize_params.source_image = "projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20230801"
    disk.initialize_params.disk_size_gb = 20
    
    # Define network configuration
    network_interface = compute_v1.NetworkInterface()
    network_interface.name = "default"
    
    # Define instance configuration
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = machine_type
    instance.disks = [disk]
    instance.network_interfaces = [network_interface]
    
    # Add tags for firewall rules
    instance.tags = compute_v1.Tags(items=["http-server", "https-server"])
    
    # Add metadata with startup script
    metadata = compute_v1.Metadata()
    metadata.items = [
        compute_v1.Metadata.Items(
            key="startup-script",
            value="""#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
echo "Hello from $(hostname)" > /var/www/html/index.html
"""
        )
    ]
    instance.metadata = metadata
    
    print(f"Creating VM instance '{instance_name}' in zone '{zone}'...")
    
    try:
        # Create the instance
        operation = compute_client.insert(
            project=project_id,
            zone=zone,
            instance_resource=instance
        )
        
        print(f"Operation started: {operation.name}")
        print("Waiting for instance creation to complete...")
        
        # Wait for operation to complete
        operation.result()
        
        print(f"✅ VM instance '{instance_name}' created successfully!")
        
        # Get instance details
        instance_info = compute_client.get(
            project=project_id,
            zone=zone,
            instance=instance_name
        )
        
        # Get external IP
        external_ip = None
        for interface in instance_info.network_interfaces:
            if interface.access_configs:
                external_ip = interface.access_configs[0].nat_i_p
                break
        
        print(f"📋 Instance Details:")
        print(f"   Name: {instance_info.name}")
        print(f"   Status: {instance_info.status}")
        print(f"   Machine Type: {instance_info.machine_type.split('/')[-1]}")
        print(f"   External IP: {external_ip}")
        print(f"   Internal IP: {instance_info.network_interfaces[0].network_i_p}")
        
        if external_ip:
            print(f"🌐 Access your instance at: http://{external_ip}")
        
        return instance_info
        
    except Exception as error:
        print(f"❌ Error creating instance: {error}")
        return None

def wait_for_instance_ready(project_id: str, zone: str, instance_name: str, timeout: int = 300):
    """
    Wait for VM instance to be in RUNNING state
    
    Args:
        project_id: GCP project ID
        zone: Zone where the instance is located
        instance_name: Name of the VM instance
        timeout: Maximum time to wait in seconds
    """
    
    compute_client = compute_v1.InstancesClient()
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            instance = compute_client.get(
                project=project_id,
                zone=zone,
                instance=instance_name
            )
            
            if instance.status == "RUNNING":
                print(f"✅ Instance '{instance_name}' is ready!")
                return True
            elif instance.status == "TERMINATED":
                print(f"⚠️  Instance '{instance_name}' is terminated")
                return False
            else:
                print(f"⏳ Instance status: {instance.status}")
                time.sleep(10)
                
        except Exception as error:
            print(f"❌ Error checking instance status: {error}")
            return False
    
    print(f"⏰ Timeout waiting for instance to be ready")
    return False

def main():
    """Main function to demonstrate VM creation"""
    
    # Configuration
    PROJECT_ID = "your-project-id"  # Replace with your project ID
    ZONE = "us-central1-a"
    INSTANCE_NAME = "my-first-vm"
    
    print("🚀 Google Compute Engine - VM Creation Example")
    print("=" * 50)
    
    # Create VM instance
    instance = create_vm_instance(PROJECT_ID, ZONE, INSTANCE_NAME)
    
    if instance:
        # Wait for instance to be ready
        wait_for_instance_ready(PROJECT_ID, ZONE, INSTANCE_NAME)
        
        print("\n🎉 Example completed successfully!")
        print("\n📚 Next steps:")
        print("1. SSH into the instance: gcloud compute ssh " + INSTANCE_NAME + " --zone=" + ZONE)
        print("2. Access the web server: http://" + (instance.network_interfaces[0].access_configs[0].nat_i_p if instance.network_interfaces[0].access_configs else "EXTERNAL_IP"))
        print("3. Check the startup script output: curl http://localhost")
        
    else:
        print("\n❌ Example failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
