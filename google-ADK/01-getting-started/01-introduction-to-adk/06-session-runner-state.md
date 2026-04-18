# Session Runner & State Management

> **Managing agent sessions and state for persistent interactions**

Session management is crucial for building conversational AI systems that maintain context across multiple interactions. Google ADK provides robust session management capabilities.

---

## 🎯 What is Session Management?

### Definition
**Session Management** in Google ADK refers to the system that:
- **Tracks Conversations**: Maintains conversation history
- **Preserves State**: Saves agent state between interactions
- **Manages Context**: Provides relevant context for responses
- **Handles Persistence**: Stores sessions across restarts
- **Enables Continuity**: Seamlessly continues conversations

### Session Components
```
┌─────────────────────────────────────────────────────────┐
│                Session Manager                        │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Session     │────────►│   Session Store      │
│   Creation   │         │   (Database/Memory)  │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   State Manager     │
                         │  - Agent State     │
                         │  - Context State   │
                         │  - Memory State    │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Session Runner    │
                         │  - Execution       │
                         │  - State Updates   │
                         │  - Event Handling  │
                         └──────────────────────┘
```

---

## 🔄 Session Lifecycle

### 1. **Session Creation**
Initialize new session with unique identifier

```python
from google_adk import SessionManager, Session

# Create session manager
session_manager = SessionManager(
    store_type="memory",  # or "database", "file"
    session_timeout=3600,  # 1 hour timeout
    max_sessions=1000
)

# Create new session
session = session_manager.create_session(
    user_id="user123",
    agent_name="customer_service",
    metadata={
        "source": "web",
        "language": "en",
        "timezone": "UTC"
    }
)

print(f"Session created: {session.session_id}")
print(f"Expires at: {session.expires_at}")
```

### 2. **Session Execution**
Run agent within session context

```python
# Execute agent in session
def run_conversation(session_manager, session_id, user_input):
    """Run agent within session context"""
    
    # Get session
    session = session_manager.get_session(session_id)
    
    if not session:
        return {"error": "Session not found"}
    
    # Check if session is expired
    if session.is_expired():
        return {"error": "Session expired"}
    
    # Add user input to session
    session.add_message("user", user_input)
    
    # Get agent from session
    agent = session.get_agent()
    
    # Get conversation context
    context = session.get_context()
    
    # Run agent with context
    response = agent.run(user_input, context=context)
    
    # Add agent response to session
    session.add_message("agent", response)
    
    # Update session state
    session.update_state({
        "last_activity": time.time(),
        "message_count": session.get_message_count(),
        "current_topic": extract_topic(response)
    })
    
    # Save session
    session_manager.save_session(session)
    
    return {
        "response": response,
        "session_id": session_id,
        "message_count": session.get_message_count()
    }

# Usage
result = run_conversation(
    session_manager, 
    session.session_id, 
    "What are your business hours?"
)
```

### 3. **Session Persistence**
Save and restore sessions

```python
# Configure session persistence
persistent_manager = SessionManager(
    store_type="database",
    connection_string="postgresql://user:pass@localhost/adk_sessions",
    session_timeout=7200,  # 2 hours
    auto_save=True
)

# Save session to database
session_manager.save_session(session)

# Restore session from database
restored_session = session_manager.load_session(session.session_id)

# Export session data
session_data = session.export_to_dict()
with open(f"session_{session.session_id}.json", "w") as f:
    json.dump(session_data, f, indent=2)
```

---

## 🗄️ State Management

### 1. **Agent State**
Track agent-specific information

```python
from google_adk import StateManager

# Create state manager
state_manager = StateManager()

# Define agent state schema
agent_state_schema = {
    "current_task": {
        "type": "string",
        "default": None
    },
    "task_progress": {
        "type": "float",
        "default": 0.0,
        "min": 0.0,
        "max": 1.0
    },
    "active_tools": {
        "type": "list",
        "default": []
    },
    "error_count": {
        "type": "integer",
        "default": 0
    },
    "last_interaction": {
        "type": "datetime",
        "default": None
    }
}

# Initialize agent state
agent_state = state_manager.create_state(
    session_id=session.session_id,
    state_type="agent",
    schema=agent_state_schema
)

# Update agent state
agent_state.update({
    "current_task": "customer_inquiry",
    "task_progress": 0.5,
    "active_tools": ["search_knowledge_base", "order_lookup"],
    "last_interaction": datetime.now()
})
```

