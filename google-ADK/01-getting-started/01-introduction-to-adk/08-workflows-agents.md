# Workflows & Agents

> **Designing and implementing complex workflows with Google ADK**

Workflows are the backbone of sophisticated AI systems, enabling agents to execute complex, multi-step processes with conditional logic, parallel execution, and error recovery.

---

## 🎯 What are Workflows?

### Definition
A **Workflow** in Google ADK is a structured sequence of operations that:
- **Defines Process Flow**: Step-by-step execution logic
- **Handles Conditions**: Branches based on data and state
- **Manages Dependencies**: Coordinates task dependencies
- **Supports Parallelism**: Executes multiple tasks simultaneously
- **Provides Error Recovery**: Handles failures gracefully

### Workflow Components
```
┌─────────────────────────────────────────────────────────┐
│                   Workflow Engine                   │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Workflow   │────────►│   Task Scheduler    │
│   Definition │         │   (Queue & Priority) │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Condition        │
                         │   Evaluator        │
                         │  (Logic & Rules)    │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Agent            │
                         │   Executor         │
                         │  (Run Tasks)        │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   State Manager    │
                         │  (Track Progress)   │
                         └──────────────────────┘
```

---

## 🏗️ Workflow Types

### 1. **Sequential Workflows**
Execute tasks in linear order

```python
from google_adk import Workflow, WorkflowStep, Agent

class SequentialWorkflow(Workflow):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.steps = []
        self.current_step = 0
    
    def add_step(self, step: WorkflowStep):
        """Add step to workflow"""
        self.steps.append(step)
    
    def execute(self, initial_data: dict) -> dict:
        """Execute workflow sequentially"""
        
        workflow_data = initial_data.copy()
        results = {}
        
        for i, step in enumerate(self.steps):
            self.current_step = i
            
            try:
                # Check if step should execute
                if not self.should_execute_step(step, workflow_data):
                    results[f"step_{i}"] = {
                        "status": "skipped",
                        "reason": "Condition not met"
                    }
                    continue
                
                # Execute step
                step_result = self.execute_step(step, workflow_data)
                
                # Store result
                results[f"step_{i}"] = {
                    "status": "completed",
                    "result": step_result,
                    "step_name": step.name
                }
                
                # Update workflow data
                workflow_data.update(step_result)
                
                # Check for early termination
                if step.terminates_workflow:
                    break
                    
            except Exception as e:
                results[f"step_{i}"] = {
                    "status": "failed",
                    "error": str(e),
                    "step_name": step.name
                }
                
                # Handle error based on workflow policy
                if step.continue_on_error:
                    continue
                else:
                    break
        
        return {
            "workflow_name": self.name,
            "total_steps": len(self.steps),
            "executed_steps": self.current_step + 1,
            "results": results,
            "final_data": workflow_data
        }
    
    def should_execute_step(self, step: WorkflowStep, data: dict) -> bool:
        """Check if step should execute based on conditions"""
        
        if not step.condition:
            return True
        
        # Evaluate condition
        return self.evaluate_condition(step.condition, data)
    
    def execute_step(self, step: WorkflowStep, data: dict) -> dict:
        """Execute individual workflow step"""
        
        if step.agent:
            # Execute with agent
            return step.agent.run(step.task, **data)
        elif step.function:
            # Execute with function
            return step.function(data)
        else:
            raise ValueError("Step must have either agent or function")

# Define workflow steps
def create_research_workflow():
    """Create a sequential research workflow"""
    
    workflow = SequentialWorkflow("research_workflow")
    
    # Step 1: Research
    research_step = WorkflowStep(
        name="research",
        agent=research_agent,
        task="Research {topic}",
        condition=lambda data: "topic" in data,
        terminates_workflow=False,
        continue_on_error=False
    )
    
    # Step 2: Analysis
    analysis_step = WorkflowStep(
        name="analysis",
        agent=analysis_agent,
        task="Analyze research data",
        condition=lambda data: "research_result" in data,
        terminates_workflow=False,
        continue_on_error=True
    )
    
    # Step 3: Report Generation
    report_step = WorkflowStep(
        name="report",
        agent=writing_agent,
        task="Generate comprehensive report",
        condition=lambda data: "analysis_result" in data,
        terminates_workflow=True,
        continue_on_error=False
    )
    
    workflow.add_step(research_step)
    workflow.add_step(analysis_step)
    workflow.add_step(report_step)
    
    return workflow

# Execute workflow
workflow = create_research_workflow()
result = workflow.execute({
    "topic": "AI technology trends 2024"
})
```

