# Callbacks in ADK

> **Implementing event-driven and asynchronous operations with callbacks**

Callbacks are essential for building responsive AI systems that can handle asynchronous operations, real-time events, and complex interaction patterns.

---

## 🎯 What are Callbacks?

### Definition
A **Callback** in Google ADK is a function or method that:
- **Triggers Automatically**: Called in response to specific events
- **Handles Asynchronous Operations**: Manages long-running tasks
- **Enables Event-Driven Architecture**: Responds to system events
- **Provides Notifications**: Informs about status changes
- **Supports Custom Logic**: Allows user-defined behavior

### Callback Architecture
```
┌─────────────────────────────────────────────────────────┐
│                Callback System                    │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Event       │────────►│   Callback Manager  │
│   Source     │         │   (Registration)     │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Callback Queue    │
│  (Event Processing)  │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Callback         │
                         │   Execution        │
│  (Function Calls)    │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Result           │
                         │   Handling         │
│  (Response Processing)│
                         └──────────────────────┘
```

---

## 🔄 Callback Types

### 1. **Event Callbacks**
Respond to system events

```python
from google_adk import CallbackManager, EventCallback

class EventCallbacks:
    def __init__(self):
        self.callback_manager = CallbackManager()
        self.setup_event_callbacks()
    
    def setup_event_callbacks(self):
        """Setup event-based callbacks"""
        
        # Agent started callback
        self.callback_manager.register_callback(
            event_type="agent_started",
            callback=self.on_agent_started,
            priority=1
        )
        
        # Agent completed callback
        self.callback_manager.register_callback(
            event_type="agent_completed",
            callback=self.on_agent_completed,
            priority=2
        )
        
        # Error callback
        self.callback_manager.register_callback(
            event_type="agent_error",
            callback=self.on_agent_error,
            priority=0  # High priority
        )
        
        # Tool executed callback
        self.callback_manager.register_callback(
            event_type="tool_executed",
            callback=self.on_tool_executed,
            priority=3
        )
    
    def on_agent_started(self, event_data: dict):
        """Handle agent started event"""
        
        agent_name = event_data.get("agent_name")
        start_time = event_data.get("start_time")
        
        print(f"🚀 Agent '{agent_name}' started at {start_time}")
        
        # Log to monitoring system
        self.log_event("agent_started", {
            "agent_name": agent_name,
            "start_time": start_time
        })
        
        # Send notification if needed
        if self.should_notify(agent_name):
            self.send_notification(f"Agent {agent_name} has started")
    
    def on_agent_completed(self, event_data: dict):
        """Handle agent completed event"""
        
        agent_name = event_data.get("agent_name")
        duration = event_data.get("duration")
        result = event_data.get("result")
        
        print(f"✅ Agent '{agent_name}' completed in {duration:.2f}s")
        
        # Update performance metrics
        self.update_performance_metrics(agent_name, duration, result)
        
        # Trigger next workflow step if applicable
        if self.is_part_of_workflow(event_data):
            self.trigger_next_step(event_data)
    
    def on_agent_error(self, event_data: dict):
        """Handle agent error event"""
        
        agent_name = event_data.get("agent_name")
        error = event_data.get("error")
        context = event_data.get("context", {})
        
        print(f"❌ Agent '{agent_name}' encountered error: {error}")
        
        # Log error with context
        self.log_error("agent_error", {
            "agent_name": agent_name,
            "error": str(error),
            "context": context,
            "timestamp": time.time()
        })
        
        # Attempt error recovery
        self.attempt_error_recovery(event_data)
    
    def on_tool_executed(self, event_data: dict):
        """Handle tool executed event"""
        
        tool_name = event_data.get("tool_name")
        agent_name = event_data.get("agent_name")
        execution_time = event_data.get("execution_time")
        result = event_data.get("result")
        
        print(f"🔧 Tool '{tool_name}' executed by '{agent_name}' in {execution_time:.3f}s")
        
        # Track tool usage
        self.track_tool_usage(tool_name, agent_name, execution_time, result)
        
        # Update tool performance metrics
        self.update_tool_metrics(tool_name, execution_time, result)

# Usage
event_callbacks = EventCallbacks()

# Trigger events (these would be called by ADK internally)
# event_callbacks.callback_manager.trigger_event("agent_started", {
#     "agent_name": "research_agent",
#     "start_time": datetime.now()
# })
```

