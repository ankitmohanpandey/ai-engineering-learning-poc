#!/usr/bin/env python3
"""
Example: Hello World Agent
Description: Your first Google ADK agent - a simple greeting agent
Concepts: Basic agent creation, simple responses, agent configuration
Difficulty: Beginner
Time: 5 minutes
"""

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from google_adk import Agent
except ImportError:
    print("❌ Google ADK not installed. Please run:")
    print("   pip install google-adk")
    sys.exit(1)

# Load environment variables
load_dotenv()

def create_hello_agent():
    """
    Create a simple hello world agent
    
    Returns:
        Agent: Configured hello world agent
    """
    
    # Create the agent with basic configuration
    agent = Agent(
        name="hello_world_agent",
        description="A simple agent that greets users and has basic conversations",
        model="text-bison@001",  # Google's text model
        temperature=0.7,  # Balanced creativity
        max_tokens=512,   # Reasonable response length
        instructions="""
        You are a friendly and helpful AI assistant. Your purpose is to:
        1. Greet users warmly
        2. Answer basic questions about yourself
        3. Explain what Google ADK is in simple terms
        4. Be polite and professional
        
        Keep responses concise and friendly. You don't have access to external tools yet,
        but you can have conversations about general topics.
        """
    )
    
    return agent

def main():
    """Main execution function"""
    
    print("🤖 Hello World Agent")
    print("=" * 50)
    print()
    
    # Check if environment is set up
    if not os.getenv("GOOGLE_CLOUD_PROJECT"):
        print("⚠️  Warning: GOOGLE_CLOUD_PROJECT not set")
        print("   Some features may not work correctly")
        print()
    
    try:
        # Create the agent
        print("🔧 Creating hello world agent...")
        agent = create_hello_agent()
        print(f"✅ Agent '{agent.name}' created successfully!")
        print(f"   Model: {agent.model}")
        print(f"   Description: {agent.description}")
        print()
        
        # Test the agent with some sample inputs
        test_inputs = [
            "Hello, how are you?",
            "What can you do?",
            "What is Google ADK?",
            "Can you help me learn?"
        ]
        
        print("🧪 Testing agent with sample inputs:")
        print("-" * 40)
        
        for i, user_input in enumerate(test_inputs, 1):
            print(f"\n📝 Test {i}: {user_input}")
            print("💭 Agent thinking...")
            
            try:
                # Run the agent
                response = agent.run(user_input)
                print(f"🤖 Agent: {response}")
            except Exception as e:
                print(f"❌ Error: {e}")
                print("   This might be expected if ADK is not fully configured")
        
        print("\n" + "=" * 50)
        print("✅ Agent execution completed!")
        print()
        print("🎯 What you learned:")
        print("   ✓ How to create a basic ADK agent")
        print("   ✓ How to configure agent properties")
        print("   ✓ How to run an agent with input")
        print("   ✓ Basic error handling")
        print()
        print("🚀 Next steps:")
        print("   → Try 02_simple_chat_agent.py for interactive conversations")
        print("   → Learn about memory in 03_agent_with_memory.py")
        print("   → Explore tools in 04_tool_using_agent.py")
        
    except Exception as e:
        print(f"❌ Failed to create or run agent: {e}")
        print()
        print("🔧 Troubleshooting:")
        print("   1. Ensure Google ADK is installed: pip install google-adk")
        print("   2. Check environment variables are set")
        print("   3. Verify Google Cloud project and permissions")
        print("   4. Run installation guide: ../02-installation-setup/README.md")
        sys.exit(1)

if __name__ == "__main__":
    main()
