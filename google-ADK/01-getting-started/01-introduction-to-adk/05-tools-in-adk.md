# Tools in ADK

> **Extending agent capabilities with tools and functions**

Tools are the bridge between AI agents and the external world. They enable agents to perform actions, access data, and interact with systems beyond their internal knowledge.

---

## 🎯 What are Tools?

### Definition
A **Tool** in Google ADK is a callable function or service that an agent can use to:
- **Access External Data**: Query databases, APIs, web services
- **Perform Actions**: Send emails, create files, execute code
- **Process Information**: Analyze data, transform content
- **Interact with Systems**: Control devices, manage workflows

### Tool Components
```
┌─────────────────────────────────────────────────────────┐
│                     Tool                              │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   Function   │────────►│   Tool Definition   │
│   Logic      │         │   (Name, Desc)      │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Parameter         │
                         │   Validation        │
                         │  (Types, Rules)    │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Execution         │
                         │   Context          │
                         │  (Timeout, Retry)   │
                         └──────────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Result           │
                         │   Processing       │
                         │  (Format, Error)    │
                         └──────────────────────┘
```

---

## 🛠️ Built-in Tools

### 1. **Search Tools**
Access information from various sources

```python
from google_adk import Agent
from google_adk.tools import GoogleSearchTool, WebCrawlerTool

# Agent with search capabilities
search_agent = Agent(
    name="search_agent",
    description="Agent that can search the web",
    model="text-bison@001",
    tools=[
        GoogleSearchTool(),      # Google Search
        WebCrawlerTool(),       # Web crawling
        NewsSearchTool(),       # News search
        ScholarSearchTool()     # Academic search
    ],
    instructions="Use search tools to find current and accurate information."
)

# Usage
response = search_agent.run("Find latest news about AI technology")
# Agent will search and provide results
```

### 2. **Computation Tools**
Perform mathematical and data operations

```python
from google_adk.tools import CalculatorTool, DataAnalyzerTool

# Agent with computation capabilities
math_agent = Agent(
    name="math_agent",
    description="Agent that can perform calculations",
    model="text-bison@001",
    tools=[
        CalculatorTool(),      # Basic calculations
        DataAnalyzerTool(),    # Statistical analysis
        PlotTool(),           # Create charts
        ExcelTool()           # Excel operations
    ],
    instructions="Use computation tools for math and data analysis."
)

# Usage
response = math_agent.run("Calculate the average of [1, 2, 3, 4, 5]")
# Agent will calculate and return result
```

### 3. **Communication Tools**
Send messages and notifications

```python
from google_adk.tools import EmailTool, SlackTool, SMSTool

# Agent with communication capabilities
communication_agent = Agent(
    name="communication_agent",
    description="Agent that can send messages",
    model="text-bison@001",
    tools=[
        EmailTool(),          # Send emails
        SlackTool(),          # Send Slack messages
        SMSTool(),           # Send SMS messages
        CalendarTool()         # Calendar operations
    ],
    instructions="Use communication tools to send notifications and messages."
)

# Usage
response = communication_agent.run("Send an email to user@example.com about the meeting")
# Agent will compose and send email
```

### 4. **File Operations Tools**
Work with files and storage

```python
from google_adk.tools import FileReaderTool, FileWriterTool, CloudStorageTool

# Agent with file capabilities
file_agent = Agent(
    name="file_agent",
    description="Agent that can work with files",
    model="text-bison@001",
    tools=[
        FileReaderTool(),      # Read files
        FileWriterTool(),     # Write files
        CloudStorageTool(),   # Cloud storage operations
        PDFTool()            # PDF operations
    ],
    instructions="Use file tools to read, write, and manage files."
)

# Usage
response = file_agent.run("Read the contents of report.txt and summarize it")
# Agent will read file and provide summary
```

---

## 🔧 Custom Tools

### 1. **Basic Custom Tool**
Create a simple custom tool

```python
from google_adk import Tool

def weather_forecast(location: str, days: int = 7) -> dict:
    """
    Get weather forecast for a location
    
    Args:
        location: City name or coordinates
        days: Number of days to forecast (1-14)
    
    Returns:
        Dictionary with weather information
    """
    
    # Implementation - call weather API
    import requests
    
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        return {
            "location": data["location"]["name"],
            "current": data["current"]["temp_c"],
            "forecast": data["forecast"]["forecastday"],
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }

# Create tool
weather_tool = Tool(
    func=weather_forecast,
    name="weather_forecast",
    description="Get weather forecast for any location",
    parameters={
        "location": {
            "type": "string",
            "description": "City name or coordinates",
            "required": True
        },
        "days": {
            "type": "integer",
            "description": "Number of days to forecast",
            "default": 7,
            "min": 1,
            "max": 14
        }
    }
)

# Use in agent
weather_agent = Agent(
    name="weather_agent",
    description="Agent that provides weather information",
    model="text-bison@001",
    tools=[weather_tool],
    instructions="Use weather_forecast tool to provide weather information."
)
```

