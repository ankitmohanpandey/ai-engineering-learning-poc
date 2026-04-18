# Multi-Agent Systems

> **Building collaborative AI systems with multiple specialized agents**

Multi-agent systems enable complex problem-solving by distributing tasks across specialized agents that can communicate, collaborate, and coordinate their actions.

---

## 🎯 What are Multi-Agent Systems?

### Definition
A **Multi-Agent System** in Google ADK is a collection of autonomous agents that:
- **Collaborate**: Work together on shared goals
- **Communicate**: Exchange information and results
- **Coordinate**: Synchronize actions and decisions
- **Specialize**: Each agent has specific expertise
- **Scale**: Handle complex tasks through distribution

### System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                Multi-Agent System                    │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Coordinator │◄────────►│   Agent Registry    │
│   (Orchestrator)│        │   (Agent Directory) │
└──────────────┘         └──────────────────────┘
          │                           │
          ▼                           ▼
┌──────────────────────┐    ┌──────────────────────┐
│   Communication    │    │   Task Manager     │
│   Bus            │    │   (Task Queue)     │
│  (Message Passing)│    │                    │
└──────────────────────┘    └──────────────────────┘
          │                           │
          └───────────┬───────────┘
                      ▼
┌─────────────────────────────────────────┐
│            Agent Pool                │
│  ┌──────────┐ ┌──────────┐      │
│  │ Agent A  │ │ Agent B  │ ...  │
│  │ (Research)│ │(Analysis)│      │
│  └──────────┘ └──────────┘      │
│  ┌──────────┐ ┌──────────┐      │
│  │ Agent C  │ │ Agent D  │ ...  │
│  │ (Writing)│ │(Review) │      │
│  └──────────┘ └──────────┘      │
└─────────────────────────────────────────┘
```

---

## 🏗️ Agent Types in Multi-Agent Systems

### 1. **Coordinator Agent**
Manages and orchestrates other agents

```python
from google_adk import Agent, MultiAgentSystem

class CoordinatorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="coordinator",
            description="Orchestrates multi-agent workflows",
            model="gemini-pro",
            tools=[
                TaskAssignmentTool(),
                AgentCommunicationTool(),
                ResultAggregationTool()
            ]
        )
    
    def coordinate_task(self, task_description: str) -> dict:
        """Coordinate task execution across agents"""
        
        # Analyze task requirements
        task_analysis = self.analyze_task(task_description)
        
        # Identify required agents
        required_agents = self.identify_agents(task_analysis)
        
        # Create execution plan
        execution_plan = self.create_plan(task_analysis, required_agents)
        
        # Execute plan
        results = self.execute_plan(execution_plan)
        
        # Aggregate results
        final_result = self.aggregate_results(results)
        
        return final_result

# Create coordinator
coordinator = CoordinatorAgent()
```

### 2. **Specialist Agents**
Agents with specific expertise

```python
# Research Agent
research_agent = Agent(
    name="researcher",
    description="Specializes in information gathering and research",
    model="gemini-pro",
    tools=[
        GoogleSearchTool(),
        ScholarSearchTool(),
        WebCrawlerTool(),
        DocumentAnalyzerTool()
    ],
    instructions="""
    You are a research specialist. Your role is to:
    1. Gather comprehensive information on given topics
    2. Validate sources and credibility
    3. Organize findings systematically
    4. Provide citations and references
    """
)

# Analysis Agent
analysis_agent = Agent(
    name="analyst",
    description="Specializes in data analysis and insights",
    model="gemini-pro",
    tools=[
        DataAnalyzerTool(),
        StatisticalTool(),
        VisualizationTool(),
        ReportGeneratorTool()
    ],
    instructions="""
    You are a data analysis specialist. Your role is to:
    1. Analyze provided data thoroughly
    2. Identify patterns and trends
    3. Generate meaningful insights
    4. Create visual representations
    """
)