### 2. **Context State**
Manage conversation context

```python
# Context state schema
context_state_schema = {
    "user_profile": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "preferences": {"type": "object"},
            "history": {"type": "array"}
        }
    },
    "conversation_topic": {
        "type": "string",
        "default": "general"
    },
    "entities": {
        "type": "array",
        "default": []
    },
    "intent": {
        "type": "string",
        "default": "unknown"
    },
    "context_window": {
        "type": "array",
        "max_items": 10
    }
}

# Initialize context state
context_state = state_manager.create_state(
    session_id=session.session_id,
    state_type="context",
    schema=context_state_schema
)

# Update context from conversation
def update_context_from_message(context_state, message, sender):
    """Update context based on new message"""
    
    # Extract entities
    entities = extract_entities(message)
    context_state.set("entities", entities)
    
    # Detect intent
    intent = detect_intent(message)
    context_state.set("intent", intent)
    
    # Update conversation topic
    topic = detect_topic(message)
    context_state.set("conversation_topic", topic)
    
    # Add to context window
    context_window = context_state.get("context_window", [])
    context_window.append({
        "sender": sender,
        "message": message,
        "timestamp": datetime.now()
    })
    
    # Keep only last N messages
    if len(context_window) > 10:
        context_window = context_window[-10:]
    
    context_state.set("context_window", context_window)
```

### 3. **Memory State**
Handle memory-related state

```python
# Memory state schema
memory_state_schema = {
    "working_memory": {
        "type": "array",
        "default": [],
        "max_items": 50
    },
    "episodic_memory": {
        "type": "array",
        "default": []
    },
    "semantic_memory": {
        "type": "object",
        "default": {}
    },
    "memory_summary": {
        "type": "string",
        "default": ""
    }
}

# Initialize memory state
memory_state = state_manager.create_state(
    session_id=session.session_id,
    state_type="memory",
    schema=memory_state_schema
)

# Update memory state
def update_memory_state(memory_state, input_text, response_text):
    """Update memory state with new interaction"""
    
    # Add to working memory
    working_memory = memory_state.get("working_memory", [])
    working_memory.append({
        "input": input_text,
        "response": response_text,
        "timestamp": datetime.now()
    })
    
    # Limit working memory size
    if len(working_memory) > 50:
        working_memory = working_memory[-50:]
    
    memory_state.set("working_memory", working_memory)
    
    # Add to episodic memory
    episodic_memory = memory_state.get("episodic_memory", [])
    episodic_memory.append({
        "interaction": {
            "user": input_text,
            "agent": response_text
        },
        "timestamp": datetime.now(),
        "summary": generate_summary(input_text, response_text)
    })
    
    memory_state.set("episodic_memory", episodic_memory)
    
    # Update memory summary
    summary = generate_memory_summary(episodic_memory)
    memory_state.set("memory_summary", summary)
```

---

## 🏃‍♂️ Session Runner

### 1. **Basic Session Runner**
Simple session execution loop

```python
from google_adk import SessionRunner

class BasicSessionRunner:
    def __init__(self, session_manager, agent):
        self.session_manager = session_manager
        self.agent = agent
    
    def run_session(self, session_id, user_input):
        """Run agent within session"""
        
        # Get session
        session = self.session_manager.get_session(session_id)
        if not session:
            return {"error": "Session not found"}
        
        # Check session validity
        if session.is_expired():
            return {"error": "Session expired"}
        
        # Add user input to session
        session.add_message("user", user_input)
        
        # Get context
        context = session.get_context()
        
        # Run agent
        response = self.agent.run(user_input, context=context)
        
        # Add response to session
        session.add_message("agent", response)
        
        # Update session
        session.update_last_activity()
        
        # Save session
        self.session_manager.save_session(session)
        
        return {
            "response": response,
            "session_id": session_id,
            "message_count": session.get_message_count()
        }

# Usage
runner = BasicSessionRunner(session_manager, customer_service_agent)
result = runner.run_session(session.session_id, "Track my order #12345")
```