### 2. **Async Callbacks**
Handle asynchronous operations

```python
import asyncio
from google_adk import AsyncCallback, AsyncCallbackManager

class AsyncCallbacks:
    def __init__(self):
        self.async_manager = AsyncCallbackManager()
        self.setup_async_callbacks()
    
    def setup_async_callbacks(self):
        """Setup asynchronous callbacks"""
        
        # Long-running task callback
        self.async_manager.register_async_callback(
            name="long_running_task",
            callback=self.handle_long_running_task,
            timeout=300  # 5 minutes
        )
        
        # Stream processing callback
        self.async_manager.register_async_callback(
            name="stream_processing",
            callback=self.handle_stream_processing,
            stream=True
        )
        
        # Batch processing callback
        self.async_manager.register_async_callback(
            name="batch_processing",
            callback=self.handle_batch_processing,
            batch_size=100
        )
    
    async def handle_long_running_task(self, task_data: dict) -> dict:
        """Handle long-running asynchronous task"""
        
        task_id = task_data.get("task_id")
        task_type = task_data.get("task_type")
        
        print(f"🔄 Starting long-running task: {task_type} (ID: {task_id})")
        
        try:
            # Simulate long-running operation
            if task_type == "data_analysis":
                result = await self.perform_data_analysis(task_data)
            elif task_type == "report_generation":
                result = await self.generate_report(task_data)
            else:
                result = await self.default_async_operation(task_data)
            
            print(f"✅ Task {task_id} completed successfully")
            return {
                "task_id": task_id,
                "status": "completed",
                "result": result,
                "completion_time": datetime.now()
            }
            
        except Exception as e:
            print(f"❌ Task {task_id} failed: {e}")
            return {
                "task_id": task_id,
                "status": "failed",
                "error": str(e),
                "completion_time": datetime.now()
            }
    
    async def handle_stream_processing(self, stream_data: dict):
        """Handle streaming data processing"""
        
        stream_id = stream_data.get("stream_id")
        data_chunk = stream_data.get("data")
        
        print(f"📊 Processing stream {stream_id}: {len(data_chunk)} bytes")
        
        # Process chunk
        processed_chunk = await self.process_data_chunk(data_chunk)
        
        # Send progress update
        await self.send_stream_update(stream_id, {
            "chunk_processed": True,
            "processed_size": len(processed_chunk),
            "timestamp": time.time()
        })
        
        return processed_chunk
    
    async def handle_batch_processing(self, batch_data: list) -> list:
        """Handle batch processing of multiple items"""
        
        batch_id = batch_data.get("batch_id")
        items = batch_data.get("items", [])
        
        print(f"📦 Processing batch {batch_id}: {len(items)} items")
        
        results = []
        
        # Process items concurrently
        semaphore = asyncio.Semaphore(10)  # Limit concurrent operations
        
        async def process_item(item):
            async with semaphore:
                return await self.process_single_item(item)
        
        # Create tasks for all items
        tasks = [process_item(item) for item in items]
        
        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter successful results
        successful_results = [r for r in results if not isinstance(r, Exception)]
        
        print(f"✅ Batch {batch_id} completed: {len(successful_results)}/{len(items)} successful")
        
        return successful_results
    
    async def perform_data_analysis(self, task_data: dict) -> dict:
        """Perform asynchronous data analysis"""
        
        # Simulate time-consuming analysis
        await asyncio.sleep(2)  # 2 second delay
        
        # Perform actual analysis
        data = task_data.get("data", [])
        analysis_result = {
            "total_records": len(data),
            "analysis_type": "statistical",
            "summary": self.generate_summary(data),
            "insights": self.extract_insights(data)
        }
        
        return analysis_result
    
    async def generate_report(self, task_data: dict) -> dict:
        """Generate report asynchronously"""
        
        report_config = task_data.get("config", {})
        
        # Simulate report generation time
        await asyncio.sleep(3)
        
        report = {
            "title": report_config.get("title", "Generated Report"),
            "content": self.generate_report_content(task_data),
            "format": report_config.get("format", "pdf"),
            "generated_at": datetime.now()
        }
        
        return report

# Usage
async_callbacks = AsyncCallbacks()

# Execute async tasks
async def main():
    # Start long-running task
    task_result = await async_callbacks.async_manager.execute_async(
        "long_running_task",
        {
            "task_id": "task_001",
            "task_type": "data_analysis",
            "data": [1, 2, 3, 4, 5]
        }
    )
    
    print(f"Task result: {task_result}")

# Run async operations
# asyncio.run(main())
```