# Writing Agent
writing_agent = Agent(
    name="writer",
    description="Specializes in content creation and writing",
    model="text-bison@001",
    tools=[
        GrammarTool(),
        StyleTool(),
        FormattingTool(),
        PlagiarismTool()
    ],
    instructions="""
    You are a writing specialist. Your role is to:
    1. Create well-structured content
    2. Ensure proper grammar and style
    3. Format content appropriately
    4. Maintain consistency and clarity
    """
)
```

### 3. **Mediator Agent**
Facilitates communication between agents

```python
class MediatorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="mediator",
            description="Mediates communication between agents",
            model="gemini-pro",
            tools=[
                MessageRouterTool(),
                ConflictResolverTool(),
                ConsensusTool()
            ]
        )
    
    def mediate_communication(self, agents: list, message: dict) -> dict:
        """Mediate communication between agents"""
        
        # Route message to appropriate agents
        routed_messages = self.route_message(agents, message)
        
        # Handle conflicts if any
        if self.detect_conflicts(routed_messages):
            resolution = self.resolve_conflicts(routed_messages)
            routed_messages = self.apply_resolution(routed_messages, resolution)
        
        # Build consensus if needed
        if self.requires_consensus(routed_messages):
            consensus = self.build_consensus(routed_messages)
            routed_messages = self.apply_consensus(routed_messages, consensus)
        
        return routed_messages

# Create mediator
mediator = MediatorAgent()
```

---

## 🔄 Communication Patterns

### 1. **Direct Communication**
Agents communicate directly with each other

```python
from google_adk import AgentCommunication

class DirectCommunication:
    def __init__(self):
        self.agents = {}
        self.message_bus = MessageBus()
    
    def register_agent(self, agent: Agent):
        """Register agent for direct communication"""
        self.agents[agent.name] = agent
        self.message_bus.subscribe(agent.name, agent.receive_message)
    
    def send_message(self, from_agent: str, to_agent: str, message: dict):
        """Send direct message between agents"""
        
        if to_agent not in self.agents:
            raise ValueError(f"Agent {to_agent} not found")
        
        # Create message envelope
        envelope = {
            "from": from_agent,
            "to": to_agent,
            "timestamp": datetime.now(),
            "message_id": str(uuid.uuid4()),
            "content": message
        }
        
        # Send message
        self.message_bus.publish(to_agent, envelope)
    
    def broadcast_message(self, from_agent: str, message: dict):
        """Broadcast message to all agents"""
        
        for agent_name in self.agents:
            if agent_name != from_agent:
                self.send_message(from_agent, agent_name, message)

# Usage
comm = DirectCommunication()
comm.register_agent(research_agent)
comm.register_agent(analysis_agent)
comm.register_agent(writing_agent)

# Send message from research to analysis
comm.send_message("researcher", "analyst", {
    "type": "data_ready",
    "data": research_results,
    "request": "analyze_this_data"
})
```

### 2. **Hierarchical Communication**
Agents communicate through structured hierarchy

```python
class HierarchicalCommunication:
    def __init__(self):
        self.hierarchy = {}
        self.message_router = MessageRouter()
    
    def add_hierarchy_level(self, level: int, agents: list):
        """Add agents to hierarchy level"""
        self.hierarchy[level] = agents
        
        # Set up communication rules
        for agent in agents:
            agent.level = level
            agent.subordinates = []
            agent.superiors = []
    
    def establish_hierarchy(self):
        """Establish hierarchical relationships"""
        
        for level in sorted(self.hierarchy.keys()):
            agents = self.hierarchy[level]
            
            # Connect to next level down
            if level + 1 in self.hierarchy:
                subordinates = self.hierarchy[level + 1]
                
                for agent in agents:
                    agent.subordinates = subordinates
                    
                    for subordinate in subordinates:
                        subordinate.superiors.append(agent)
    
    def send_up_hierarchy(self, from_agent: Agent, message: dict):
        """Send message up the hierarchy"""
        
        for superior in from_agent.superiors:
            self.message_router.route(
                from_agent=from_agent.name,
                to_agent=superior.name,
                message=message,
                direction="up"
            )
    
    def send_down_hierarchy(self, from_agent: Agent, message: dict):
        """Send message down the hierarchy"""
        
        for subordinate in from_agent.subordinates:
            self.message_router.route(
                from_agent=from_agent.name,
                to_agent=subordinate.name,
                message=message,
                direction="down"
            )