### 2. **Advanced Session Runner**
Enhanced with state management and error handling

```python
class AdvancedSessionRunner:
    def __init__(self, session_manager, agent_factory):
        self.session_manager = session_manager
        self.agent_factory = agent_factory  # Factory to create agents
        self.state_manager = StateManager()
    
    def run_session(self, session_id, user_input, config=None):
        """Advanced session execution with state management"""
        
        try:
            # Get or create session
            session = self.session_manager.get_session(session_id)
            if not session:
                session = self.session_manager.create_session(
                    user_id="anonymous",
                    agent_name="default",
                    session_id=session_id
                )
            
            # Get or create agent
            agent = session.get_agent()
            if not agent:
                agent = self.agent_factory.create_agent(config)
                session.set_agent(agent)
            
            # Get states
            agent_state = self.state_manager.get_state(session_id, "agent")
            context_state = self.state_manager.get_state(session_id, "context")
            memory_state = self.state_manager.get_state(session_id, "memory")
            
            # Process input
            processed_input = self.preprocess_input(user_input, context_state)
            
            # Update context state
            update_context_from_message(context_state, processed_input, "user")
            
            # Prepare agent context
            agent_context = {
                "agent_state": agent_state.to_dict() if agent_state else {},
                "context_state": context_state.to_dict() if context_state else {},
                "memory_state": memory_state.to_dict() if memory_state else {},
                "session_info": session.to_dict()
            }
            
            # Run agent
            response = agent.run(processed_input, context=agent_context)
            
            # Process response
            processed_response = self.postprocess_response(response, context_state)
            
            # Update states
            if agent_state:
                agent_state.update({
                    "last_interaction": datetime.now(),
                    "task_progress": calculate_task_progress(processed_response)
                })
            
            update_memory_state(memory_state, processed_input, processed_response)
            update_context_from_message(context_state, processed_response, "agent")
            
            # Save states
            self.state_manager.save_state(agent_state)
            self.state_manager.save_state(context_state)
            self.state_manager.save_state(memory_state)
            
            # Update session
            session.add_message("user", processed_input)
            session.add_message("agent", processed_response)
            session.update_last_activity()
            
            # Save session
            self.session_manager.save_session(session)
            
            return {
                "response": processed_response,
                "session_id": session_id,
                "states": {
                    "agent": agent_state.to_dict() if agent_state else None,
                    "context": context_state.to_dict() if context_state else None,
                    "memory": memory_state.to_dict() if memory_state else None
                },
                "session_info": {
                    "message_count": session.get_message_count(),
                    "duration": session.get_duration(),
                    "expires_at": session.expires_at
                }
            }
        
        except Exception as e:
            # Handle errors
            self.handle_session_error(session_id, e)
            return {
                "error": str(e),
                "session_id": session_id,
                "error_type": type(e).__name__
            }
    
    def preprocess_input(self, user_input, context_state):
        """Preprocess user input"""
        # Clean and validate input
        cleaned_input = clean_text(user_input)
        
        # Add context if available
        if context_state and context_state.get("conversation_topic"):
            cleaned_input = f"[Topic: {context_state.get('conversation_topic')}] {cleaned_input}"
        
        return cleaned_input
    
    def postprocess_response(self, response, context_state):
        """Postprocess agent response"""
        # Add personalization if available
        if context_state and context_state.get("user_profile", {}).get("name"):
            response = f"Hi {context_state['user_profile']['name']}, {response}"
        
        return response
    
    def handle_session_error(self, session_id, error):
        """Handle session errors"""
        # Log error
        logger.error(f"Session {session_id} error: {error}")
        
        # Update session state
        session = self.session_manager.get_session(session_id)
        if session:
            session.set_error(error)
            self.session_manager.save_session(session)
```

---

## 🔄 Session Events

### 1. **Event System**
Handle session lifecycle events