### 2. **Parallel Workflows**
Execute multiple tasks simultaneously

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed

class ParallelWorkflow(Workflow):
    def __init__(self, name: str, max_workers: int = 5):
        super().__init__(name=name)
        self.parallel_steps = []
        self.max_workers = max_workers
    
    def add_parallel_step(self, step: WorkflowStep):
        """Add parallel step to workflow"""
        self.parallel_steps.append(step)
    
    def execute(self, initial_data: dict) -> dict:
        """Execute workflow steps in parallel"""
        
        workflow_data = initial_data.copy()
        results = {}
        
        # Filter steps that should execute
        executable_steps = [
            step for step in self.parallel_steps
            if self.should_execute_step(step, workflow_data)
        ]
        
        # Execute steps in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_step = {
                executor.submit(self.execute_step, step, workflow_data): step
                for step in executable_steps
            }
            
            # Collect results as they complete
            for future in as_completed(future_to_step):
                step = future_to_step[future]
                step_name = step.name
                
                try:
                    step_result = future.result()
                    results[step_name] = {
                        "status": "completed",
                        "result": step_result
                    }
                    
                    # Update workflow data
                    workflow_data[step_name] = step_result
                    
                except Exception as e:
                    results[step_name] = {
                        "status": "failed",
                        "error": str(e)
                    }
        
        return {
            "workflow_name": self.name,
            "total_steps": len(self.parallel_steps),
            "executed_steps": len(executable_steps),
            "results": results,
            "final_data": workflow_data
        }

# Define parallel workflow
def create_parallel_analysis_workflow():
    """Create a parallel analysis workflow"""
    
    workflow = ParallelWorkflow("parallel_analysis", max_workers=3)
    
    # Parallel Step 1: Market Research
    market_step = WorkflowStep(
        name="market_research",
        agent=research_agent,
        task="Research market trends",
        condition=lambda data: "market" in data
    )
    
    # Parallel Step 2: Competitor Analysis
    competitor_step = WorkflowStep(
        name="competitor_analysis",
        agent=analysis_agent,
        task="Analyze competitors",
        condition=lambda data: "competitors" in data
    )
    
    # Parallel Step 3: Customer Analysis
    customer_step = WorkflowStep(
        name="customer_analysis",
        agent=data_analyst_agent,
        task="Analyze customer data",
        condition=lambda data: "customer_data" in data
    )
    
    workflow.add_parallel_step(market_step)
    workflow.add_parallel_step(competitor_step)
    workflow.add_parallel_step(customer_step)
    
    return workflow

# Execute parallel workflow
workflow = create_parallel_analysis_workflow()
result = workflow.execute({
    "market": "technology",
    "competitors": ["OpenAI", "Anthropic", "Cohere"],
    "customer_data": "customer_survey_2024.csv"
})
```

### 3. **Conditional Workflows**
Branch execution based on conditions

```python
class ConditionalWorkflow(Workflow):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.branches = {}
        self.default_branch = None
    
    def add_branch(self, condition: callable, branch: Workflow):
        """Add conditional branch"""
        self.branches[condition] = branch
    
    def set_default_branch(self, branch: Workflow):
        """Set default branch"""
        self.default_branch = branch
    
    def execute(self, initial_data: dict) -> dict:
        """Execute workflow with conditional branching"""
        
        # Evaluate conditions
        for condition, branch in self.branches.items():
            try:
                if condition(initial_data):
                    return branch.execute(initial_data)
            except Exception as e:
                # Log error and continue to next condition
                print(f"Condition evaluation error: {e}")
                continue
        
        # Execute default branch if no condition matched
        if self.default_branch:
            return self.default_branch.execute(initial_data)
        else:
            return {
                "workflow_name": self.name,
                "status": "no_matching_branch",
                "message": "No condition matched and no default branch"
            }

