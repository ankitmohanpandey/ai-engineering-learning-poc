"""
Google Gemini Integration - AI Engineering POC

This module demonstrates how to integrate with Google Gemini API.

Features:
1. Basic text generation
2. Streaming responses
3. Conversation handling
4. Error handling
5. Configuration management

Run this example:
    python integrations/gemini_integration.py
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional, List, Dict

# Load environment variables
load_dotenv()

# ============================================================================
# Configuration
# ============================================================================

class GeminiConfig:
    """Configuration for Gemini API"""
    
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.model_name = os.getenv('DEFAULT_MODEL', 'gemini-pro')
        self.temperature = float(os.getenv('DEFAULT_TEMPERATURE', '0.7'))
        self.max_tokens = int(os.getenv('DEFAULT_MAX_TOKENS', '2048'))
        self.top_p = float(os.getenv('DEFAULT_TOP_P', '0.9'))
        
        # Configure API
        genai.configure(api_key=self.api_key)


# ============================================================================
# EXAMPLE 1: Basic Text Generation
# ============================================================================

def basic_generation():
    """
    Simple text generation example
    """
    print("=" * 60)
    print("EXAMPLE 1: Basic Text Generation")
    print("=" * 60)
    
    # Initialize configuration
    config = GeminiConfig()
    
    # Create model
    model = genai.GenerativeModel(config.model_name)
    
    # Generate response
    prompt = "Explain what AI Engineering is in 3 sentences."
    print(f"\nPrompt: {prompt}\n")
    
    response = model.generate_content(prompt)
    print(f"Response:\n{response.text}\n")


# ============================================================================
# EXAMPLE 2: Conversation with History
# ============================================================================

def conversation_example():
    """
    Multi-turn conversation with history
    """
    print("=" * 60)
    print("EXAMPLE 2: Conversation with History")
    print("=" * 60)
    
    config = GeminiConfig()
    model = genai.GenerativeModel(config.model_name)
    
    # Start chat
    chat = model.start_chat(history=[])
    
    # First message
    message1 = "What are the three main types of machine learning?"
    print(f"\nUser: {message1}")
    response1 = chat.send_message(message1)
    print(f"Assistant: {response1.text}\n")
    
    # Follow-up message (uses context)
    message2 = "Can you explain the first one in more detail?"
    print(f"User: {message2}")
    response2 = chat.send_message(message2)
    print(f"Assistant: {response2.text}\n")
    
    # Show conversation history
    print("Conversation History:")
    for i, msg in enumerate(chat.history):
        role = "User" if msg.role == "user" else "Assistant"
        print(f"{i+1}. {role}: {msg.parts[0].text[:100]}...")


# ============================================================================
# EXAMPLE 3: Streaming Responses
# ============================================================================

def streaming_example():
    """
    Stream responses token by token
    """
    print("=" * 60)
    print("EXAMPLE 3: Streaming Responses")
    print("=" * 60)
    
    config = GeminiConfig()
    model = genai.GenerativeModel(config.model_name)
    
    prompt = "Write a short poem about artificial intelligence."
    print(f"\nPrompt: {prompt}\n")
    print("Streaming response:")
    
    response = model.generate_content(prompt, stream=True)
    
    for chunk in response:
        if chunk.text:
            print(chunk.text, end='', flush=True)
    
    print("\n")


# ============================================================================
# EXAMPLE 4: Advanced Configuration
# ============================================================================

def advanced_config_example():
    """
    Use advanced generation configuration
    """
    print("=" * 60)
    print("EXAMPLE 4: Advanced Configuration")
    print("=" * 60)
    
    config = GeminiConfig()
    
    # Create generation config
    generation_config = genai.types.GenerationConfig(
        temperature=0.9,  # Higher = more creative
        top_p=0.95,
        top_k=40,
        max_output_tokens=1024,
        candidate_count=1
    )
    
    model = genai.GenerativeModel(
        config.model_name,
        generation_config=generation_config
    )
    
    prompt = "Generate a creative name for an AI assistant that helps with coding."
    print(f"\nPrompt: {prompt}")
    print(f"Temperature: {generation_config.temperature} (high creativity)\n")
    
    response = model.generate_content(prompt)
    print(f"Response: {response.text}\n")


# ============================================================================
# EXAMPLE 5: Error Handling
# ============================================================================

def error_handling_example():
    """
    Demonstrate proper error handling
    """
    print("=" * 60)
    print("EXAMPLE 5: Error Handling")
    print("=" * 60)
    
    config = GeminiConfig()
    model = genai.GenerativeModel(config.model_name)
    
    prompts = [
        "What is 2+2?",  # Valid
        "",  # Empty prompt
        "A" * 50000,  # Too long
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\nTest {i}: Prompt length = {len(prompt)} characters")
        
        try:
            if not prompt:
                raise ValueError("Prompt cannot be empty")
            
            if len(prompt) > 30000:
                raise ValueError("Prompt too long")
            
            response = model.generate_content(prompt)
            print(f"✓ Success: {response.text[:100]}...")
            
        except ValueError as e:
            print(f"✗ Validation Error: {e}")
        except Exception as e:
            print(f"✗ API Error: {e}")


# ============================================================================
# EXAMPLE 6: Safety Settings
# ============================================================================

def safety_settings_example():
    """
    Configure content safety settings
    """
    print("=" * 60)
    print("EXAMPLE 6: Safety Settings")
    print("=" * 60)
    
    config = GeminiConfig()
    
    # Configure safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    
    model = genai.GenerativeModel(
        config.model_name,
        safety_settings=safety_settings
    )
    
    prompt = "Explain the importance of AI safety."
    print(f"\nPrompt: {prompt}\n")
    
    response = model.generate_content(prompt)
    print(f"Response: {response.text}\n")
    
    # Check safety ratings
    if hasattr(response, 'prompt_feedback'):
        print("Safety Ratings:")
        for rating in response.prompt_feedback.safety_ratings:
            print(f"  {rating.category}: {rating.probability}")


# ============================================================================
# EXAMPLE 7: List Available Models
# ============================================================================

def list_models():
    """
    List all available Gemini models
    """
    print("=" * 60)
    print("EXAMPLE 7: Available Models")
    print("=" * 60)
    
    config = GeminiConfig()
    
    print("\nAvailable Gemini models:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"\n  Model: {model.name}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Description: {model.description}")
            print(f"  Input Token Limit: {model.input_token_limit}")
            print(f"  Output Token Limit: {model.output_token_limit}")


# ============================================================================
# EXAMPLE 8: Token Counting
# ============================================================================

def token_counting_example():
    """
    Count tokens in prompts and responses
    """
    print("=" * 60)
    print("EXAMPLE 8: Token Counting")
    print("=" * 60)
    
    config = GeminiConfig()
    model = genai.GenerativeModel(config.model_name)
    
    prompt = "Explain the concept of embeddings in AI in detail."
    print(f"\nPrompt: {prompt}\n")
    
    # Count tokens
    token_count = model.count_tokens(prompt)
    print(f"Input tokens: {token_count.total_tokens}")
    
    # Generate response
    response = model.generate_content(prompt)
    print(f"\nResponse: {response.text}\n")
    
    # Count response tokens
    response_tokens = model.count_tokens(response.text)
    print(f"Output tokens: {response_tokens.total_tokens}")
    print(f"Total tokens: {token_count.total_tokens + response_tokens.total_tokens}")


# ============================================================================
# Helper Class: GeminiClient
# ============================================================================

class GeminiClient:
    """
    Reusable Gemini client with common functionality
    """
    
    def __init__(self, model_name: str = 'gemini-pro'):
        """Initialize Gemini client"""
        self.config = GeminiConfig()
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name)
        self.chat = None
    
    def generate(self, prompt: str, stream: bool = False) -> str:
        """
        Generate response from prompt
        
        Args:
            prompt: Input prompt
            stream: Whether to stream response
            
        Returns:
            Generated text
        """
        try:
            response = self.model.generate_content(prompt, stream=stream)
            
            if stream:
                full_response = ""
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                return full_response
            else:
                return response.text
                
        except Exception as e:
            return f"Error: {e}"
    
    def start_conversation(self) -> None:
        """Start a new conversation"""
        self.chat = self.model.start_chat(history=[])
    
    def send_message(self, message: str) -> str:
        """
        Send message in conversation
        
        Args:
            message: User message
            
        Returns:
            Assistant response
        """
        if not self.chat:
            self.start_conversation()
        
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {e}"
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        Get conversation history
        
        Returns:
            List of messages
        """
        if not self.chat:
            return []
        
        history = []
        for msg in self.chat.history:
            history.append({
                'role': msg.role,
                'content': msg.parts[0].text
            })
        return history