# Usage
hierarchy = HierarchicalCommunication()
hierarchy.add_hierarchy_level(1, [coordinator])
hierarchy.add_hierarchy_level(2, [research_agent, analysis_agent])
hierarchy.add_hierarchy_level(3, [writing_agent])

hierarchy.establish_hierarchy()

# Send message up hierarchy
hierarchy.send_up_hierarchy(writing_agent, {
    "type": "status_update",
    "status": "completed",
    "task": "document_writing"
})
```

### 3. **Event-Driven Communication**
Agents communicate through events

```python
from google_adk import EventBus, Event

class EventDrivenCommunication:
    def __init__(self):
        self.event_bus = EventBus()
        self.agents = {}
        self.event_handlers = {}
    
    def register_agent(self, agent: Agent):
        """Register agent for event communication"""
        self.agents[agent.name] = agent
        
        # Subscribe agent to relevant events
        for event_type in agent.subscribed_events:
            self.event_bus.subscribe(event_type, agent.handle_event)
    
    def publish_event(self, event_type: str, event_data: dict, source: str):
        """Publish event to all subscribed agents"""
        
        event = Event(
            type=event_type,
            data=event_data,
            source=source,
            timestamp=datetime.now(),
            event_id=str(uuid.uuid4())
        )
        
        self.event_bus.publish(event)
    
    def create_workflow_events(self, workflow_name: str):
        """Create standard workflow events"""
        
        events = [
            f"{workflow_name}.started",
            f"{workflow_name}.progress",
            f"{workflow_name}.completed",
            f"{workflow_name}.failed",
            f"{workflow_name}.agent_assigned",
            f"{workflow_name}.agent_completed"
        ]
        
        return events

# Usage
event_comm = EventDrivenCommunication()

# Define agent event subscriptions
research_agent.subscribed_events = ["research.started", "research.data_requested"]
analysis_agent.subscribed_events = ["research.completed", "analysis.started"]
writing_agent.subscribed_events = ["analysis.completed", "writing.started"]

# Register agents
event_comm.register_agent(research_agent)
event_comm.register_agent(analysis_agent)
event_comm.register_agent(writing_agent)

# Publish events
event_comm.publish_event("research.started", {
    "topic": "AI technology trends",
    "deadline": "2024-02-01"
}, source="coordinator")
```

---

## 🎯 Orchestration Patterns

### 1. **Sequential Orchestration**
Agents execute tasks in sequence

```python
class SequentialOrchestrator:
    def __init__(self):
        self.agents = {}
        self.workflow_steps = []
    
    def add_agent(self, agent: Agent):
        """Add agent to orchestration"""
        self.agents[agent.name] = agent
    
    def define_workflow(self, steps: list):
        """Define sequential workflow"""
        self.workflow_steps = steps
    
    def execute_workflow(self, initial_input: dict) -> dict:
        """Execute sequential workflow"""
        
        current_data = initial_input
        results = {}
        
        for step in self.workflow_steps:
            agent_name = step["agent"]
            task = step["task"]
            input_mapping = step.get("input_mapping", {})
            
            # Prepare input for current agent
            agent_input = self.prepare_input(current_data, input_mapping)
            
            # Execute agent
            agent = self.agents[agent_name]
            result = agent.run(task, **agent_input)
            
            # Store result
            results[f"{agent_name}_result"] = result
            
            # Update current data for next step
            current_data.update(result)
            
            # Check if workflow should continue
            if step.get("condition"):
                if not self.evaluate_condition(step["condition"], current_data):
                    break
        
        return results
    
    def prepare_input(self, data: dict, mapping: dict) -> dict:
        """Prepare input for agent based on mapping"""
        agent_input = {}
        
        for key, value_path in mapping.items():
            if isinstance(value_path, str):
                agent_input[key] = self.get_nested_value(data, value_path)
            else:
                agent_input[key] = value_path
        
        return agent_input