### 3. **Progress Callbacks**
Monitor and report progress

```python
from google_adk import ProgressCallback, ProgressTracker

class ProgressCallbacks:
    def __init__(self):
        self.progress_tracker = ProgressTracker()
        self.setup_progress_callbacks()
    
    def setup_progress_callbacks(self):
        """Setup progress monitoring callbacks"""
        
        # Task progress callback
        self.progress_tracker.register_progress_callback(
            task_type="agent_execution",
            callback=self.on_agent_progress,
            update_interval=1.0  # Update every 1 second
        )
        
        # Workflow progress callback
        self.progress_tracker.register_progress_callback(
            task_type="workflow_execution",
            callback=self.on_workflow_progress,
            update_interval=2.0
        )
        
        # File processing progress callback
        self.progress_tracker.register_progress_callback(
            task_type="file_processing",
            callback=self.on_file_progress,
            update_interval=0.5
        )
    
    def on_agent_progress(self, progress_data: dict):
        """Handle agent execution progress"""
        
        agent_name = progress_data.get("agent_name")
        current_step = progress_data.get("current_step")
        total_steps = progress_data.get("total_steps")
        percentage = progress_data.get("percentage", 0)
        elapsed_time = progress_data.get("elapsed_time")
        
        # Create progress bar
        progress_bar = self.create_progress_bar(percentage, width=30)
        
        print(f"🤖 {agent_name}: [{progress_bar}] {percentage:.1f}% - Step {current_step}/{total_steps} ({elapsed_time:.1f}s)")
        
        # Send progress update to UI
        self.update_ui_progress(agent_name, {
            "percentage": percentage,
            "current_step": current_step,
            "total_steps": total_steps,
            "elapsed_time": elapsed_time
        })
        
        # Check for progress milestones
        self.check_progress_milestones(agent_name, percentage)
    
    def on_workflow_progress(self, progress_data: dict):
        """Handle workflow execution progress"""
        
        workflow_name = progress_data.get("workflow_name")
        current_stage = progress_data.get("current_stage")
        total_stages = progress_data.get("total_stages")
        stage_progress = progress_data.get("stage_progress", 0)
        
        print(f"⚙️ Workflow '{workflow_name}': Stage {current_stage}/{total_stages} ({stage_progress:.1f}%)")
        
        # Update workflow dashboard
        self.update_workflow_dashboard(workflow_name, {
            "current_stage": current_stage,
            "total_stages": total_stages,
            "stage_progress": stage_progress
        })
    
    def on_file_progress(self, progress_data: dict):
        """Handle file processing progress"""
        
        file_name = progress_data.get("file_name")
        bytes_processed = progress_data.get("bytes_processed")
        total_bytes = progress_data.get("total_bytes")
        processing_rate = progress_data.get("processing_rate", 0)
        
        percentage = (bytes_processed / total_bytes) * 100 if total_bytes > 0 else 0
        
        # Format file size
        processed_mb = bytes_processed / (1024 * 1024)
        total_mb = total_bytes / (1024 * 1024)
        
        print(f"📁 {file_name}: {processed_mb:.1f}/{total_mb:.1f} MB ({percentage:.1f}%) - {processing_rate:.1f} MB/s")
        
        # Update file progress UI
        self.update_file_progress(file_name, {
            "bytes_processed": bytes_processed,
            "total_bytes": total_bytes,
            "percentage": percentage,
            "processing_rate": processing_rate
        })
    
    def create_progress_bar(self, percentage: float, width: int = 30) -> str:
        """Create ASCII progress bar"""
        
        filled = int((percentage / 100) * width)
        bar = "█" * filled + "░" * (width - filled)
        return bar
    
    def check_progress_milestones(self, agent_name: str, percentage: float):
        """Check and notify on progress milestones"""
        
        milestones = [25, 50, 75, 90, 100]
        
        for milestone in milestones:
            if percentage >= milestone and not self.is_milestone_notified(agent_name, milestone):
                self.notify_milestone(agent_name, milestone)
                self.mark_milestone_notified(agent_name, milestone)

# Usage
progress_callbacks = ProgressCallbacks()

# Simulate progress updates
def simulate_agent_progress():
    """Simulate agent execution with progress callbacks"""
    
    agent_name = "research_agent"
    total_steps = 5
    
    for step in range(1, total_steps + 1):
        # Calculate progress
        percentage = (step / total_steps) * 100
        elapsed_time = step * 2.5  # Simulate 2.5 seconds per step
        
        # Trigger progress callback
        progress_callbacks.progress_tracker.trigger_progress(
            task_type="agent_execution",
            progress_data={
                "agent_name": agent_name,
                "current_step": step,
                "total_steps": total_steps,
                "percentage": percentage,
                "elapsed_time": elapsed_time
            }
        )
        
        time.sleep(0.5)  # Simulate processing time

# Run progress simulation
# simulate_agent_progress()
```