# Define conditional workflow
def create_customer_service_workflow():
    """Create conditional customer service workflow"""
    
    workflow = ConditionalWorkflow("customer_service")
    
    # Branch 1: Technical Issues
    technical_branch = SequentialWorkflow("technical_support")
    technical_branch.add_step(WorkflowStep(
        name="diagnose",
        agent=tech_agent,
        task="Diagnose technical issue"
    ))
    technical_branch.add_step(WorkflowStep(
        name="resolve",
        agent=tech_agent,
        task="Resolve technical issue"
    ))
    
    # Branch 2: Billing Issues
    billing_branch = SequentialWorkflow("billing_support")
    billing_branch.add_step(WorkflowStep(
        name="verify_account",
        agent=billing_agent,
        task="Verify account details"
    ))
    billing_branch.add_step(WorkflowStep(
        name="process_billing",
        agent=billing_agent,
        task="Process billing request"
    ))
    
    # Branch 3: General Inquiries
    general_branch = SequentialWorkflow("general_support")
    general_branch.add_step(WorkflowStep(
        name="provide_info",
        agent=general_agent,
        task="Provide general information"
    ))
    
    # Add branches with conditions
    workflow.add_branch(
        condition=lambda data: "technical" in data.get("category", "").lower(),
        branch=technical_branch
    )
    
    workflow.add_branch(
        condition=lambda data: "billing" in data.get("category", "").lower(),
        branch=billing_branch
    )
    
    workflow.add_branch(
        condition=lambda data: "account" in data.get("category", "").lower(),
        branch=billing_branch
    )
    
    workflow.set_default_branch(general_branch)
    
    return workflow

# Execute conditional workflow
workflow = create_customer_service_workflow()

# Technical issue
result1 = workflow.execute({
    "category": "technical",
    "issue": "Cannot login to account"
})

# Billing issue
result2 = workflow.execute({
    "category": "billing",
    "issue": "Question about invoice"
})
```

---

## 🔄 Workflow Patterns

### 1. **Pipeline Pattern**
Data flows through sequential processing stages

```python
class PipelineWorkflow(Workflow):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.stages = []
    
    def add_stage(self, stage: WorkflowStep):
        """Add processing stage"""
        self.stages.append(stage)
    
    def execute(self, initial_data: dict) -> dict:
        """Execute pipeline workflow"""
        
        pipeline_data = initial_data.copy()
        stage_results = {}
        
        for i, stage in enumerate(self.stages):
            stage_name = stage.name
            
            try:
                # Transform data through stage
                transformed_data = self.execute_stage(stage, pipeline_data)
                
                stage_results[stage_name] = {
                    "status": "completed",
                    "input_data": pipeline_data.copy(),
                    "output_data": transformed_data
                }
                
                # Update pipeline data for next stage
                pipeline_data.update(transformed_data)
                
            except Exception as e:
                stage_results[stage_name] = {
                    "status": "failed",
                    "error": str(e),
                    "input_data": pipeline_data.copy()
                }
                break
        
        return {
            "workflow_name": self.name,
            "total_stages": len(self.stages),
            "stage_results": stage_results,
            "final_data": pipeline_data
        }
    
    def execute_stage(self, stage: WorkflowStep, data: dict) -> dict:
        """Execute individual pipeline stage"""
        
        if stage.transform_function:
            return stage.transform_function(data)
        elif stage.agent:
            return stage.agent.run(stage.task, **data)
        else:
            raise ValueError("Stage must have transform_function or agent")