# ============================================================================
# EXAMPLE 9: Using GeminiClient
# ============================================================================

def client_example():
    """
    Use the GeminiClient helper class
    """
    print("=" * 60)
    print("EXAMPLE 9: Using GeminiClient")
    print("=" * 60)
    
    # Create client
    client = GeminiClient()
    
    # Simple generation
    print("\n1. Simple Generation:")
    response = client.generate("What is machine learning?")
    print(f"Response: {response[:200]}...\n")
    
    # Conversation
    print("2. Conversation:")
    client.start_conversation()
    
    response1 = client.send_message("Hi! Can you help me learn about AI?")
    print(f"User: Hi! Can you help me learn about AI?")
    print(f"Assistant: {response1[:200]}...\n")
    
    response2 = client.send_message("What should I learn first?")
    print(f"User: What should I learn first?")
    print(f"Assistant: {response2[:200]}...\n")


# ============================================================================
# Main execution
# ============================================================================

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("GOOGLE GEMINI INTEGRATION EXAMPLES")
    print("=" * 60 + "\n")
    
    try:
        # Run examples
        basic_generation()
        conversation_example()
        streaming_example()
        advanced_config_example()
        error_handling_example()
        safety_settings_example()
        list_models()
        token_counting_example()
        client_example()
        
        print("=" * 60)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease ensure:")
        print("1. You have created .env file (cp .env.example .env)")
        print("2. You have added your GEMINI_API_KEY to .env")
        print("3. Your API key is valid")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()