### 4. **Result Callbacks**
Handle operation results

```python
from google_adk import ResultCallback, ResultProcessor

class ResultCallbacks:
    def __init__(self):
        self.result_processor = ResultProcessor()
        self.setup_result_callbacks()
    
    def setup_result_callbacks(self):
        """Setup result handling callbacks"""
        
        # Success callback
        self.result_processor.register_result_callback(
            result_type="success",
            callback=self.on_success_result,
            priority=1
        )
        
        # Error callback
        self.result_processor.register_result_callback(
            result_type="error",
            callback=self.on_error_result,
            priority=0  # High priority for errors
        )
        
        # Partial result callback
        self.result_processor.register_result_callback(
            result_type="partial",
            callback=self.on_partial_result,
            priority=2
        )
        
        # Timeout callback
        self.result_processor.register_result_callback(
            result_type="timeout",
            callback=self.on_timeout_result,
            priority=3
        )
    
    def on_success_result(self, result_data: dict):
        """Handle successful operation result"""
        
        operation_id = result_data.get("operation_id")
        result = result_data.get("result")
        execution_time = result_data.get("execution_time")
        
        print(f"✅ Operation {operation_id} completed successfully in {execution_time:.2f}s")
        
        # Process successful result
        processed_result = self.process_successful_result(result)
        
        # Store result
        self.store_result(operation_id, {
            "status": "success",
            "result": processed_result,
            "timestamp": datetime.now()
        })
        
        # Trigger success callbacks
        self.trigger_success_callbacks(operation_id, processed_result)
    
    def on_error_result(self, result_data: dict):
        """Handle operation error result"""
        
        operation_id = result_data.get("operation_id")
        error = result_data.get("error")
        error_type = result_data.get("error_type", "unknown")
        context = result_data.get("context", {})
        
        print(f"❌ Operation {operation_id} failed: {error}")
        
        # Log error with context
        self.log_operation_error(operation_id, error, error_type, context)
        
        # Attempt error recovery
        recovery_result = self.attempt_error_recovery(result_data)
        
        if recovery_result:
            print(f"🔄 Error recovery successful for operation {operation_id}")
        else:
            # Store error result
            self.store_result(operation_id, {
                "status": "error",
                "error": str(error),
                "error_type": error_type,
                "context": context,
                "timestamp": datetime.now()
            })
    
    def on_partial_result(self, result_data: dict):
        """Handle partial operation result"""
        
        operation_id = result_data.get("operation_id")
        partial_result = result_data.get("result")
        progress_percentage = result_data.get("progress_percentage", 0)
        
        print(f"📊 Operation {operation_id} partial result: {progress_percentage:.1f}% complete")
        
        # Store partial result
        self.store_partial_result(operation_id, {
            "partial_result": partial_result,
            "progress_percentage": progress_percentage,
            "timestamp": datetime.now()
        })
        
        # Update progress tracking
        self.update_operation_progress(operation_id, progress_percentage)
    
    def on_timeout_result(self, result_data: dict):
        """Handle operation timeout"""
        
        operation_id = result_data.get("operation_id")
        timeout_duration = result_data.get("timeout_duration")
        last_known_state = result_data.get("last_known_state")
        
        print(f"⏰ Operation {operation_id} timed out after {timeout_duration}s")
        
        # Handle timeout
        timeout_result = self.handle_operation_timeout(result_data)
        
        # Store timeout result
        self.store_result(operation_id, {
            "status": "timeout",
            "timeout_duration": timeout_duration,
            "last_known_state": last_known_state,
            "timeout_result": timeout_result,
            "timestamp": datetime.now()
        })
    
    def process_successful_result(self, result: dict) -> dict:
        """Process and format successful result"""
        
        # Validate result structure
        if not isinstance(result, dict):
            return {"error": "Invalid result format"}
        
        # Add processing metadata
        processed_result = {
            "data": result,
            "processed_at": datetime.now(),
            "processor": "ResultCallbacks",
            "validation": "passed"
        }
        
        # Apply result transformations if configured
        if self.should_transform_result(result):
            processed_result["data"] = self.transform_result(result)
        
        return processed_result
    
    def attempt_error_recovery(self, error_data: dict) -> dict:
        """Attempt to recover from error"""
        
        error_type = error_data.get("error_type")
        
        # Define recovery strategies
        recovery_strategies = {
            "timeout": self.retry_with_longer_timeout,
            "network_error": self.retry_with_different_endpoint,
            "validation_error": self.retry_with_corrected_data,
            "permission_error": self.retry_with_different_credentials
        }
        
        recovery_function = recovery_strategies.get(error_type)
        
        if recovery_function:
            try:
                return recovery_function(error_data)
            except Exception as e:
                print(f"Recovery attempt failed: {e}")
                return None
        
        return None

# Usage
result_callbacks = ResultCallbacks()

# Simulate operation results
def simulate_operation_results():
    """Simulate various operation results"""
    
    # Success result
    result_callbacks.result_processor.trigger_result(
        result_type="success",
        result_data={
            "operation_id": "op_001",
            "result": {"status": "completed", "data": [1, 2, 3]},
            "execution_time": 2.5
        }
    )
    
    # Error result
    result_callbacks.result_processor.trigger_result(
        result_type="error",
        result_data={
            "operation_id": "op_002",
            "error": "Connection timeout",
            "error_type": "timeout",
            "context": {"endpoint": "api.example.com"}
        }
    )
    
    # Partial result
    result_callbacks.result_processor.trigger_result(
        result_type="partial",
        result_data={
            "operation_id": "op_003",
            "result": {"partial_data": [1, 2]},
            "progress_percentage": 60
        }
    )

# Run result simulation
# simulate_operation_results()
```