# Define data processing pipeline
def create_data_processing_pipeline():
    """Create a data processing pipeline"""
    
    pipeline = PipelineWorkflow("data_processing")
    
    # Stage 1: Data Collection
    collection_stage = WorkflowStep(
        name="collect_data",
        agent=data_collector_agent,
        task="Collect raw data from sources",
        transform_function=None
    )
    
    # Stage 2: Data Cleaning
    cleaning_stage = WorkflowStep(
        name="clean_data",
        transform_function=lambda data: {
            "cleaned_data": clean_text_data(data.get("raw_data", ""))
        }
    )
    
    # Stage 3: Data Analysis
    analysis_stage = WorkflowStep(
        name="analyze_data",
        agent=analysis_agent,
        task="Analyze cleaned data"
    )
    
    # Stage 4: Report Generation
    report_stage = WorkflowStep(
        name="generate_report",
        agent=report_agent,
        task="Generate analysis report"
    )
    
    pipeline.add_stage(collection_stage)
    pipeline.add_stage(cleaning_stage)
    pipeline.add_stage(analysis_stage)
    pipeline.add_stage(report_stage)
    
    return pipeline
```

### 2. **Map-Reduce Pattern**
Process data in parallel and aggregate results

```python
class MapReduceWorkflow(Workflow):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.map_function = None
        self.reduce_function = None
        self.map_agents = []
    
    def set_map_function(self, map_func: callable):
        """Set map function"""
        self.map_function = map_func
    
    def set_reduce_function(self, reduce_func: callable):
        """Set reduce function"""
        self.reduce_function = reduce_func
    
    def add_map_agent(self, agent: Agent):
        """Add agent for map phase"""
        self.map_agents.append(agent)
    
    def execute(self, initial_data: dict) -> dict:
        """Execute map-reduce workflow"""
        
        # Map phase
        map_results = []
        
        if self.map_function:
            # Use map function
            map_results = self.map_function(initial_data)
        elif self.map_agents:
            # Use map agents in parallel
            with ThreadPoolExecutor(max_workers=len(self.map_agents)) as executor:
                futures = [
                    executor.submit(agent.run, "Process data", **initial_data)
                    for agent in self.map_agents
                ]
                
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        map_results.append(result)
                    except Exception as e:
                        print(f"Map phase error: {e}")
        
        # Reduce phase
        if self.reduce_function:
            final_result = self.reduce_function(map_results)
        else:
            final_result = self.aggregate_results(map_results)
        
        return {
            "workflow_name": self.name,
            "map_results": map_results,
            "final_result": final_result,
            "total_map_operations": len(map_results)
        }
    
    def aggregate_results(self, results: list) -> dict:
        """Default aggregation function"""
        return {
            "combined_results": results,
            "summary": f"Processed {len(results)} items"
        }

# Define map-reduce workflow
def create_text_analysis_workflow():
    """Create text analysis map-reduce workflow"""
    
    workflow = MapReduceWorkflow("text_analysis")
    
    # Map phase: Analyze different aspects
    def map_text_analysis(data: dict) -> list:
        text = data.get("text", "")
        
        # Create analysis tasks
        analysis_tasks = [
            {"type": "sentiment", "text": text},
            {"type": "entities", "text": text},
            {"type": "keywords", "text": text},
            {"type": "topics", "text": text}
        ]
        
        return analysis_tasks
    
    # Reduce phase: Combine analysis results
    def reduce_analysis(results: list) -> dict:
        combined = {
            "sentiment": None,
            "entities": [],
            "keywords": [],
            "topics": []
        }
        
        for result in results:
            if result.get("type") == "sentiment":
                combined["sentiment"] = result.get("result")
            elif result.get("type") == "entities":
                combined["entities"].extend(result.get("result", []))
            elif result.get("type") == "keywords":
                combined["keywords"].extend(result.get("result", []))
            elif result.get("type") == "topics":
                combined["topics"].extend(result.get("result", []))
        
        return combined
    
    workflow.set_map_function(map_text_analysis)
    workflow.set_reduce_function(reduce_analysis)
    
    return workflow
