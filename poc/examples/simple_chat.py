"""
Simple Chat Example - AI Engineering POC

A basic chatbot with conversation memory using Google Gemini.

Features:
1. Interactive chat interface
2. Conversation history
3. Context awareness
4. Graceful exit

Run this example:
    python poc/examples/simple_chat.py
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Load environment variables
load_dotenv()

# ============================================================================
# Simple Chatbot Class
# ============================================================================

class SimpleChatbot:
    """
    A simple chatbot with conversation memory
    """
    
    def __init__(self, model_name: str = 'gemini-pro'):
        """
        Initialize chatbot
        
        Args:
            model_name: Gemini model to use
        """
        # Get API key
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Create model
        self.model = genai.GenerativeModel(model_name)
        
        # Start chat
        self.chat = self.model.start_chat(history=[])
        
        # System message
        self.system_message = """You are a helpful AI assistant. 
You are friendly, concise, and knowledgeable. 
You help users learn about AI and answer their questions."""
        
        # Send system message
        self.chat.send_message(self.system_message)
    
    def send_message(self, message: str) -> str:
        """
        Send message and get response
        
        Args:
            message: User message
            
        Returns:
            Assistant response
        """
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {e}"
    
    def get_history(self) -> list:
        """
        Get conversation history
        
        Returns:
            List of messages
        """
        history = []
        for msg in self.chat.history[1:]:  # Skip system message
            history.append({
                'role': msg.role,
                'content': msg.parts[0].text
            })
        return history
    
    def clear_history(self):
        """Clear conversation history"""
        self.chat = self.model.start_chat(history=[])
        self.chat.send_message(self.system_message)


# ============================================================================
# Interactive Chat Interface
# ============================================================================

def run_interactive_chat():
    """
    Run interactive chat session
    """
    print("\n" + "=" * 60)
    print("SIMPLE AI CHATBOT")
    print("=" * 60)
    print("\nWelcome! I'm your AI assistant.")
    print("I can help you learn about AI and answer your questions.")
    print("\nCommands:")
    print("  - Type your message and press Enter to chat")
    print("  - Type 'history' to see conversation history")
    print("  - Type 'clear' to clear conversation history")
    print("  - Type 'quit' or 'exit' to end the chat")
    print("=" * 60 + "\n")
    
    # Create chatbot
    try:
        chatbot = SimpleChatbot()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nPlease ensure:")
        print("1. You have created .env file (cp .env.example .env)")
        print("2. You have added your GEMINI_API_KEY to .env")
        return
    
    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for empty input
            if not user_input:
                continue
            
            # Check for commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nAssistant: Goodbye! Have a great day! 👋\n")
                break
            
            elif user_input.lower() == 'history':
                print("\n" + "-" * 60)
                print("CONVERSATION HISTORY")
                print("-" * 60)
                history = chatbot.get_history()
                for i, msg in enumerate(history, 1):
                    role = "You" if msg['role'] == 'user' else "Assistant"
                    print(f"\n{i}. {role}:")
                    print(f"   {msg['content']}")
                print("-" * 60 + "\n")
                continue
            
            elif user_input.lower() == 'clear':
                chatbot.clear_history()
                print("\nAssistant: Conversation history cleared! Let's start fresh. 🔄\n")
                continue
            
            # Get response
            print("\nAssistant: ", end='', flush=True)
            response = chatbot.send_message(user_input)
            print(response + "\n")
            
        except KeyboardInterrupt:
            print("\n\nAssistant: Goodbye! Have a great day! 👋\n")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


# ============================================================================
# Demo Mode (Non-interactive)
# ============================================================================

def run_demo():
    """
    Run demo conversation (non-interactive)
    """
    print("\n" + "=" * 60)
    print("SIMPLE CHATBOT DEMO")
    print("=" * 60 + "\n")
    
    # Create chatbot
    chatbot = SimpleChatbot()
    
    # Demo conversation
    demo_messages = [
        "Hi! What can you help me with?",
        "I want to learn about AI. Where should I start?",
        "What's the difference between AI and machine learning?",
        "Can you explain what LLMs are?",
        "Thanks for your help!"
    ]
    
    for message in demo_messages:
        print(f"You: {message}")
        response = chatbot.send_message(message)
        print(f"Assistant: {response}\n")
    
    # Show history
    print("-" * 60)
    print("CONVERSATION SUMMARY")
    print("-" * 60)
    history = chatbot.get_history()
    print(f"Total messages: {len(history)}")
    print(f"User messages: {len([m for m in history if m['role'] == 'user'])}")
    print(f"Assistant messages: {len([m for m in history if m['role'] == 'model'])}")
    print("-" * 60 + "\n")


# ============================================================================
# Main execution
# ============================================================================

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple AI Chatbot')
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode (non-interactive)'
    )
    
    args = parser.parse_args()
    
    if args.demo:
        run_demo()
    else:
        run_interactive_chat()


if __name__ == '__main__':
    main()


"""
DETAILED EXPLANATION
====================

1. CHATBOT ARCHITECTURE

   Components:
   - Model: Gemini LLM
   - Chat: Conversation manager
   - History: Message storage
   - Interface: User interaction
   
   Flow:
   User Input → Chat → Model → Response → Display

2. CONVERSATION MEMORY

   How it works:
   - Chat object maintains history
   - Each message added to history
   - Context sent with each request
   - Model uses history for context
   
   Benefits:
   - Contextual responses
   - Follow-up questions work
   - Coherent conversation

3. SYSTEM MESSAGE

   Purpose:
   - Define assistant behavior
   - Set personality
   - Provide instructions
   
   Example:
   "You are a helpful AI assistant.
   You are friendly and concise."

4. INTERACTIVE MODE

   Features:
   - Real-time chat
   - Command support
   - History viewing
   - Graceful exit
   
   Commands:
   - history: View conversation
   - clear: Reset conversation
   - quit/exit: End chat

5. DEMO MODE

   Purpose:
   - Test chatbot
   - Show capabilities
   - No user input needed
   
   Usage:
   python simple_chat.py --demo

6. ERROR HANDLING

   Handled errors:
   - Missing API key
   - API failures
   - Network issues
   - Invalid input
   
   User-friendly messages displayed

7. CONVERSATION FLOW

   1. Initialize chatbot
   2. Send system message
   3. User sends message
   4. Model generates response
   5. Display response
   6. Repeat 3-5

8. CONTEXT MANAGEMENT

   Automatic:
   - Gemini manages context
   - History included in requests
   - No manual context handling
   
   Limitations:
   - Context window limit
   - Older messages may be dropped

9. CUSTOMIZATION

   Easy to modify:
   - Change system message
   - Adjust model parameters
   - Add new commands
   - Customize interface

10. BEST PRACTICES

    ✅ Clear system message
    ✅ Handle errors gracefully
    ✅ Provide user feedback
    ✅ Allow conversation reset
    ✅ Show conversation history
    
    ❌ Don't ignore errors
    ❌ Don't lose context
    ❌ Don't block on errors

11. EXTENDING THE CHATBOT

    Add features:
    - Streaming responses
    - Save conversations
    - Multiple personalities
    - Tool integration
    - RAG capabilities

12. USAGE

    Interactive mode:
    python poc/examples/simple_chat.py
    
    Demo mode:
    python poc/examples/simple_chat.py --demo
    
    Requirements:
    - GEMINI_API_KEY in .env
    - google-generativeai installed

13. NEXT STEPS

    Learn more:
    - Add memory persistence
    - Implement RAG
    - Add tools/functions
    - Build web interface
    - Deploy to production
"""