### 2. **Advanced Custom Tool**
Tool with complex parameters and validation

```python
from google_adk import Tool
from typing import Dict, List, Optional
import re

def database_query(
    table: str,
    query_type: str = "SELECT",
    conditions: Optional[Dict[str, any]] = None,
    limit: int = 100,
    order_by: Optional[str] = None
) -> List[Dict]:
    """
    Execute database query with safety validation
    
    Args:
        table: Database table name
        query_type: Type of query (SELECT, INSERT, UPDATE, DELETE)
        conditions: Dictionary of WHERE conditions
        limit: Maximum number of results
        order_by: Column to order by
    
    Returns:
        List of database records
    """
    
    # Validate table name
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table):
        raise ValueError("Invalid table name")
    
    # Validate query type
    allowed_queries = ["SELECT", "INSERT", "UPDATE", "DELETE"]
    if query_type not in allowed_queries:
        raise ValueError(f"Query type must be one of: {allowed_queries}")
    
    # Build safe query
    if query_type == "SELECT":
        query = f"SELECT * FROM {table}"
        
        if conditions:
            where_clauses = []
            for key, value in conditions.items():
                where_clauses.append(f"{key} = '{value}'")
            query += f" WHERE {' AND '.join(where_clauses)}"
        
        if order_by:
            query += f" ORDER BY {order_by}"
        
        query += f" LIMIT {limit}"
        
        # Execute query (implementation depends on your database)
        # results = execute_query(query)
        results = []  # Placeholder
        
        return results
    
    else:
        raise NotImplementedError(f"Query type {query_type} not implemented")

# Create advanced tool
db_tool = Tool(
    func=database_query,
    name="database_query",
    description="Execute safe database queries",
    parameters={
        "table": {
            "type": "string",
            "description": "Database table name",
            "required": True,
            "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
        },
        "query_type": {
            "type": "string",
            "description": "Type of query",
            "enum": ["SELECT", "INSERT", "UPDATE", "DELETE"],
            "default": "SELECT"
        },
        "conditions": {
            "type": "object",
            "description": "WHERE conditions as key-value pairs",
            "additionalProperties": True
        },
        "limit": {
            "type": "integer",
            "description": "Maximum number of results",
            "default": 100,
            "min": 1,
            "max": 1000
        },
        "order_by": {
            "type": "string",
            "description": "Column to order by",
            "optional": True
        }
    },
    safety_checks=[
        "sql_injection_protection",
        "parameter_validation",
        "query_logging"
    ]
)
```

### 3. **Tool with External API**
Integrate with external services

```python
import requests
import json
from google_adk import Tool

def slack_message(
    channel: str,
    message: str,
    webhook_url: str = None
) -> dict:
    """
    Send message to Slack channel
    
    Args:
        channel: Slack channel name
        message: Message to send
        webhook_url: Slack webhook URL (optional, uses default)
    
    Returns:
        Dictionary with response status
    """
    
    # Get webhook URL from environment if not provided
    if not webhook_url:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    
    if not webhook_url:
        return {
            "error": "No webhook URL provided",
            "success": False
        }
    
    # Prepare payload
    payload = {
        "channel": channel,
        "text": message
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            return {
                "message": "Message sent successfully",
                "channel": channel,
                "success": True
            }
        else:
            return {
                "error": f"Failed to send message: {response.status_code}",
                "success": False
            }
    
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }

# Create Slack tool
slack_tool = Tool(
    func=slack_message,
    name="send_slack_message",
    description="Send message to Slack channel",
    parameters={
        "channel": {
            "type": "string",
            "description": "Slack channel name (e.g., #general)",
            "required": True
        },
        "message": {
            "type": "string",
            "description": "Message to send",
            "required": True,
            "max_length": 4000
        },
        "webhook_url": {
            "type": "string",
            "description": "Slack webhook URL",
            "required": False,
            "format": "uri"
        }
    },
    rate_limit={
        "max_calls": 60,
        "time_window": 60  # 60 calls per minute
    }
)
```

---

## 🔗 Tool Composition

### 1. **Sequential Tool Chain**
Execute tools in sequence

```python
from google_adk import ToolChain

# Create tool chain
research_chain = ToolChain([
    ("search", GoogleSearchTool()),
    ("analyze", DataAnalyzerTool()),
    ("summarize", SummarizeTool()),
    ("report", ReportGeneratorTool())
])

# Use tool chain
def research_topic(topic: str) -> str:
    """Research a topic using multiple tools"""
    
    # Step 1: Search for information
    search_results = GoogleSearchTool().search(topic)
    
    # Step 2: Analyze the data
    analysis = DataAnalyzerTool().analyze(search_results)
    
    # Step 3: Summarize findings
    summary = SummarizeTool().summarize(analysis)
    
    # Step 4: Generate report
    report = ReportGeneratorTool().generate(summary)
    
    return report

# Create composed tool
research_tool = Tool(
    func=research_topic,
    name="research_topic",
    description="Comprehensive research using multiple tools"
)
```