```

### 3. **State Machine Workflow**
Workflow with defined states and transitions

```python
class StateMachineWorkflow(Workflow):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.initial_state = None
    
    def add_state(self, state_name: str, actions: list):
        """Add state with actions"""
        self.states[state_name] = actions
    
    def add_transition(self, from_state: str, to_state: str, condition: callable):
        """Add transition between states"""
        if from_state not in self.transitions:
            self.transitions[from_state] = []
        self.transitions[from_state].append({
            "to_state": to_state,
            "condition": condition
        })
    
    def set_initial_state(self, state_name: str):
        """Set initial state"""
        self.initial_state = state_name
        self.current_state = state_name
    
    def execute(self, initial_data: dict) -> dict:
        """Execute state machine workflow"""
        
        workflow_data = initial_data.copy()
        execution_history = []
        
        # Start from initial state
        self.current_state = self.initial_state
        max_iterations = 50  # Prevent infinite loops
        iteration = 0
        
        while self.current_state and iteration < max_iterations:
            iteration += 1
            
            # Execute actions in current state
            state_actions = self.states.get(self.current_state, [])
            state_results = []
            
            for action in state_actions:
                try:
                    action_result = self.execute_action(action, workflow_data)
                    state_results.append({
                        "action": action["name"],
                        "result": action_result,
                        "status": "completed"
                    })
                    
                    # Update workflow data
                    workflow_data.update(action_result)
                    
                except Exception as e:
                    state_results.append({
                        "action": action["name"],
                        "error": str(e),
                        "status": "failed"
                    })
            
            # Record state execution
            execution_history.append({
                "state": self.current_state,
                "actions": state_results,
                "iteration": iteration
            })
            
            # Find next state
            next_state = self.find_next_state(self.current_state, workflow_data)
            
            if not next_state:
                break  # No valid transition
            
            self.current_state = next_state
        
        return {
            "workflow_name": self.name,
            "execution_history": execution_history,
            "final_state": self.current_state,
            "final_data": workflow_data,
            "total_iterations": iteration
        }
    
    def find_next_state(self, current_state: str, data: dict) -> str:
        """Find next state based on transitions"""
        
        transitions = self.transitions.get(current_state, [])
        
        for transition in transitions:
            try:
                if transition["condition"](data):
                    return transition["to_state"]
            except Exception as e:
                print(f"Transition condition error: {e}")
                continue
        
        return None  # No valid transition
    
    def execute_action(self, action: dict, data: dict) -> dict:
        """Execute action in current state"""
        
        if action["type"] == "agent":
            return action["agent"].run(action["task"], **data)
        elif action["type"] == "function":
            return action["function"](data)
        else:
            raise ValueError(f"Unknown action type: {action['type']}")

# Define order processing state machine
def create_order_processing_workflow():
    """Create order processing state machine"""
    
    workflow = StateMachineWorkflow("order_processing")
    
    # Define states
    workflow.add_state("pending", [
        {
            "name": "validate_order",
            "type": "agent",
            "agent": validation_agent,
            "task": "Validate order details"
        }
    ])
    
    workflow.add_state("validated", [
        {
            "name": "check_inventory",
            "type": "agent",
            "agent": inventory_agent,
            "task": "Check product availability"
        }
    ])
    
    workflow.add_state("inventory_checked", [
        {
            "name": "process_payment",
            "type": "agent",
            "agent": payment_agent,
            "task": "Process payment"
        }
    ])
    
    workflow.add_state("payment_processed", [
        {
            "name": "fulfill_order",
            "type": "agent",
            "agent": fulfillment_agent,
            "task": "Fulfill order"
        }
    ])
    
    workflow.add_state("completed", [])
    workflow.add_state("failed", [])
    
    # Define transitions
    workflow.add_transition(
        "pending", "validated",
        condition=lambda data: data.get("order_valid", False)
    )
    
    workflow.add_transition(
        "pending", "failed",
        condition=lambda data: data.get("order_invalid", False)
    )
    
    workflow.add_transition(
        "validated", "inventory_checked",
        condition=lambda data: "inventory_result" in data
    )
    
    workflow.add_transition(
        "inventory_checked", "payment_processed",
        condition=lambda data: data.get("inventory_available", False)
    )
    
    workflow.add_transition(
        "payment_processed", "fulfilled",
        condition=lambda data: data.get("payment_successful", False)
    )
    
    workflow.set_initial_state("pending")
    
    return workflow
