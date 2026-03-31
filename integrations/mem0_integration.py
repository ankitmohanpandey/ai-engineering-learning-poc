"""
Mem0 Integration - AI Engineering Handbook

This module demonstrates how to use Mem0 for intelligent memory management
in AI applications.

Mem0 provides:
- Persistent memory across sessions
- Semantic search for relevant memories
- Multi-user support
- Automatic memory updates

Installation:
    pip install mem0ai

Run this example:
    python integrations/mem0_integration.py
"""

import os
import sys
from dotenv import load_dotenv
from mem0 import Memory
import google.generativeai as genai

# Load environment variables
load_dotenv()

# ============================================================================
# EXAMPLE 1: Basic Mem0 Usage
# ============================================================================

def basic_mem0_example():
    """
    Basic memory operations with Mem0
    """
    print("=" * 60)
    print("EXAMPLE 1: Basic Mem0 Usage")
    print("=" * 60)
    
    # Initialize memory
    memory = Memory()
    
    user_id = "user123"
    
    # Add memories
    print("\n1. Adding memories...")
    memories_to_add = [
        "User's name is Ankit",
        "User is learning AI Engineering",
        "User prefers Python over JavaScript",
        "User is building AI agents",
        "User works on data engineering projects"
    ]
    
    for mem in memories_to_add:
        result = memory.add(mem, user_id=user_id)
        print(f"  ✓ Added: {mem}")
    
    # Get all memories
    print("\n2. Retrieving all memories...")
    all_memories = memory.get_all(user_id=user_id)
    print(f"  Total memories: {len(all_memories)}")
    for i, mem in enumerate(all_memories, 1):
        print(f"  {i}. {mem['memory']}")
    
    # Search memories
    print("\n3. Searching memories...")
    search_queries = [
        "What is the user's name?",
        "What programming language does user prefer?",
        "What is user learning?"
    ]
    
    for query in search_queries:
        results = memory.search(query, user_id=user_id, limit=2)
        print(f"\n  Query: {query}")
        for result in results:
            print(f"    → {result['memory']}")
    
    print()


# ============================================================================
# EXAMPLE 2: Mem0 with Gemini LLM
# ============================================================================

def mem0_with_llm_example():
    """
    Use Mem0 to provide context to LLM
    """
    print("=" * 60)
    print("EXAMPLE 2: Mem0 with Gemini LLM")
    print("=" * 60)
    
    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("\n❌ GEMINI_API_KEY not found. Skipping this example.")
        return
    
    # Initialize
    memory = Memory()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    user_id = "user456"
    
    # Add user context
    print("\n1. Storing user information...")
    user_facts = [
        "User is a data engineer",
        "User has 5 years of experience",
        "User specializes in Apache Kafka and Airflow",
        "User is transitioning to AI Engineering",
        "User's goal is to build production AI systems"
    ]
    
    for fact in user_facts:
        memory.add(fact, user_id=user_id)
        print(f"  ✓ Stored: {fact}")
    
    # User asks a question
    print("\n2. User interaction with context...")
    user_question = "What should I learn next to achieve my goals?"
    
    # Retrieve relevant context
    relevant_memories = memory.search(
        user_question,
        user_id=user_id,
        limit=5
    )
    
    # Build context
    context = "\n".join([
        f"- {mem['memory']}"
        for mem in relevant_memories
    ])
    
    # Create prompt with context
    prompt = f"""
You are a helpful AI career advisor.

What you know about the user:
{context}

User question: {user_question}

Provide personalized advice based on what you know about the user.
"""
    
    print(f"\n  User: {user_question}")
    print(f"\n  Retrieved context:")
    for mem in relevant_memories:
        print(f"    - {mem['memory']}")
    
    # Generate response
    response = model.generate_content(prompt)
    print(f"\n  AI Response:\n  {response.text}\n")


# ============================================================================
# EXAMPLE 3: Memory-Enabled Chatbot
# ============================================================================

class MemoryEnabledChatbot:
    """
    Chatbot that remembers user information across conversations
    """
    
    def __init__(self, user_id: str):
        """Initialize chatbot with memory"""
        self.user_id = user_id
        self.memory = Memory()
        
        # Check for API key
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Conversation history (short-term memory)
        self.conversation = []
    
    def chat(self, message: str) -> str:
        """
        Send message and get response with memory context
        
        Args:
            message: User message
            
        Returns:
            AI response
        """
        # Add to conversation history
        self.conversation.append({
            'role': 'user',
            'content': message
        })
        
        # Retrieve relevant long-term memories
        relevant_memories = self.memory.search(
            message,
            user_id=self.user_id,
            limit=3
        )
        
        # Build context from memories
        memory_context = "\n".join([
            f"- {mem['memory']}"
            for mem in relevant_memories
        ]) if relevant_memories else "No previous context"
        
        # Build conversation history (short-term memory)
        recent_conversation = "\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in self.conversation[-5:]  # Last 5 messages
        ])
        
        # Create prompt
        prompt = f"""
You are a helpful AI assistant with memory.

What you remember about the user:
{memory_context}

Recent conversation:
{recent_conversation}

Respond naturally, using what you know about the user when relevant.
"""
        
        # Generate response
        response = self.model.generate_content(prompt)
        response_text = response.text
        
        # Add response to conversation
        self.conversation.append({
            'role': 'assistant',
            'content': response_text
        })
        
        # Store important information from user message
        # (In production, you'd use more sophisticated extraction)
        self.memory.add(message, user_id=self.user_id)
        
        return response_text
    
    def get_all_memories(self):
        """Get all stored memories"""
        return self.memory.get_all(user_id=self.user_id)
    
    def clear_memories(self):
        """Clear all memories for this user"""
        memories = self.get_all_memories()
        for mem in memories:
            self.memory.delete(mem['id'])