### 2. **Conditional Tool Selection**
Choose tools based on conditions

```python
def conditional_tool_executor(input_text: str) -> str:
    """Execute different tools based on input"""
    
    # Analyze input type
    if "calculate" in input_text.lower() or "math" in input_text.lower():
        return CalculatorTool().calculate(input_text)
    
    elif "search" in input_text.lower() or "find" in input_text.lower():
        query = input_text.lower().replace("search", "").replace("find", "").strip()
        return GoogleSearchTool().search(query)
    
    elif "weather" in input_text.lower():
        # Extract location
        import re
        location_match = re.search(r'weather in ([a-zA-Z\s]+)', input_text, re.IGNORECASE)
        if location_match:
            location = location_match.group(1)
            return WeatherTool().get_forecast(location)
    
    else:
        return "I'm not sure which tool to use for this request."

# Create conditional tool
conditional_tool = Tool(
    func=conditional_tool_executor,
    name="conditional_executor",
    description="Execute appropriate tool based on input"
)
```

### 3. **Parallel Tool Execution**
Run multiple tools simultaneously

```python
from google_adk import ParallelToolExecutor
import asyncio

async def parallel_analysis(text: str) -> dict:
    """Run multiple analysis tools in parallel"""
    
    # Create tasks
    tasks = [
        SentimentTool().analyze(text),
        KeywordTool().extract(text),
        EntityTool().extract(text),
        LanguageTool().detect(text)
    ]
    
    # Execute in parallel
    results = await asyncio.gather(*tasks)
    
    return {
        "sentiment": results[0],
        "keywords": results[1],
        "entities": results[2],
        "language": results[3]
    }

# Create parallel tool
parallel_tool = Tool(
    func=parallel_analysis,
    name="parallel_analysis",
    description="Run multiple analysis tools in parallel"
)
```

---

## 🛡️ Tool Security

### 1. **Input Validation**
Ensure safe tool usage

```python
from google_adk import Tool, InputValidator

def safe_file_operation(filename: str, operation: str, content: str = None) -> dict:
    """Perform safe file operations"""
    
    # Validate filename
    if not InputValidator.is_safe_filename(filename):
        return {
            "error": "Unsafe filename detected",
            "success": False
        }
    
    # Validate operation
    allowed_operations = ["read", "write", "append", "delete"]
    if operation not in allowed_operations:
        return {
            "error": f"Operation '{operation}' not allowed",
            "success": False
        }
    
    # Validate content for write operations
    if operation in ["write", "append"] and content:
        if not InputValidator.is_safe_content(content):
            return {
                "error": "Unsafe content detected",
                "success": False
            }
    
    # Execute operation
    try:
        if operation == "read":
            with open(filename, 'r') as f:
                content = f.read()
            return {"content": content, "success": True}
        
        elif operation == "write":
            with open(filename, 'w') as f:
                f.write(content)
            return {"message": f"File {filename} written", "success": True}
        
        # ... other operations
    
    except Exception as e:
        return {"error": str(e), "success": False}

# Create safe tool
safe_file_tool = Tool(
    func=safe_file_operation,
    name="safe_file_operation",
    description="Perform safe file operations",
    safety_checks=[
        "filename_validation",
        "operation_validation",
        "content_validation",
        "path_traversal_protection"
    ]
)
```

### 2. **Rate Limiting**
Prevent tool abuse

```python
from google_adk import Tool, RateLimiter

# Create rate limiter
api_rate_limiter = RateLimiter(
    max_calls=100,
    time_window=3600,  # 100 calls per hour
    per_user=True
)

def rate_limited_api_call(endpoint: str, params: dict) -> dict:
    """Make rate-limited API calls"""
    
    # Check rate limit
    if not api_rate_limiter.is_allowed():
        return {
            "error": "Rate limit exceeded. Please try again later.",
            "success": False
        }
    
    # Make API call
    try:
        response = requests.get(endpoint, params=params, timeout=30)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"API error: {response.status_code}",
                "success": False
            }
    
    except Exception as e:
        return {"error": str(e), "success": False}

# Create rate-limited tool
api_tool = Tool(
    func=rate_limited_api_call,
    name="api_call",
    description="Make rate-limited API calls",
    rate_limit={
        "max_calls": 100,
        "time_window": 3600,
        "per_user": True
    }
)
```

### 3. **Authentication & Authorization**
Secure tool access