"""
DETAILED EXPLANATION
====================

1. GEMINI API BASICS

   Setup:
   - Install: pip install google-generativeai
   - Get API key: https://makersuite.google.com/app/apikey
   - Configure: genai.configure(api_key=api_key)
   
   Basic usage:
   model = genai.GenerativeModel('gemini-pro')
   response = model.generate_content(prompt)
   print(response.text)

2. MODELS AVAILABLE

   - gemini-pro: Text generation
   - gemini-pro-vision: Text + image input
   - gemini-ultra: Most capable (limited access)
   
   Check available models:
   for model in genai.list_models():
       print(model.name)

3. GENERATION CONFIGURATION

   Parameters:
   - temperature: 0.0-1.0 (creativity)
   - top_p: Nucleus sampling
   - top_k: Top-k sampling
   - max_output_tokens: Response length
   - candidate_count: Number of responses

4. CONVERSATION HANDLING

   Start chat:
   chat = model.start_chat(history=[])
   
   Send messages:
   response = chat.send_message(message)
   
   Access history:
   for msg in chat.history:
       print(msg.role, msg.parts[0].text)

5. STREAMING RESPONSES

   Enable streaming:
   response = model.generate_content(prompt, stream=True)
   
   Process chunks:
   for chunk in response:
       print(chunk.text, end='')

6. SAFETY SETTINGS

   Categories:
   - HARM_CATEGORY_HARASSMENT
   - HARM_CATEGORY_HATE_SPEECH
   - HARM_CATEGORY_SEXUALLY_EXPLICIT
   - HARM_CATEGORY_DANGEROUS_CONTENT
   
   Thresholds:
   - BLOCK_NONE
   - BLOCK_LOW_AND_ABOVE
   - BLOCK_MEDIUM_AND_ABOVE
   - BLOCK_HIGH_AND_ABOVE

7. TOKEN COUNTING

   Count tokens:
   token_count = model.count_tokens(text)
   print(token_count.total_tokens)
   
   Important for:
   - Cost estimation
   - Context window management
   - Rate limiting

8. ERROR HANDLING

   Common errors:
   - Invalid API key
   - Rate limit exceeded
   - Content filtered by safety
   - Token limit exceeded
   
   Best practices:
   - Validate input
   - Handle exceptions
   - Implement retries
   - Log errors

9. BEST PRACTICES

   ✅ Use environment variables for API keys
   ✅ Implement error handling
   ✅ Count tokens for cost control
   ✅ Use streaming for long responses
   ✅ Configure safety settings
   ✅ Cache responses when possible
   ✅ Monitor API usage
   
   ❌ Don't hardcode API keys
   ❌ Don't ignore rate limits
   ❌ Don't skip error handling
   ❌ Don't send sensitive data

10. COST OPTIMIZATION

    Tips:
    - Use lower temperature for deterministic tasks
    - Limit max_output_tokens
    - Cache common responses
    - Batch requests when possible
    - Monitor token usage

11. TESTING

    Test your integration:
    python integrations/gemini_integration.py
    
    Verify:
    - API key works
    - Models accessible
    - Responses generated
    - Streaming works
    - Error handling works

12. PRODUCTION CHECKLIST

    ✅ API key in environment variables
    ✅ Error handling implemented
    ✅ Rate limiting configured
    ✅ Logging enabled
    ✅ Token counting active
    ✅ Safety settings configured
    ✅ Monitoring in place
    ✅ Costs tracked
"""