```python
from google_adk import SessionEventManager

class SessionEventHandler:
    def __init__(self):
        self.event_handlers = {}
    
    def register_handler(self, event_type, handler):
        """Register event handler"""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)
    
    def emit_event(self, event_type, session, data=None):
        """Emit session event"""
        handlers = self.event_handlers.get(event_type, [])
        for handler in handlers:
            try:
                handler(session, data)
            except Exception as e:
                logger.error(f"Event handler error: {e}")

# Create event handler
event_handler = SessionEventHandler()

# Register event handlers
@event_handler.register_handler("session_created")
def on_session_created(session, data):
    """Handle session creation"""
    logger.info(f"Session {session.session_id} created")
    
    # Initialize analytics
    analytics.track("session_created", {
        "session_id": session.session_id,
        "user_id": session.user_id,
        "agent_name": session.agent_name
    })

@event_handler.register_handler("session_expired")
def on_session_expired(session, data):
    """Handle session expiration"""
    logger.info(f"Session {session.session_id} expired")
    
    # Clean up resources
    cleanup_session_resources(session.session_id)
    
    # Notify user
    send_session_expiry_notification(session.user_id)

@event_handler.register_handler("message_added")
def on_message_added(session, data):
    """Handle new message"""
    message = data["message"]
    sender = data["sender"]
    
    # Update analytics
    analytics.track("message_added", {
        "session_id": session.session_id,
        "sender": sender,
        "message_length": len(message)
    })
    
    # Check for escalation triggers
    if should_escalate(message):
        trigger_escalation(session.session_id, message)
```

### 2. **Session Analytics**
Track session metrics

```python
class SessionAnalytics:
    def __init__(self):
        self.metrics = {}
    
    def track_session_metrics(self, session):
        """Track session performance metrics"""
        
        session_metrics = {
            "session_id": session.session_id,
            "duration": session.get_duration(),
            "message_count": session.get_message_count(),
            "agent_response_time": session.get_avg_response_time(),
            "error_count": session.get_error_count(),
            "user_satisfaction": session.get_satisfaction_score()
        }
        
        # Store metrics
        self.metrics[session.session_id] = session_metrics
        
        # Update aggregated metrics
        self.update_aggregated_metrics(session_metrics)
    
    def get_session_report(self, session_id):
        """Generate detailed session report"""
        metrics = self.metrics.get(session_id)
        if not metrics:
            return None
        
        return {
            "session_id": session_id,
            "performance": {
                "duration_minutes": metrics["duration"] / 60,
                "total_messages": metrics["message_count"],
                "avg_response_time": metrics["agent_response_time"],
                "error_rate": metrics["error_count"] / metrics["message_count"]
            },
            "quality": {
                "satisfaction_score": metrics["user_satisfaction"],
                "completion_rate": calculate_completion_rate(session_id),
                "escalation_rate": calculate_escalation_rate(session_id)
            },
            "recommendations": generate_recommendations(metrics)
        }
```

---

## 🛠️ Session Configuration

### 1. **Session Store Types**
Different storage backends for sessions

```python
# Memory store - for development/testing
memory_store = SessionStore(
    type="memory",
    max_sessions=100,
    cleanup_interval=300  # 5 minutes
)

# Database store - for production
database_store = SessionStore(
    type="postgresql",
    connection_string="postgresql://user:pass@localhost/adk_sessions",
    table_name="sessions",
    connection_pool_size=10
)

# Redis store - for distributed systems
redis_store = SessionStore(
    type="redis",
    host="localhost",
    port=6379,
    db=0,
    ttl=3600,  # 1 hour
    max_connections=20
)

# File store - for simple deployments
file_store = SessionStore(
    type="file",
    directory="/var/lib/adk/sessions",
    file_format="json",
    compression=True
)
```

### 2. **Session Policies**
Define session behavior rules

