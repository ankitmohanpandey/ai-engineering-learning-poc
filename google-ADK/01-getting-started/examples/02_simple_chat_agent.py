#!/usr/bin/env python3
"""
Example: Simple Chat Agent
Description: Interactive conversation agent with turn-taking
Concepts: Conversation handling, user interaction, basic chat loop
Difficulty: Beginner
Time: 10 minutes
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

def create_chat_agent():
    """
    Create a simple chat agent for conversations
    
    Returns:
        Agent: Configured chat agent
    """
    
    agent = Agent(
        name="simple_chat_agent",
        description="An interactive chat agent that can engage in conversations",
        model="text-bison@001",
        temperature=0.8,  # Slightly more creative for conversations
        max_tokens=1024,  # Longer responses for better conversations
        instructions="""
        You are a friendly and engaging conversational AI assistant. Your role is to:
        
        1. Have natural, flowing conversations with users
        2. Ask follow-up questions to keep conversations interesting
        3. Share helpful information when appropriate
        4. Be empathetic and understanding
        5. Remember context within the current conversation
        6. Avoid repetitive responses
        
        Conversation guidelines:
        - Use a friendly, conversational tone
        - Ask questions to encourage dialogue
        - Share relevant experiences or knowledge
        - Be supportive and positive
        - If you don't know something, say so honestly
        - Keep responses engaging but not too long
        
        You don't have access to external tools or memory beyond the current conversation,
        but you can have meaningful discussions about various topics.
        """
    )
    
    return agent

def print_welcome():
    """Print welcome message and instructions"""
    print("💬 Simple Chat Agent")
    print("=" * 50)
    print("Welcome! I'm your AI chat assistant. Let's have a conversation!")
    print()
    print("Instructions:")
    print("• Type your message and press Enter")
    print("• Type 'quit', 'exit', or 'bye' to end the conversation")
    print("• Type 'help' for assistance")
    print("• Type 'clear' to clear the conversation context")
    print()

def print_help():
    """Print help information"""
    print("📚 Help - Available Commands:")
    print("• help     - Show this help message")
    print("• clear    - Clear conversation context")
    print("• quit     - End the conversation")
    print("• exit     - End the conversation")
    print("• bye      - End the conversation")
    print()
    print("💡 Tips for better conversations:")
    print("• Ask me questions about various topics")
    print("• Share your thoughts and opinions")
    print("• Ask for advice or recommendations")
    print("• Discuss current events or interests")

def should_exit(user_input):
    """Check if user wants to exit"""
    exit_commands = ['quit', 'exit', 'bye', 'goodbye', 'see you', 'cya']
    return user_input.lower().strip() in exit_commands

def is_help_command(user_input):
    """Check if user asked for help"""
    help_commands = ['help', 'commands', 'instructions']
    return user_input.lower().strip() in help_commands

def is_clear_command(user_input):
    """Check if user wants to clear context"""
    clear_commands = ['clear', 'reset', 'start over']
    return user_input.lower().strip() in clear_commands

def main():
    """Main chat loop"""
    
    print_welcome()
    
    # Check if environment is set up
    if not os.getenv("GOOGLE_CLOUD_PROJECT"):
        print("⚠️  Warning: GOOGLE_CLOUD_PROJECT not set")
        print("   Some features may not work correctly")
        print()
    
    try:
        # Create the agent
        print("🔧 Initializing chat agent...")
        agent = create_chat_agent()
        print("✅ Chat agent ready!")
        print()
        
        conversation_count = 0
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = input("👤 You: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                conversation_count += 1
                
                # Handle special commands
                if should_exit(user_input):
                    print(f"\n🤖 Agent: Goodbye! It was nice chatting with you ({conversation_count} exchanges).")
                    break
                
                if is_help_command(user_input):
                    print_help()
                    continue
                
                if is_clear_command(user_input):
                    print("\n🤖 Agent: Conversation context cleared. Let's start fresh!")
                    print()
                    continue
                
                # Process user input with agent
                print("💭 Agent is thinking...")
                
                try:
                    response = agent.run(user_input)
                    print(f"🤖 Agent: {response}")
                    print()
                    
                except Exception as e:
                    print(f"❌ Agent error: {e}")
                    print("🤖 Agent: I'm having trouble processing that. Could you try rephrasing?")
                    print()
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 Agent: Conversation interrupted. Goodbye! ({conversation_count} exchanges)")
                break
            except EOFError:
                print(f"\n\n🤖 Agent: End of input. Goodbye! ({conversation_count} exchanges)")
                break
        
        print("\n" + "=" * 50)
        print("📊 Conversation Summary:")
        print(f"   Total exchanges: {conversation_count}")
        print("✅ Chat session completed successfully!")
        print()
        print("🎯 What you learned:")
        print("   ✓ How to create an interactive chat agent")
        print("   ✓ How to handle user input and commands")
        print("   ✓ How to manage conversation flow")
        print("   ✓ Basic error handling in conversations")
        print()
        print("🚀 Next steps:")
        print("   → Add memory in 03_agent_with_memory.py")
        print("   → Learn about tools in 04_tool_using_agent.py")
        print("   → Try multi-tool agent in 05_multi_tool_agent.py")
        
    except Exception as e:
        print(f"❌ Failed to start chat agent: {e}")
        print()
        print("🔧 Troubleshooting:")
        print("   1. Ensure Google ADK is installed: pip install google-adk")
        print("   2. Check environment variables are set")
        print("   3. Verify Google Cloud project and permissions")
        print("   4. Run installation guide: ../02-installation-setup/README.md")
        sys.exit(1)

if __name__ == "__main__":
    main()