---

## 🔧 Callback Configuration

### 1. **Callback Registration**
Register callbacks with different configurations

```python
from google_adk import CallbackRegistry, CallbackConfig

class CallbackConfiguration:
    def __init__(self):
        self.registry = CallbackRegistry()
        self.setup_configured_callbacks()
    
    def setup_configured_callbacks(self):
        """Setup callbacks with different configurations"""
        
        # High-priority error callback
        self.registry.register_callback(
            name="critical_error_handler",
            callback=self.handle_critical_error,
            config=CallbackConfig(
                priority=0,  # Highest priority
                async_execution=False,
                retry_count=3,
                timeout=30,
                condition=lambda data: data.get("severity") == "critical"
            )
        )
        
        # Async progress callback
        self.registry.register_callback(
            name="async_progress_tracker",
            callback=self.track_progress_async,
            config=CallbackConfig(
                priority=5,
                async_execution=True,
                retry_count=0,
                timeout=None,
                condition=lambda data: "progress" in data
            )
        )
        
        # Conditional success callback
        self.registry.register_callback(
            name="conditional_success_handler",
            callback=self.handle_conditional_success,
            config=CallbackConfig(
                priority=3,
                async_execution=False,
                retry_count=1,
                timeout=10,
                condition=lambda data: (
                    data.get("result_type") == "success" and
                    data.get("result", {}).get("important", False)
                )
            )
        )
    
    def handle_critical_error(self, error_data: dict):
        """Handle critical errors with special processing"""
        
        error_id = error_data.get("error_id")
        error_message = error_data.get("error")
        
        print(f"🚨 CRITICAL ERROR: {error_id} - {error_message}")
        
        # Immediate notification
        self.send_critical_alert(error_id, error_message)
        
        # Attempt immediate recovery
        self.emergency_recovery_procedure(error_data)
        
        # Log to critical error system
        self.log_critical_error(error_data)
    
    async def track_progress_async(self, progress_data: dict):
        """Track progress asynchronously"""
        
        # Update progress database
        await self.update_progress_database(progress_data)
        
        # Send real-time updates
        await self.send_real_time_updates(progress_data)
        
        # Check for alerts
        await self.check_progress_alerts(progress_data)
    
    def handle_conditional_success(self, success_data: dict):
        """Handle important success results"""
        
        operation_id = success_data.get("operation_id")
        result = success_data.get("result")
        
        print(f"🎉 Important success: {operation_id}")
        
        # Special processing for important results
        self.process_important_result(result)
        
        # Notify stakeholders
        self.notify_stakeholders(operation_id, result)

# Usage
callback_config = CallbackConfiguration()

# Trigger callbacks with different data
# callback_config.registry.trigger_callback("critical_error_handler", {
#     "error_id": "ERR_001",
#     "error": "Database connection failed",
#     "severity": "critical"
# })
```