# Usage
orchestrator = SequentialOrchestrator()
orchestrator.add_agent(research_agent)
orchestrator.add_agent(analysis_agent)
orchestrator.add_agent(writing_agent)

# Define workflow
workflow_steps = [
    {
        "agent": "researcher",
        "task": "Research AI technology trends",
        "input_mapping": {"topic": "topic"}
    },
    {
        "agent": "analyst",
        "task": "Analyze research findings",
        "input_mapping": {
            "data": "researcher_result.data",
            "analysis_type": "trend_analysis"
        }
    },
    {
        "agent": "writer",
        "task": "Write comprehensive report",
        "input_mapping": {
            "research_data": "researcher_result.data",
            "analysis": "analyst_result.insights",
            "format": "executive_report"
        }
    }
]

orchestrator.define_workflow(workflow_steps)

# Execute workflow
results = orchestrator.execute_workflow({
    "topic": "AI technology trends 2024"
})
```

### 2. **Parallel Orchestration**
Agents execute tasks simultaneously

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ParallelOrchestrator:
    def __init__(self, max_workers: int = 5):
        self.agents = {}
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    def add_agent(self, agent: Agent):
        """Add agent to orchestration"""
        self.agents[agent.name] = agent
    
    async def execute_parallel_tasks(self, tasks: list) -> dict:
        """Execute tasks in parallel"""
        
        # Create async tasks
        async_tasks = []
        for task in tasks:
            async_task = self.execute_single_task(task)
            async_tasks.append(async_task)
        
        # Execute all tasks concurrently
        results = await asyncio.gather(*async_tasks, return_exceptions=True)
        
        # Process results
        processed_results = {}
        for i, result in enumerate(results):
            task_name = tasks[i]["name"]
            
            if isinstance(result, Exception):
                processed_results[task_name] = {
                    "error": str(result),
                    "success": False
                }
            else:
                processed_results[task_name] = {
                    "data": result,
                    "success": True
                }
        
        return processed_results
    
    async def execute_single_task(self, task: dict) -> dict:
        """Execute single task asynchronously"""
        
        agent_name = task["agent"]
        task_description = task["task"]
        agent = self.agents[agent_name]
        
        # Execute agent in thread pool
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            self.executor,
            agent.run,
            task_description
        )
        
        return result

# Usage
parallel_orchestrator = ParallelOrchestrator(max_workers=3)
parallel_orchestrator.add_agent(research_agent)
parallel_orchestrator.add_agent(analysis_agent)
parallel_orchestrator.add_agent(writing_agent)

# Define parallel tasks
parallel_tasks = [
    {
        "name": "market_research",
        "agent": "researcher",
        "task": "Research market trends in AI"
    },
    {
        "name": "competitor_analysis",
        "agent": "analyst",
        "task": "Analyze competitor strategies"
    },
    {
        "name": "content_creation",
        "agent": "writer",
        "task": "Create marketing content"
    }
]

# Execute parallel tasks
async def run_parallel():
    results = await parallel_orchestrator.execute_parallel_tasks(parallel_tasks)
    return results

# Run the parallel execution
results = asyncio.run(run_parallel())
```

### 3. **Dynamic Orchestration**
Agents are selected and coordinated dynamically