```python
from google_adk import Tool, AuthManager

def authenticated_database_operation(
    operation: str,
    table: str,
    data: dict = None,
    user_token: str = None
) -> dict:
    """Perform authenticated database operations"""
    
    # Validate user token
    if not AuthManager.validate_token(user_token):
        return {
            "error": "Invalid or expired token",
            "success": False
        }
    
    # Check user permissions
    user_permissions = AuthManager.get_permissions(user_token)
    
    if not AuthManager.can_access_table(user_permissions, table):
        return {
            "error": "Insufficient permissions for this table",
            "success": False
        }
    
    # Execute operation
    try:
        if operation == "SELECT":
            # Execute SELECT with user's row-level security
            results = execute_secure_select(table, user_token)
            return {"data": results, "success": True}
        
        elif operation == "INSERT":
            if AuthManager.can_insert(user_permissions, table):
                result = execute_secure_insert(table, data, user_token)
                return {"message": "Data inserted", "success": True}
            else:
                return {"error": "No INSERT permission", "success": False}
        
        # ... other operations
    
    except Exception as e:
        return {"error": str(e), "success": False}

# Create authenticated tool
auth_db_tool = Tool(
    func=authenticated_database_operation,
    name="authenticated_db_operation",
    description="Perform authenticated database operations",
    authentication={
        "required": True,
        "token_validation": True,
        "permission_check": True,
        "audit_logging": True
    }
)
```

---

## 📊 Tool Monitoring

### 1. **Usage Tracking**
Monitor tool performance

```python
from google_adk import ToolMonitor

# Create tool monitor
monitor = ToolMonitor(
    metrics=["usage_count", "response_time", "error_rate", "success_rate"],
    log_file="tool_usage.log"
)

def monitored_tool_function(input_data: dict) -> dict:
    """Tool function with monitoring"""
    
    start_time = time.time()
    
    try:
        # Execute tool logic
        result = actual_tool_logic(input_data)
        
        # Log success
        monitor.log_usage(
            tool_name="monitored_tool",
            success=True,
            response_time=time.time() - start_time,
            input_size=len(str(input_data)),
            output_size=len(str(result))
        )
        
        return result
    
    except Exception as e:
        # Log error
        monitor.log_usage(
            tool_name="monitored_tool",
            success=False,
            response_time=time.time() - start_time,
            error=str(e)
        )
        
        return {"error": str(e), "success": False}

# Create monitored tool
monitored_tool = Tool(
    func=monitored_tool_function,
    name="monitored_tool",
    description="Tool with usage monitoring",
    monitoring={
        "enabled": True,
        "metrics": ["usage", "performance", "errors"],
        "alert_threshold": {
            "error_rate": 0.05,  # Alert if error rate > 5%
            "response_time": 5.0  # Alert if response time > 5 seconds
        }
    }
)
```

### 2. **Performance Optimization**
Improve tool performance

```python
from google_adk import Tool, CacheManager

# Create cache manager
cache = CacheManager(
    ttl=3600,  # Cache for 1 hour
    max_size=1000
)

def cached_api_call(endpoint: str, params: dict) -> dict:
    """API call with caching"""
    
    # Create cache key
    cache_key = f"{endpoint}:{hash(str(sorted(params.items())))}"
    
    # Check cache
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result
    
    # Make API call
    result = make_actual_api_call(endpoint, params)
    
    # Cache result
    cache.set(cache_key, result)
    
    return result

# Create cached tool
cached_tool = Tool(
    func=cached_api_call,
    name="cached_api_call",
    description="API call with caching",
    optimization={
        "caching": True,
        "cache_ttl": 3600,
        "compression": True,
        "batch_processing": True
    }
)
```

---

## 🎯 Best Practices

### 1. **Tool Design**
- **Single Responsibility**: Each tool does one thing well
- **Clear Interface**: Well-defined inputs and outputs
- **Error Handling**: Graceful error recovery
- **Documentation**: Clear descriptions and examples

### 2. **Security**
- **Input Validation**: Validate all inputs
- **Rate Limiting**: Prevent abuse
- **Authentication**: Secure access control
- **Audit Logging**: Track tool usage

### 3. **Performance**
- **Caching**: Cache frequently used results
- **Async Operations**: Use async for I/O operations
- **Batch Processing**: Process multiple items together
- **Monitoring**: Track performance metrics

### 4. **Maintenance**
- **Version Control**: Track tool versions
- **Testing**: Comprehensive test coverage
- **Documentation**: Keep docs up to date
- **Monitoring**: Track tool health

---

## 📚 Next Steps

1. **Build Custom Tools** → Create tools for your specific needs
2. **Combine Tools** → Learn tool composition patterns
3. **Secure Tools** → Implement security best practices
4. **Monitor Performance** → Track and optimize tool usage

---

**🛠️ Extend your agents with powerful tools!**