```

---

## 🔧 Workflow Configuration

### 1. **Workflow Definition**
Define workflows using configuration files

```python
import yaml
from google_adk import WorkflowLoader

class WorkflowConfig:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> dict:
        """Load workflow configuration from file"""
        
        with open(self.config_file, 'r') as f:
            if self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                return yaml.safe_load(f)
            else:
                return json.load(f)
    
    def create_workflow(self) -> Workflow:
        """Create workflow from configuration"""
        
        workflow_type = self.config.get("type", "sequential")
        
        if workflow_type == "sequential":
            return self.create_sequential_workflow()
        elif workflow_type == "parallel":
            return self.create_parallel_workflow()
        elif workflow_type == "conditional":
            return self.create_conditional_workflow()
        elif workflow_type == "state_machine":
            return self.create_state_machine_workflow()
        else:
            raise ValueError(f"Unknown workflow type: {workflow_type}")
    
    def create_sequential_workflow(self) -> SequentialWorkflow:
        """Create sequential workflow from config"""
        
        workflow = SequentialWorkflow(self.config["name"])
        
        for step_config in self.config["steps"]:
            step = self.create_step_from_config(step_config)
            workflow.add_step(step)
        
        return workflow
    
    def create_step_from_config(self, step_config: dict) -> WorkflowStep:
        """Create workflow step from configuration"""
        
        # Load agent if specified
        agent = None
        if "agent" in step_config:
            agent = self.load_agent(step_config["agent"])
        
        # Create step
        step = WorkflowStep(
            name=step_config["name"],
            agent=agent,
            task=step_config.get("task", ""),
            condition=self.parse_condition(step_config.get("condition")),
            terminates_workflow=step_config.get("terminates", False),
            continue_on_error=step_config.get("continue_on_error", False)
        )
        
        return step