```python
class DynamicOrchestrator:
    def __init__(self):
        self.agents = {}
        self.agent_capabilities = {}
        self.task_queue = TaskQueue()
        self.result_store = ResultStore()
    
    def register_agent(self, agent: Agent, capabilities: list):
        """Register agent with capabilities"""
        self.agents[agent.name] = agent
        self.agent_capabilities[agent.name] = capabilities
    
    def submit_task(self, task: dict) -> str:
        """Submit task for dynamic execution"""
        
        task_id = str(uuid.uuid4())
        task["id"] = task_id
        task["status"] = "pending"
        task["created_at"] = datetime.now()
        
        # Analyze task requirements
        required_capabilities = self.analyze_task_requirements(task)
        
        # Find suitable agents
        suitable_agents = self.find_suitable_agents(required_capabilities)
        
        # Select best agent
        selected_agent = self.select_best_agent(suitable_agents, task)
        
        # Assign task to agent
        if selected_agent:
            task["assigned_agent"] = selected_agent
            task["status"] = "assigned"
            self.assign_task_to_agent(selected_agent, task)
        else:
            task["status"] = "no_suitable_agent"
        
        # Store task
        self.result_store.store_task(task)
        
        return task_id
    
    def find_suitable_agents(self, required_capabilities: list) -> list:
        """Find agents with required capabilities"""
        
        suitable_agents = []
        
        for agent_name, capabilities in self.agent_capabilities.items():
            # Check if agent has all required capabilities
            if all(cap in capabilities for cap in required_capabilities):
                suitable_agents.append({
                    "name": agent_name,
                    "capabilities": capabilities,
                    "workload": self.get_agent_workload(agent_name),
                    "performance": self.get_agent_performance(agent_name)
                })
        
        return suitable_agents
    
    def select_best_agent(self, suitable_agents: list, task: dict) -> str:
        """Select best agent for task"""
        
        if not suitable_agents:
            return None
        
        # Score agents based on multiple factors
        best_agent = None
        best_score = -1
        
        for agent_info in suitable_agents:
            score = self.calculate_agent_score(agent_info, task)
            
            if score > best_score:
                best_score = score
                best_agent = agent_info["name"]
        
        return best_agent
    
    def calculate_agent_score(self, agent_info: dict, task: dict) -> float:
        """Calculate score for agent selection"""
        
        # Factors for scoring
        capability_match = len(agent_info["capabilities"])  # More capabilities = better
        workload_factor = 1 / (1 + agent_info["workload"])  # Less workload = better
        performance_factor = agent_info["performance"]  # Better performance = better
        
        # Weighted score
        score = (
            capability_match * 0.3 +
            workload_factor * 0.4 +
            performance_factor * 0.3
        )
        
        return score

# Usage
dynamic_orchestrator = DynamicOrchestrator()

# Register agents with capabilities
dynamic_orchestrator.register_agent(
    research_agent,
    ["web_search", "data_collection", "source_validation"]
)

dynamic_orchestrator.register_agent(
    analysis_agent,
    ["data_analysis", "statistics", "visualization"]
)

dynamic_orchestrator.register_agent(
    writing_agent,
    ["content_creation", "editing", "formatting"]
)

# Submit tasks
task1_id = dynamic_orchestrator.submit_task({
    "description": "Research latest AI trends",
    "priority": "high",
    "required_capabilities": ["web_search", "data_collection"]
})

task2_id = dynamic_orchestrator.submit_task({
    "description": "Analyze market data",
    "priority": "medium",
    "required_capabilities": ["data_analysis", "statistics"]
})
```

---

## 🔄 Coordination Strategies

### 1. **Task Decomposition**
Break complex tasks into smaller subtasks