```python
# Session policies
session_policies = {
    "timeout": {
        "idle_timeout": 1800,      # 30 minutes idle
        "max_duration": 7200,      # 2 hours total
        "warning_time": 300         # 5 minutes before expiry
    },
    "limits": {
        "max_messages": 100,        # Max messages per session
        "max_memory_usage": "100MB", # Max memory per session
        "max_concurrent_sessions": 5  # Per user
    },
    "security": {
        "require_authentication": True,
        "session_encryption": True,
        "audit_logging": True
    },
    "cleanup": {
        "auto_cleanup": True,
        "cleanup_interval": 3600,   # 1 hour
        "retention_days": 30
    }
}

# Apply policies
session_manager = SessionManager(
    store=database_store,
    policies=session_policies
)
```

---

## 📊 Session Monitoring

### 1. **Real-time Monitoring**
Track active sessions

```python
class SessionMonitor:
    def __init__(self, session_manager):
        self.session_manager = session_manager
        self.metrics_collector = MetricsCollector()
    
    def start_monitoring(self):
        """Start real-time session monitoring"""
        
        while True:
            # Get current session stats
            stats = self.session_manager.get_stats()
            
            # Collect metrics
            self.metrics_collector.record("active_sessions", stats["active_count"])
            self.metrics_collector.record("total_sessions", stats["total_count"])
            self.metrics_collector.record("expired_sessions", stats["expired_count"])
            
            # Check for issues
            if stats["active_count"] > 1000:
                self.alert_high_load(stats)
            
            if stats["error_rate"] > 0.05:
                self.alert_high_error_rate(stats)
            
            # Sleep before next check
            time.sleep(60)  # Check every minute
    
    def alert_high_load(self, stats):
        """Alert on high session load"""
        send_alert(
            "High Session Load",
            f"Active sessions: {stats['active_count']}",
            severity="warning"
        )
    
    def alert_high_error_rate(self, stats):
        """Alert on high error rate"""
        send_alert(
            "High Session Error Rate",
            f"Error rate: {stats['error_rate']:.2%}",
            severity="critical"
        )
```

### 2. **Session Health Checks**
Validate session integrity

```python
def health_check_sessions(session_manager):
    """Perform health check on all sessions"""
    
    sessions = session_manager.get_all_sessions()
    health_report = {
        "total_sessions": len(sessions),
        "healthy_sessions": 0,
        "unhealthy_sessions": 0,
        "issues": []
    }
    
    for session in sessions:
        issues = []
        
        # Check session validity
        if session.is_expired():
            issues.append("Session expired")
        
        # Check state consistency
        if not session.state_is_consistent():
            issues.append("State inconsistency")
        
        # Check memory usage
        if session.get_memory_usage() > 100 * 1024 * 1024:  # 100MB
            issues.append("High memory usage")
        
        # Check message count
        if session.get_message_count() > 1000:
            issues.append("Too many messages")
        
        if issues:
            health_report["unhealthy_sessions"] += 1
            health_report["issues"].append({
                "session_id": session.session_id,
                "issues": issues
            })
        else:
            health_report["healthy_sessions"] += 1
    
    return health_report
```

---

## 🎯 Best Practices

### 1. **Session Design**
- **Short Sessions**: Keep sessions focused and purposeful
- **Clear State**: Maintain clean, predictable state
- **Efficient Storage**: Use appropriate storage backend
- **Regular Cleanup**: Remove expired sessions

### 2. **State Management**
- **Immutable Updates**: Create new state objects instead of modifying
- **State Validation**: Validate state before saving
- **Snapshotting**: Create state snapshots for recovery
- **Conflict Resolution**: Handle concurrent state updates

### 3. **Performance**
- **Lazy Loading**: Load sessions only when needed
- **Caching**: Cache frequently accessed sessions
- **Batch Operations**: Process multiple sessions together
- **Connection Pooling**: Reuse database connections

### 4. **Security**
- **Session Encryption**: Encrypt sensitive session data
- **Access Control**: Validate session access permissions
- **Audit Logging**: Track all session operations
- **Secure Storage**: Use secure storage backends

---

## 📚 Next Steps

1. **Learn Multi-Agent Systems** → `07-multi-agent-systems.md`
2. **Build Session Management** → Implement session runners
3. **Practice State Management** → Create custom state handlers
4. **Deploy Session Systems** → Set up production session management

---

**🔄 Master session management for persistent AI interactions!**