# Example workflow configuration (workflow.yaml)
"""
name: "customer_onboarding"
type: "sequential"
description: "Customer onboarding workflow"

steps:
  - name: "welcome"
    agent: "welcome_agent"
    task: "Send welcome message to new customer"
    condition: "customer_status == 'new'"
    
  - name: "profile_setup"
    agent: "profile_agent"
    task: "Help customer set up their profile"
    condition: "welcome_completed == true"
    
  - name: "tutorial"
    agent: "tutorial_agent"
    task: "Provide product tutorial"
    condition: "profile_completed == true"
    
  - name: "follow_up"
    agent: "followup_agent"
    task: "Schedule follow up call"
    condition: "tutorial_completed == true"
    terminates: true

agents:
  welcome_agent:
    type: "Agent"
    model: "chat-bison@001"
    tools: ["email_tool", "sms_tool"]
    
  profile_agent:
    type: "Agent"
    model: "text-bison@001"
    tools: ["database_tool", "validation_tool"]
    
  tutorial_agent:
    type: "Agent"
    model: "gemini-pro"
    tools: ["knowledge_base_tool", "screen_share_tool"]
    
  followup_agent:
    type: "Agent"
    model: "chat-bison@001"
    tools: ["calendar_tool", "reminder_tool"]
"""
```

### 2. **Dynamic Workflow Generation**
Generate workflows based on requirements

```python
class WorkflowGenerator:
    def __init__(self):
        self.agent_registry = {}
        self.workflow_templates = {}
    
    def register_agent(self, name: str, agent: Agent, capabilities: list):
        """Register agent with capabilities"""
        self.agent_registry[name] = {
            "agent": agent,
            "capabilities": capabilities
        }
    
    def generate_workflow(self, requirements: dict) -> Workflow:
        """Generate workflow based on requirements"""
        
        # Analyze requirements
        task_complexity = requirements.get("complexity", "medium")
        parallelizable = requirements.get("parallelizable", False)
        has_conditions = requirements.get("conditional", False)
        
        # Select workflow type
        if parallelizable and task_complexity == "high":
            return self.generate_parallel_workflow(requirements)
        elif has_conditions:
            return self.generate_conditional_workflow(requirements)
        else:
            return self.generate_sequential_workflow(requirements)
    
    def generate_sequential_workflow(self, requirements: dict) -> SequentialWorkflow:
        """Generate sequential workflow"""
        
        workflow = SequentialWorkflow(f"generated_{int(time.time())}")
        
        # Generate steps based on requirements
        steps = self.analyze_requirements_steps(requirements)
        
        for step_def in steps:
            agent = self.select_best_agent(step_def["required_capabilities"])
            
            step = WorkflowStep(
                name=step_def["name"],
                agent=agent,
                task=step_def["task"],
                condition=step_def.get("condition")
            )
            
            workflow.add_step(step)
        
        return workflow
    
    def select_best_agent(self, required_capabilities: list) -> Agent:
        """Select best agent for required capabilities"""
        
        suitable_agents = []
        
        for name, agent_info in self.agent_registry.items():
            agent_capabilities = agent_info["capabilities"]
            
            # Check if agent has all required capabilities
            if all(cap in agent_capabilities for cap in required_capabilities):
                suitable_agents.append({
                    "name": name,
                    "agent": agent_info["agent"],
                    "match_score": len(agent_capabilities)
                })
        
        if not suitable_agents:
            raise ValueError("No suitable agent found for required capabilities")
        
        # Select agent with most capabilities (most specialized)
        best_agent = max(suitable_agents, key=lambda x: x["match_score"])
        return best_agent["agent"]

# Usage
generator = WorkflowGenerator()

# Register agents
generator.register_agent("researcher", research_agent, ["web_search", "data_collection"])
generator.register_agent("analyst", analysis_agent, ["data_analysis", "statistics"])
generator.register_agent("writer", writing_agent, ["content_creation", "formatting"])

# Generate workflow
requirements = {
    "complexity": "high",
    "parallelizable": True,
    "conditional": False,
    "task_description": "Comprehensive market analysis"
}