def chatbot_example():
    """
    Demonstrate memory-enabled chatbot
    """
    print("=" * 60)
    print("EXAMPLE 3: Memory-Enabled Chatbot")
    print("=" * 60)
    
    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("\n❌ GEMINI_API_KEY not found. Skipping this example.")
        return
    
    try:
        # Create chatbot
        bot = MemoryEnabledChatbot(user_id="demo_user")
        
        # Conversation 1
        print("\n--- Conversation 1 ---")
        messages = [
            "Hi! My name is Ankit and I'm learning AI Engineering.",
            "I'm particularly interested in building AI agents.",
            "I have experience with Python and data engineering."
        ]
        
        for msg in messages:
            print(f"\nUser: {msg}")
            response = bot.chat(msg)
            print(f"Bot: {response[:200]}...")  # Truncate for display
        
        # Show stored memories
        print("\n--- Stored Memories ---")
        memories = bot.get_all_memories()
        for i, mem in enumerate(memories, 1):
            print(f"{i}. {mem['memory']}")
        
        # Conversation 2 (simulating new session)
        print("\n--- Conversation 2 (New Session) ---")
        new_messages = [
            "What's my name?",
            "What am I interested in learning?"
        ]
        
        for msg in new_messages:
            print(f"\nUser: {msg}")
            response = bot.chat(msg)
            print(f"Bot: {response}")
        
        print("\n✓ Chatbot remembers across conversations!\n")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}\n")


# ============================================================================
# EXAMPLE 4: Memory Updates and Management
# ============================================================================

def memory_management_example():
    """
    Demonstrate memory updates and management
    """
    print("=" * 60)
    print("EXAMPLE 4: Memory Updates and Management")
    print("=" * 60)
    
    memory = Memory()
    user_id = "user789"
    
    # Add initial memory
    print("\n1. Adding initial memory...")
    result = memory.add(
        "User is learning Python",
        user_id=user_id
    )
    print(f"  ✓ Added: User is learning Python")
    
    # Get memory ID
    memories = memory.get_all(user_id=user_id)
    if memories:
        memory_id = memories[0]['id']
        
        # Update memory
        print("\n2. Updating memory...")
        memory.update(
            memory_id=memory_id,
            data="User is now proficient in Python and learning AI"
        )
        print(f"  ✓ Updated memory")
        
        # Verify update
        updated = memory.get_all(user_id=user_id)
        print(f"  New value: {updated[0]['memory']}")
    
    # Add more memories
    print("\n3. Adding multiple memories...")
    new_memories = [
        "User completed Apache Kafka tutorial",
        "User built a chatbot with Gemini",
        "User is interested in RAG systems"
    ]
    
    for mem in new_memories:
        memory.add(mem, user_id=user_id)
        print(f"  ✓ Added: {mem}")
    
    # Search and filter
    print("\n4. Searching memories...")
    results = memory.search(
        "What has the user learned?",
        user_id=user_id,
        limit=5
    )
    
    print(f"  Found {len(results)} relevant memories:")
    for result in results:
        print(f"    - {result['memory']}")
    
    # Delete specific memory
    print("\n5. Deleting a memory...")
    if len(memories) > 0:
        memory.delete(memory_id=memories[0]['id'])
        print(f"  ✓ Deleted memory")
    
    # Show remaining
    remaining = memory.get_all(user_id=user_id)
    print(f"\n  Remaining memories: {len(remaining)}")
    
    print()


# ============================================================================
# EXAMPLE 5: Multi-User Memory
# ============================================================================

def multi_user_example():
    """
    Demonstrate separate memory for different users
    """
    print("=" * 60)
    print("EXAMPLE 5: Multi-User Memory")
    print("=" * 60)
    
    memory = Memory()
    
    # User 1
    print("\n1. User 1 memories...")
    user1_facts = [
        "User prefers Python",
        "User is a beginner in AI"
    ]
    for fact in user1_facts:
        memory.add(fact, user_id="user1")
        print(f"  User1: {fact}")
    
    # User 2
    print("\n2. User 2 memories...")
    user2_facts = [
        "User prefers JavaScript",
        "User is an expert in AI"
    ]
    for fact in user2_facts:
        memory.add(fact, user_id="user2")
        print(f"  User2: {fact}")
    
    # Retrieve separately
    print("\n3. Retrieving user-specific memories...")
    
    user1_memories = memory.get_all(user_id="user1")
    print(f"\n  User 1 has {len(user1_memories)} memories:")
    for mem in user1_memories:
        print(f"    - {mem['memory']}")
    
    user2_memories = memory.get_all(user_id="user2")
    print(f"\n  User 2 has {len(user2_memories)} memories:")
    for mem in user2_memories:
        print(f"    - {mem['memory']}")
    
    print("\n  ✓ Memories are isolated per user!\n")