### 2. **Callback Chaining**
Chain multiple callbacks together

```python
class CallbackChain:
    def __init__(self):
        self.chains = {}
    
    def create_chain(self, chain_name: str, callbacks: list):
        """Create a callback chain"""
        
        self.chains[chain_name] = callbacks
    
    def execute_chain(self, chain_name: str, data: dict) -> dict:
        """Execute callback chain"""
        
        if chain_name not in self.chains:
            raise ValueError(f"Chain {chain_name} not found")
        
        chain_data = data.copy()
        chain_results = []
        
        for i, callback in enumerate(self.chains[chain_name]):
            try:
                # Execute callback
                result = callback(chain_data)
                
                chain_results.append({
                    "step": i,
                    "callback_name": callback.__name__,
                    "result": result,
                    "status": "success"
                })
                
                # Update data for next callback
                if isinstance(result, dict):
                    chain_data.update(result)
                
            except Exception as e:
                chain_results.append({
                    "step": i,
                    "callback_name": callback.__name__,
                    "error": str(e),
                    "status": "failed"
                })
                
                # Decide whether to continue chain
                if self.should_stop_chain_on_error(e):
                    break
        
        return {
            "chain_name": chain_name,
            "total_steps": len(self.chains[chain_name]),
            "results": chain_results,
            "final_data": chain_data
        }
    
    def should_stop_chain_on_error(self, error: Exception) -> bool:
        """Determine if chain should stop on error"""
        
        # Stop on critical errors
        if "critical" in str(error).lower():
            return True
        
        # Continue on non-critical errors
        return False

# Define callback chain functions
def validate_input(data: dict) -> dict:
    """Validate input data"""
    
    if "input" not in data:
        raise ValueError("Missing input field")
    
    input_value = data["input"]
    
    if not isinstance(input_value, str):
        raise ValueError("Input must be string")
    
    return {"validation_status": "passed", "validated_input": input_value}

def process_data(data: dict) -> dict:
    """Process validated data"""
    
    validated_input = data.get("validated_input")
    
    # Simulate processing
    processed = validated_input.upper()
    
    return {"processed_data": processed, "processing_time": 0.5}

def store_result(data: dict) -> dict:
    """Store processed result"""
    
    processed_data = data.get("processed_data")
    
    # Simulate storage
    storage_id = f"result_{int(time.time())}"
    
    return {
        "storage_id": storage_id,
        "stored_data": processed_data,
        "storage_status": "success"
    }

def send_notification(data: dict) -> dict:
    """Send notification about stored result"""
    
    storage_id = data.get("storage_id")
    
    # Simulate notification
    notification_sent = True
    
    return {
        "notification_sent": notification_sent,
        "notification_target": "admin",
        "notification_message": f"Result stored with ID: {storage_id}"
    }

# Create and use callback chain
chain = CallbackChain()
chain.create_chain("data_processing_chain", [
    validate_input,
    process_data,
    store_result,
    send_notification
])

# Execute chain
chain_result = chain.execute_chain("data_processing_chain", {
    "input": "hello world"
})
```