```python
class TaskDecomposer:
    def __init__(self):
        self.decomposition_rules = {}
    
    def add_decomposition_rule(self, task_type: str, rule: callable):
        """Add rule for decomposing specific task types"""
        self.decomposition_rules[task_type] = rule
    
    def decompose_task(self, task: dict) -> list:
        """Decompose task into subtasks"""
        
        task_type = task.get("type", "general")
        
        # Use specific rule if available
        if task_type in self.decomposition_rules:
            return self.decomposition_rules[task_type](task)
        
        # Use general decomposition
        return self.general_decomposition(task)
    
    def general_decomposition(self, task: dict) -> list:
        """General task decomposition strategy"""
        
        subtasks = []
        
        # Research phase
        if task.get("requires_research", True):
            subtasks.append({
                "type": "research",
                "description": f"Research information for: {task['description']}",
                "agent": "researcher",
                "dependencies": []
            })
        
        # Analysis phase
        if task.get("requires_analysis", True):
            subtasks.append({
                "type": "analysis",
                "description": f"Analyze data for: {task['description']}",
                "agent": "analyst",
                "dependencies": ["research"]
            })
        
        # Creation phase
        if task.get("requires_creation", True):
            subtasks.append({
                "type": "creation",
                "description": f"Create output for: {task['description']}",
                "agent": "writer",
                "dependencies": ["research", "analysis"]
            })
        
        return subtasks

# Usage
decomposer = TaskDecomposer()

# Add specific decomposition rule
def decompose_research_task(task: dict) -> list:
    """Decompose research task specifically"""
    
    return [
        {
            "type": "search",
            "description": f"Search for: {task['query']}",
            "agent": "researcher",
            "dependencies": []
        },
        {
            "type": "validate",
            "description": "Validate search results",
            "agent": "analyst",
            "dependencies": ["search"]
        },
        {
            "type": "summarize",
            "description": "Summarize findings",
            "agent": "writer",
            "dependencies": ["validate"]
        }
    ]

decomposer.add_decomposition_rule("research", decompose_research_task)

# Decompose task
task = {
    "type": "research",
    "description": "Research AI market trends",
    "query": "AI market trends 2024"
}

subtasks = decomposer.decompose_task(task)
```

### 2. **Conflict Resolution**
Handle conflicts between agents

```python
class ConflictResolver:
    def __init__(self):
        self.resolution_strategies = {}
    
    def add_resolution_strategy(self, conflict_type: str, strategy: callable):
        """Add strategy for resolving specific conflict types"""
        self.resolution_strategies[conflict_type] = strategy
    
    def resolve_conflict(self, conflict: dict) -> dict:
        """Resolve conflict between agents"""
        
        conflict_type = conflict["type"]
        
        # Use specific strategy if available
        if conflict_type in self.resolution_strategies:
            return self.resolution_strategies[conflict_type](conflict)
        
        # Use general resolution
        return self.general_resolution(conflict)
    
    def general_resolution(self, conflict: dict) -> dict:
        """General conflict resolution strategy"""
        
        # Get conflicting agents
        agents = conflict["agents"]
        issues = conflict["issues"]
        
        # Try to find common ground
        resolution = {
            "type": "compromise",
            "solutions": []
        }
        
        for issue in issues:
            # Generate compromise solutions
            solutions = self.generate_compromise_solutions(issue, agents)
            resolution["solutions"].extend(solutions)
        
        # Select best solution
        best_solution = self.select_best_solution(resolution["solutions"])
        resolution["selected_solution"] = best_solution
        
        return resolution
    
    def generate_compromise_solutions(self, issue: dict, agents: list) -> list:
        """Generate compromise solutions for issue"""
        
        solutions = []
        
        # Solution 1: Priority-based
        if "priority" in issue:
            high_priority_agent = max(agents, key=lambda a: a.get("priority", 0))
            solutions.append({
                "type": "priority_based",
                "description": f"Follow {high_priority_agent.name}'s approach",
                "agent": high_priority_agent.name
            })
        
        # Solution 2: Hybrid approach
        solutions.append({
            "type": "hybrid",
            "description": "Combine approaches from all agents",
            "agents": [a.name for a in agents]
        })
        
        # Solution 3: Escalation
        solutions.append({
            "type": "escalation",
            "description": "Escalate to coordinator agent",
            "escalated_to": "coordinator"
        })
        
        return solutions

# Usage
conflict_resolver = ConflictResolver()

# Add specific resolution strategy
def resolve_data_conflict(conflict: dict) -> dict:
    """Resolve data-related conflicts"""
    
    conflicting_data = conflict["data"]
    agents = conflict["agents"]
    
    # Try to merge data
    merged_data = {}
    for agent in agents:
        agent_data = conflicting_data.get(agent.name, {})
        merged_data.update(agent_data)
    
    return {
        "type": "data_merge",
        "resolution": "merged_data",
        "merged_data": merged_data,
        "agents_involved": [a.name for a in agents]
    }

conflict_resolver.add_resolution_strategy("data_conflict", resolve_data_conflict)

# Resolve conflict
conflict = {
    "type": "data_conflict",
    "agents": [research_agent, analysis_agent],
    "data": {
        "researcher": {"source": "web", "confidence": 0.8},
        "analyst": {"source": "database", "confidence": 0.9}
    }
}

resolution = conflict_resolver.resolve_conflict(conflict)
```