# ============================================================================
# Main execution
# ============================================================================

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("MEM0 INTEGRATION EXAMPLES")
    print("=" * 60 + "\n")
    
    try:
        # Run examples
        basic_mem0_example()
        mem0_with_llm_example()
        chatbot_example()
        memory_management_example()
        multi_user_example()
        
        print("=" * 60)
        print("ALL EXAMPLES COMPLETED!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Explore handbook/06-memory-context/")
        print("2. Build your own memory-enabled chatbot")
        print("3. Experiment with different memory strategies")
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Install mem0: pip install mem0ai")
        print("2. Set GEMINI_API_KEY in .env file")
        print("3. Check your internet connection")
        sys.exit(1)


if __name__ == '__main__':
    main()


"""
DETAILED EXPLANATION
====================

1. WHAT IS MEM0?

   Mem0 is an intelligent memory layer for AI applications that:
   - Stores information persistently
   - Retrieves relevant memories using semantic search
   - Manages multi-user memory separately
   - Updates and consolidates memories automatically
   
   Think of it as giving your AI a "brain" that remembers.

2. KEY FEATURES

   Persistent Storage:
   - Memories survive across sessions
   - No need to repeat information
   
   Semantic Search:
   - Find by meaning, not exact words
   - "What does user like?" finds "User prefers Python"
   
   Multi-User:
   - Separate memory per user
   - Privacy and personalization
   
   Auto-Updates:
   - Consolidates duplicate information
   - Keeps memories current

3. BASIC OPERATIONS

   Add Memory:
   memory.add("User likes Python", user_id="user123")
   
   Search Memory:
   results = memory.search("preferences", user_id="user123")
   
   Get All:
   all_mem = memory.get_all(user_id="user123")
   
   Update:
   memory.update(memory_id="id", data="new data")
   
   Delete:
   memory.delete(memory_id="id")

4. INTEGRATION WITH LLMS

   Flow:
   1. User sends message
   2. Retrieve relevant memories
   3. Add memories to LLM context
   4. Generate response
   5. Store new information
   
   Benefits:
   - Personalized responses
   - Context awareness
   - Continuous learning

5. MEMORY TYPES

   Short-Term (Conversation):
   - In-memory list
   - Current session only
   - Fast access
   
   Long-Term (Mem0):
   - Persistent storage
   - Cross-session
   - Semantic search
   
   Working (Task State):
   - Active processing
   - Temporary
   - Task-specific

6. USE CASES

   Personal Assistants:
   - Remember user preferences
   - Recall past conversations
   - Provide personalized help
   
   Customer Support:
   - Track customer history
   - Remember issues
   - Provide context to agents
   
   Learning Companions:
   - Track progress
   - Remember what was taught
   - Adapt to learning style

7. BEST PRACTICES

   ✅ Store Structured Data:
   memory.add({
       'type': 'preference',
       'value': 'Python',
       'timestamp': datetime.now()
   })
   
   ✅ Use Metadata:
   memory.search(query, filters={'type': 'preference'})
   
   ✅ Update, Don't Duplicate:
   Check existing before adding new
   
   ✅ Implement Privacy:
   Allow users to view/delete their data

8. PERFORMANCE TIPS

   Limit Search Results:
   memory.search(query, limit=5)  # Top 5 only
   
   Use Filters:
   memory.search(query, filters={'recent': True})
   
   Cache Frequently Used:
   @lru_cache
   def get_user_context(user_id):
       return memory.get_all(user_id=user_id)

9. PRIVACY & SECURITY

   Considerations:
   - Store only necessary information
   - Implement data retention policies
   - Allow user data deletion
   - Encrypt sensitive data
   - Comply with GDPR/privacy laws

10. TROUBLESHOOTING

    Memory Not Found:
    - Check user_id is correct
    - Verify memory was added
    - Check filters
    
    Poor Search Results:
    - Improve query phrasing
    - Adjust limit parameter
    - Check memory quality
    
    Performance Issues:
    - Limit search results
    - Use filters
    - Implement caching

11. INSTALLATION

    pip install mem0ai
    
    Requirements:
    - Python 3.8+
    - Internet connection
    - LLM API key (for integration)

12. NEXT STEPS

    Learn More:
    - Read handbook/06-memory-context/
    - Explore RAG systems
    - Build production chatbot
    - Implement advanced memory strategies
"""