workflow = generator.generate_workflow(requirements)
```

---

## 📊 Workflow Monitoring

### 1. **Execution Tracking**
Monitor workflow execution in real-time

```python
class WorkflowMonitor:
    def __init__(self):
        self.active_workflows = {}
        self.execution_history = []
        self.metrics = {}
    
    def start_monitoring(self, workflow: Workflow, execution_id: str):
        """Start monitoring workflow execution"""
        
        self.active_workflows[execution_id] = {
            "workflow": workflow,
            "start_time": time.time(),
            "status": "running",
            "current_step": 0,
            "steps_completed": 0,
            "errors": []
        }
    
    def update_step_progress(self, execution_id: str, step_name: str, status: str, result: dict = None):
        """Update step progress"""
        
        if execution_id in self.active_workflows:
            workflow_info = self.active_workflows[execution_id]
            
            if status == "completed":
                workflow_info["steps_completed"] += 1
            
            workflow_info["current_step_name"] = step_name
            workflow_info["current_step_status"] = status
            
            if result:
                workflow_info["last_result"] = result
            
            # Log step completion
            self.log_step_event(execution_id, step_name, status, result)
    
    def complete_workflow(self, execution_id: str, final_result: dict):
        """Mark workflow as completed"""
        
        if execution_id in self.active_workflows:
            workflow_info = self.active_workflows[execution_id]
            
            workflow_info["status"] = "completed"
            workflow_info["end_time"] = time.time()
            workflow_info["duration"] = workflow_info["end_time"] - workflow_info["start_time"]
            workflow_info["final_result"] = final_result
            
            # Move to history
            self.execution_history.append(workflow_info)
            del self.active_workflows[execution_id]
            
            # Update metrics
            self.update_metrics(workflow_info)
    
    def log_step_event(self, execution_id: str, step_name: str, status: str, result: dict):
        """Log step event"""
        
        event = {
            "execution_id": execution_id,
            "step_name": step_name,
            "status": status,
            "timestamp": time.time(),
            "result": result
        }
        
        # Store event (could be database, file, etc.)
        self.store_event(event)
    
    def get_workflow_status(self, execution_id: str) -> dict:
        """Get current workflow status"""
        
        return self.active_workflows.get(execution_id, {
            "status": "not_found"
        })
    
    def get_execution_metrics(self, execution_id: str) -> dict:
        """Get execution metrics"""
        
        workflow_info = None
        
        # Check active workflows
        if execution_id in self.active_workflows:
            workflow_info = self.active_workflows[execution_id]
        
        # Check execution history
        for hist in self.execution_history:
            if hist.get("execution_id") == execution_id:
                workflow_info = hist
                break
        
        if workflow_info:
            return {
                "execution_id": execution_id,
                "workflow_name": workflow_info["workflow"].name,
                "status": workflow_info["status"],
                "duration": workflow_info.get("duration", time.time() - workflow_info["start_time"]),
                "steps_completed": workflow_info["steps_completed"],
                "total_steps": len(workflow_info["workflow"].steps) if hasattr(workflow_info["workflow"], 'steps') else 0,
                "error_count": len(workflow_info.get("errors", [])),
                "progress_percentage": (workflow_info["steps_completed"] / len(workflow_info["workflow"].steps)) * 100 if hasattr(workflow_info["workflow"], 'steps') else 0
            }
        
        return {"status": "not_found"}

# Usage
monitor = WorkflowMonitor()

# Start monitoring workflow
execution_id = f"workflow_{int(time.time())}"
monitor.start_monitoring(workflow, execution_id)

# Update progress during execution
monitor.update_step_progress(execution_id, "research", "completed", research_result)
monitor.update_step_progress(execution_id, "analysis", "completed", analysis_result)

# Complete workflow
monitor.complete_workflow(execution_id, final_result)
```

---

## 🎯 Best Practices

### 1. **Workflow Design**
- **Clear Steps**: Each step should have single responsibility
- **Error Handling**: Define behavior for failures
- **Idempotency**: Steps should be safe to retry
- **Modularity**: Design reusable workflow components

### 2. **Performance**
- **Parallel Execution**: Use parallel workflows when possible
- **Resource Management**: Optimize agent utilization
- **Caching**: Cache intermediate results
- **Timeout Handling**: Set appropriate timeouts

### 3. **Monitoring**
- **Real-time Tracking**: Monitor workflow execution
- **Metrics Collection**: Track performance metrics
- **Alerting**: Set up alerts for failures
- **Logging**: Comprehensive execution logs

### 4. **Maintenance**
- **Version Control**: Track workflow versions
- **Testing**: Test workflows thoroughly
- **Documentation**: Document workflow logic
- **Validation**: Validate workflow definitions

---

## 📚 Next Steps

1. **Learn Callbacks** → `09-callbacks.md`
2. **Master MCP Integration** → `10-mcp-with-adk.md`
3. **Build Complex Workflows** → Create advanced workflow systems
4. **Deploy to Production** → Scale workflow execution

---

**⚙️ Design powerful workflows for complex AI automation!**