---

## 📊 Multi-Agent System Examples

### 1. **Research Team System**
Multiple agents collaborating on research

```python
class ResearchTeamSystem:
    def __init__(self):
        self.agents = {}
        self.coordinator = CoordinatorAgent()
        self.setup_research_team()
    
    def setup_research_team(self):
        """Setup research team with specialized agents"""
        
        # Lead Researcher
        lead_researcher = Agent(
            name="lead_researcher",
            description="Leads research efforts and coordinates team",
            model="gemini-pro",
            tools=[
                TaskAssignmentTool(),
                ResearchTool(),
                ValidationTool()
            ]
        )
        
        # Data Collector
        data_collector = Agent(
            name="data_collector",
            description="Collects and organizes research data",
            model="text-bison@001",
            tools=[
                WebScraperTool(),
                DatabaseTool(),
                FileProcessorTool()
            ]
        )
        
        # Analyst
        analyst = Agent(
            name="analyst",
            description="Analyzes collected data and identifies patterns",
            model="gemini-pro",
            tools=[
                StatisticalTool(),
                VisualizationTool(),
                PatternRecognitionTool()
            ]
        )
        
        # Report Writer
        report_writer = Agent(
            name="report_writer",
            description="Writes comprehensive research reports",
            model="text-bison@001",
            tools=[
                DocumentGeneratorTool(),
                FormattingTool(),
                CitationTool()
            ]
        )
        
        # Register agents
        self.agents = {
            "lead_researcher": lead_researcher,
            "data_collector": data_collector,
            "analyst": analyst,
            "report_writer": report_writer
        }
    
    def conduct_research(self, research_topic: str) -> dict:
        """Conduct comprehensive research on topic"""
        
        # Phase 1: Planning
        plan = self.coordinator.coordinate_task({
            "type": "research_planning",
            "topic": research_topic,
            "required_agents": ["lead_researcher", "data_collector", "analyst", "report_writer"]
        })
        
        # Phase 2: Data Collection
        data_collection = self.agents["data_collector"].run(
            f"Collect comprehensive data on: {research_topic}"
        )
        
        # Phase 3: Analysis
        analysis = self.agents["analyst"].run(
            f"Analyze collected data on: {research_topic}",
            data=data_collection
        )
        
        # Phase 4: Report Generation
        report = self.agents["report_writer"].run(
            f"Write comprehensive research report on: {research_topic}",
            data=data_collection,
            analysis=analysis
        )
        
        return {
            "topic": research_topic,
            "plan": plan,
            "data": data_collection,
            "analysis": analysis,
            "report": report,
            "participants": list(self.agents.keys())
        }

# Usage
research_team = ResearchTeamSystem()
results = research_team.conduct_research("Impact of AI on healthcare")
```

### 2. **Customer Service System**
Multi-agent system for customer support