---

## 📊 Callback Monitoring

### 1. **Performance Monitoring**
Track callback performance

```python
class CallbackMonitor:
    def __init__(self):
        self.metrics = {}
        self.active_callbacks = {}
    
    def start_monitoring(self, callback_name: str):
        """Start monitoring callback execution"""
        
        self.active_callbacks[callback_name] = {
            "start_time": time.time(),
            "status": "running"
        }
    
    def end_monitoring(self, callback_name: str, success: bool, error: str = None):
        """End monitoring callback execution"""
        
        if callback_name in self.active_callbacks:
            callback_info = self.active_callbacks[callback_name]
            
            end_time = time.time()
            duration = end_time - callback_info["start_time"]
            
            # Update metrics
            if callback_name not in self.metrics:
                self.metrics[callback_name] = {
                    "total_calls": 0,
                    "successful_calls": 0,
                    "failed_calls": 0,
                    "total_duration": 0,
                    "avg_duration": 0,
                    "errors": []
                }
            
            metrics = self.metrics[callback_name]
            metrics["total_calls"] += 1
            metrics["total_duration"] += duration
            
            if success:
                metrics["successful_calls"] += 1
            else:
                metrics["failed_calls"] += 1
                if error:
                    metrics["errors"].append({
                        "error": error,
                        "timestamp": end_time
                    })
            
            metrics["avg_duration"] = metrics["total_duration"] / metrics["total_calls"]
            
            # Remove from active callbacks
            del self.active_callbacks[callback_name]
    
    def get_callback_metrics(self, callback_name: str) -> dict:
        """Get performance metrics for callback"""
        
        return self.metrics.get(callback_name, {})
    
    def get_all_metrics(self) -> dict:
        """Get all callback metrics"""
        
        return self.metrics

# Usage
monitor = CallbackMonitor()

# Decorator for monitoring callbacks
def monitored_callback(callback_name: str):
    """Decorator to monitor callback execution"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            monitor.start_monitoring(callback_name)
            
            try:
                result = func(*args, **kwargs)
                monitor.end_monitoring(callback_name, True)
                return result
            except Exception as e:
                monitor.end_monitoring(callback_name, False, str(e))
                raise
        
        return wrapper
    return decorator

# Apply monitoring to callbacks
@monitored_callback("data_validation")
def validate_data_with_monitoring(data: dict) -> dict:
    """Validated data with monitoring"""
    
    # Validation logic
    if "data" not in data:
        raise ValueError("Missing data field")
    
    return {"validation_status": "passed"}

# Get metrics
metrics = monitor.get_callback_metrics("data_validation")
print(f"Callback metrics: {metrics}")
```

---

## 🎯 Best Practices

### 1. **Callback Design**
- **Single Responsibility**: Each callback should do one thing well
- **Error Handling**: Handle errors gracefully
- **Idempotency**: Safe to call multiple times
- **Documentation**: Clear documentation for parameters

### 2. **Performance**
- **Async Operations**: Use async for long-running callbacks
- **Timeout Handling**: Set appropriate timeouts
- **Resource Management**: Clean up resources properly
- **Batch Processing**: Process multiple items efficiently

### 3. **Reliability**
- **Retry Logic**: Implement retry mechanisms
- **Circuit Breakers**: Prevent cascade failures
- **Logging**: Comprehensive logging for debugging
- **Monitoring**: Track callback performance

### 4. **Security**
- **Input Validation**: Validate all callback inputs
- **Permission Checks**: Verify callback permissions
- **Rate Limiting**: Prevent callback abuse
- **Audit Logging**: Log all callback executions

---

## 📚 Next Steps

1. **Learn MCP Integration** → `10-mcp-with-adk.md`
2. **Build Callback Systems** → Implement callback architectures
3. **Master Async Patterns** → Create asynchronous systems
4. **Deploy to Production** → Scale callback-based applications

---

**🔄 Master callbacks for responsive AI systems!**