```python
class CustomerServiceSystem:
    def __init__(self):
        self.agents = {}
        self.setup_service_team()
    
    def setup_service_team(self):
        """Setup customer service team"""
        
        # Triage Agent
        triage_agent = Agent(
            name="triage",
            description="Categorizes and routes customer inquiries",
            model="gemini-pro",
            tools=[
                IntentClassifierTool(),
                RoutingTool(),
                PriorityTool()
            ]
        )
        
        # Technical Support Agent
        tech_agent = Agent(
            name="tech_support",
            description="Handles technical support inquiries",
            model="gemini-pro",
            tools=[
                DiagnosticTool(),
                KnowledgeBaseTool(),
                RemoteAccessTool()
            ]
        )
        
        # Billing Agent
        billing_agent = Agent(
            name="billing",
            description="Handles billing and account inquiries",
            model="text-bison@001",
            tools=[
                AccountTool(),
                BillingTool(),
                PaymentTool()
            ]
        )
        
        # Escalation Agent
        escalation_agent = Agent(
            name="escalation",
            description="Handles escalated and complex issues",
            model="gemini-pro",
            tools=[
                CaseManagementTool(),
                HumanHandoffTool(),
                SupervisorNotificationTool()
            ]
        )
        
        self.agents = {
            "triage": triage_agent,
            "tech_support": tech_agent,
            "billing": billing_agent,
            "escalation": escalation_agent
        }
    
    def handle_customer_inquiry(self, inquiry: dict) -> dict:
        """Handle customer inquiry through multi-agent system"""
        
        # Step 1: Triage
        triage_result = self.agents["triage"].run(
            f"Triage customer inquiry: {inquiry['message']}",
            customer_info=inquiry.get("customer_info", {})
        )
        
        # Step 2: Route to appropriate agent
        if triage_result["category"] == "technical":
            response = self.agents["tech_support"].run(
                inquiry["message"],
                customer_info=inquiry.get("customer_info", {}),
                triage_info=triage_result
            )
        elif triage_result["category"] == "billing":
            response = self.agents["billing"].run(
                inquiry["message"],
                customer_info=inquiry.get("customer_info", {}),
                triage_info=triage_result
            )
        else:
            # Escalate for unknown categories
            response = self.agents["escalation"].run(
                inquiry["message"],
                customer_info=inquiry.get("customer_info", {}),
                triage_info=triage_result
            )
        
        return {
            "inquiry_id": inquiry.get("id"),
            "triage": triage_result,
            "response": response,
            "handled_by": response.get("agent", "escalation"),
            "resolution": response.get("status", "pending")
        }

# Usage
customer_service = CustomerServiceSystem()

inquiry = {
    "id": "REQ-001",
    "message": "I can't access my account and need help with billing",
    "customer_info": {
        "customer_id": "CUST-123",
        "account_type": "premium"
    }
}

result = customer_service.handle_customer_inquiry(inquiry)
```

---

## 🎯 Best Practices

### 1. **System Design**
- **Clear Roles**: Define specific responsibilities for each agent
- **Loose Coupling**: Minimize dependencies between agents
- **Scalable Architecture**: Design for easy addition/removal of agents
- **Fault Tolerance**: Handle agent failures gracefully

### 2. **Communication**
- **Standardized Protocols**: Use consistent message formats
- **Async Communication**: Use non-blocking communication patterns
- **Message Validation**: Validate all inter-agent messages
- **Conflict Resolution**: Implement strategies for handling disagreements

### 3. **Coordination**
- **Centralized Orchestration**: Use coordinator for complex workflows
- **Decentralized Decision Making**: Allow agents to make local decisions
- **Dynamic Assignment**: Assign tasks based on agent capabilities and availability
- **Load Balancing**: Distribute workload evenly across agents

### 4. **Monitoring**
- **Agent Health**: Monitor individual agent performance
- **System Metrics**: Track overall system performance
- **Bottleneck Detection**: Identify performance bottlenecks
- **Audit Logging**: Log all inter-agent communications

---

## 📚 Next Steps

1. **Build Multi-Agent Systems** → Create your own agent teams
2. **Implement Communication** → Set up agent communication protocols
3. **Design Workflows** → Create orchestration patterns
4. **Deploy to Production** → Scale multi-agent systems

---

**🤖 Build powerful collaborative AI systems with multiple agents!**
