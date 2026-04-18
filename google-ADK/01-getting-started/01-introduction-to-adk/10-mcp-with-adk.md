# MCP with ADK

> **Integrating Model Context Protocol with Google ADK**

MCP (Model Context Protocol) enables standardized communication between AI models and external tools/services. Google ADK provides robust MCP integration for building extensible AI systems.

---

## 🎯 What is MCP?

### Definition
**MCP (Model Context Protocol)** is a standardized protocol that:
- **Standardizes Communication**: Common interface for model-tool interactions
- **Enables Interoperability**: Tools work across different AI systems
- **Provides Context Management**: Standardized context sharing
- **Supports Discovery**: Automatic tool and capability discovery
- **Facilitates Composition**: Easy tool combination and chaining

### MCP Architecture
```
┌─────────────────────────────────────────────────────────┐
│                MCP Ecosystem                      │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────────────┐
│   AI Model   │◄────────►│   MCP Server        │
│   (ADK)     │         │   (Protocol Layer)  │
└──────────────┘         └──────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────┐
│                MCP Tools                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │  Tool A  │ │  Tool B  │ │  Tool C  │ ...  │
│  │ (Search) │ │ (Calc)  │ │ (API)   │      │
│  └──────────┘ └──────────┘ └──────────┘      │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 MCP Integration in ADK

### 1. **MCP Server Setup**
Configure MCP server for ADK

```python
from google_adk import MCPServer, MCPTool, MCPResource

class ADKMCPServer(MCPServer):
    def __init__(self):
        super().__init__(
            name="adk-mcp-server",
            version="1.0.0",
            description="Google ADK MCP Server"
        )
        self.setup_mcp_tools()
        self.setup_mcp_resources()
    
    def setup_mcp_tools(self):
        """Setup MCP-compliant tools"""
        
        # Search tool
        search_tool = MCPTool(
            name="search",
            description="Search the web for information",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results",
                        "default": 10
                    }
                },
                "required": ["query"]
            },
            handler=self.handle_search_request
        )
        
        # Calculator tool
        calculator_tool = MCPTool(
            name="calculator",
            description="Perform mathematical calculations",
            input_schema={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            },
            handler=self.handle_calculation_request
        )
        
        # File operations tool
        file_tool = MCPTool(
            name="file_operations",
            description="Perform file operations",
            input_schema={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["read", "write", "delete", "list"],
                        "description": "File operation to perform"
                    },
                    "path": {
                        "type": "string",
                        "description": "File path"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content for write operations"
                    }
                },
                "required": ["operation", "path"]
            },
            handler=self.handle_file_request
        )
        
        # Register tools
        self.register_tool(search_tool)
        self.register_tool(calculator_tool)
        self.register_tool(file_tool)
    
    def setup_mcp_resources(self):
        """Setup MCP resources"""
        
        # Knowledge base resource
        knowledge_resource = MCPResource(
            name="knowledge_base",
            description="Access to knowledge base",
            uri="knowledge://base",
            mime_type="application/json",
            handler=self.handle_knowledge_request
        )
        
        # Configuration resource
        config_resource = MCPResource(
            name="configuration",
            description="System configuration",
            uri="config://system",
            mime_type="application/json",
            handler=self.handle_config_request
        )
        
        # Register resources
        self.register_resource(knowledge_resource)
        self.register_resource(config_resource)
    
    def handle_search_request(self, arguments: dict) -> dict:
        """Handle search requests via MCP"""
        
        query = arguments.get("query")
        max_results = arguments.get("max_results", 10)
        
        # Perform search
        search_results = self.perform_search(query, max_results)
        
        return {
            "results": search_results,
            "query": query,
            "total_results": len(search_results),
            "timestamp": datetime.now().isoformat()
        }
    
    def handle_calculation_request(self, arguments: dict) -> dict:
        """Handle calculation requests via MCP"""
        
        expression = arguments.get("expression")
        
        try:
            # Safe evaluation
            result = eval(expression, {"__builtins__": {}}, {})
            
            return {
                "result": result,
                "expression": expression,
                "status": "success"
            }
        except Exception as e:
            return {
                "error": str(e),
                "expression": expression,
                "status": "error"
            }
    
    def handle_file_request(self, arguments: dict) -> dict:
        """Handle file operation requests via MCP"""
        
        operation = arguments.get("operation")
        path = arguments.get("path")
        content = arguments.get("content")
        
        try:
            if operation == "read":
                result = self.read_file(path)
            elif operation == "write":
                result = self.write_file(path, content)
            elif operation == "delete":
                result = self.delete_file(path)
            elif operation == "list":
                result = self.list_files(path)
            else:
                raise ValueError(f"Unknown operation: {operation}")
            
            return {
                "result": result,
                "operation": operation,
                "path": path,
                "status": "success"
            }
        
        except Exception as e:
            return {
                "error": str(e),
                "operation": operation,
                "path": path,
                "status": "error"
            }

# Create and start MCP server
mcp_server = ADKMCPServer()
mcp_server.start(host="localhost", port=8080)
```

### 2. **MCP Client Integration**
Connect ADK agents to MCP servers

```python
from google_adk import MCPClient, MCPConnection

class ADKMCPClient(MCPClient):
    def __init__(self, server_url: str):
        super().__init__(server_url)
        self.available_tools = {}
        self.available_resources = {}
    
    async def connect_to_server(self):
        """Connect to MCP server"""
        
        try:
            # Establish connection
            await self.establish_connection()
            
            # Discover available tools
            await self.discover_tools()
            
            # Discover available resources
            await self.discover_resources()
            
            print(f"✅ Connected to MCP server: {self.server_url}")
            print(f"📦 Available tools: {len(self.available_tools)}")
            print(f"📁 Available resources: {len(self.available_resources)}")
            
        except Exception as e:
            print(f"❌ Failed to connect to MCP server: {e}")
            raise
    
    async def discover_tools(self):
        """Discover available tools from MCP server"""
        
        tools_response = await self.send_request({
            "method": "tools/list",
            "params": {}
        })
        
        if tools_response.get("success"):
            for tool_info in tools_response.get("tools", []):
                self.available_tools[tool_info["name"]] = tool_info
    
    async def discover_resources(self):
        """Discover available resources from MCP server"""
        
        resources_response = await self.send_request({
            "method": "resources/list",
            "params": {}
        })
        
        if resources_response.get("success"):
            for resource_info in resources_response.get("resources", []):
                self.available_resources[resource_info["name"]] = resource_info
    
    async def call_tool(self, tool_name: str, arguments: dict) -> dict:
        """Call tool via MCP"""
        
        if tool_name not in self.available_tools:
            raise ValueError(f"Tool {tool_name} not available")
        
        tool_call = {
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        response = await self.send_request(tool_call)
        
        return response
    
    async def access_resource(self, resource_name: str, params: dict = None) -> dict:
        """Access resource via MCP"""
        
        if resource_name not in self.available_resources:
            raise ValueError(f"Resource {resource_name} not available")
        
        resource_call = {
            "method": "resources/read",
            "params": {
                "name": resource_name,
                "params": params or {}
            }
        }
        
        response = await self.send_request(resource_call)
        
        return response

# Usage
async def main():
    # Create MCP client
    client = ADKMCPClient("http://localhost:8080")
    
    # Connect to server
    await client.connect_to_server()
    
    # Use tools
    search_result = await client.call_tool("search", {
        "query": "artificial intelligence trends",
        "max_results": 5
    })
    
    calc_result = await client.call_tool("calculator", {
        "expression": "2 + 2 * 3"
    })
    
    # Access resources
    knowledge = await client.access_resource("knowledge_base")
    
    print(f"Search results: {search_result}")
    print(f"Calculation result: {calc_result}")
    print(f"Knowledge base: {knowledge}")

# Run MCP client
# asyncio.run(main())
```

---

## 🤖 ADK Agents with MCP

### 1. **MCP-Enabled Agent**
Agent that uses MCP tools

```python
from google_adk import Agent, MCPClient

class MCPEnabledAgent(Agent):
    def __init__(self, mcp_server_url: str):
        super().__init__(
            name="mcp_enabled_agent",
            description="Agent with MCP tool integration",
            model="gemini-pro"
        )
        self.mcp_client = None
        self.mcp_server_url = mcp_server_url
    
    async def initialize(self):
        """Initialize agent with MCP connection"""
        
        # Connect to MCP server
        self.mcp_client = ADKMCPClient(self.mcp_server_url)
        await self.mcp_client.connect_to_server()
        
        # Register MCP tools as agent tools
        await self.register_mcp_tools()
    
    async def register_mcp_tools(self):
        """Register MCP tools as agent tools"""
        
        for tool_name, tool_info in self.mcp_client.available_tools.items():
            # Create MCP tool wrapper
            mcp_tool = self.create_mcp_tool_wrapper(tool_name, tool_info)
            self.add_tool(mcp_tool)
    
    def create_mcp_tool_wrapper(self, tool_name: str, tool_info: dict):
        """Create wrapper for MCP tool"""
        
        async def mcp_tool_wrapper(**kwargs):
            """Wrapper function for MCP tool call"""
            
            try:
                # Call MCP tool
                result = await self.mcp_client.call_tool(tool_name, kwargs)
                
                if result.get("success"):
                    return result.get("result")
                else:
                    raise Exception(f"MCP tool error: {result.get('error')}")
            
            except Exception as e:
                return f"Error calling MCP tool {tool_name}: {str(e)}"
        
        # Create ADK tool
        from google_adk import Tool
        return Tool(
            func=mcp_tool_wrapper,
            name=f"mcp_{tool_name}",
            description=tool_info.get("description", f"MCP tool: {tool_name}"),
            parameters=tool_info.get("input_schema", {})
        )
    
    async def run_with_mcp_tools(self, user_input: str) -> str:
        """Run agent with MCP tools"""
        
        # Generate response using available MCP tools
        context = {
            "available_tools": list(self.mcp_client.available_tools.keys()),
            "available_resources": list(self.mcp_client.available_resources.keys())
        }
        
        response = await self.run(user_input, context=context)
        
        return response

# Usage
async def create_mcp_agent():
    """Create and use MCP-enabled agent"""
    
    agent = MCPEnabledAgent("http://localhost:8080")
    await agent.initialize()
    
    # Use agent
    response = await agent.run_with_mcp_tools(
        "Search for information about quantum computing and calculate the potential market size"
    )
    
    print(f"Agent response: {response}")

# Run MCP agent
# asyncio.run(create_mcp_agent())
```

### 2. **Multi-Server MCP Agent**
Agent that connects to multiple MCP servers

```python
class MultiServerMCPAgent(Agent):
    def __init__(self, server_urls: list):
        super().__init__(
            name="multi_server_mcp_agent",
            description="Agent with multiple MCP server connections",
            model="gemini-pro"
        )
        self.server_urls = server_urls
        self.mcp_clients = {}
        self.combined_tools = {}
    
    async def initialize(self):
        """Initialize connections to multiple MCP servers"""
        
        # Connect to all servers
        for url in self.server_urls:
            try:
                client = ADKMCPClient(url)
                await client.connect_to_server()
                self.mcp_clients[url] = client
                print(f"✅ Connected to MCP server: {url}")
            except Exception as e:
                print(f"❌ Failed to connect to {url}: {e}")
        
        # Combine tools from all servers
        await self.combine_tools()
    
    async def combine_tools(self):
        """Combine tools from all MCP servers"""
        
        tool_counter = 0
        
        for server_url, client in self.mcp_clients.items():
            for tool_name, tool_info in client.available_tools.items():
                # Create unique tool name
                unique_name = f"{tool_name}_{tool_counter}"
                tool_counter += 1
                
                # Create tool wrapper
                tool_wrapper = self.create_multi_server_tool_wrapper(
                    unique_name, tool_name, tool_info, server_url, client
                )
                
                self.combined_tools[unique_name] = {
                    "wrapper": tool_wrapper,
                    "original_name": tool_name,
                    "server_url": server_url,
                    "tool_info": tool_info
                }
                
                self.add_tool(tool_wrapper)
    
    def create_multi_server_tool_wrapper(self, unique_name: str, original_name: str, 
                                       tool_info: dict, server_url: str, client):
        """Create wrapper for multi-server MCP tool"""
        
        async def multi_server_tool_wrapper(**kwargs):
            """Wrapper function for multi-server MCP tool"""
            
            try:
                # Call MCP tool on specific server
                result = await client.call_tool(original_name, kwargs)
                
                if result.get("success"):
                    return {
                        "result": result.get("result"),
                        "server": server_url,
                        "tool": original_name
                    }
                else:
                    raise Exception(f"MCP tool error: {result.get('error')}")
            
            except Exception as e:
                return {
                    "error": str(e),
                    "server": server_url,
                    "tool": original_name
                }
        
        # Create ADK tool
        from google_adk import Tool
        return Tool(
            func=multi_server_tool_wrapper,
            name=unique_name,
            description=f"MCP tool from {server_url}: {original_name}",
            parameters=tool_info.get("input_schema", {})
        )
    
    async def run_with_multi_server_tools(self, user_input: str) -> str:
        """Run agent with multi-server MCP tools"""
        
        # Create context with server information
        context = {
            "available_servers": list(self.mcp_clients.keys()),
            "total_tools": len(self.combined_tools),
            "server_tools": {
                url: len(client.available_tools) 
                for url, client in self.mcp_clients.items()
            }
        }
        
        response = await self.run(user_input, context=context)
        
        return response

# Usage
async def create_multi_server_agent():
    """Create agent with multiple MCP servers"""
    
    servers = [
        "http://localhost:8080",  # Local MCP server
        "http://tools.example.com:8080",  # External MCP server
        "http://company-tools.com:8080"  # Company MCP server
    ]
    
    agent = MultiServerMCPAgent(servers)
    await agent.initialize()
    
    # Use agent
    response = await agent.run_with_multi_server_tools(
        "Search for company data and calculate financial projections"
    )
    
    print(f"Multi-server agent response: {response}")

# Run multi-server agent
# asyncio.run(create_multi_server_agent())
```

---

## 🔧 MCP Tool Development

### 1. **Custom MCP Tool**
Create custom tools for MCP

```python
from google_adk import MCPTool, MCPToolHandler

class CustomMCPTools(MCPToolHandler):
    def __init__(self):
        self.tools = {}
        self.setup_custom_tools()
    
    def setup_custom_tools(self):
        """Setup custom MCP tools"""
        
        # Weather tool
        weather_tool = MCPTool(
            name="weather",
            description="Get weather information for any location",
            input_schema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name or coordinates"
                    },
                    "units": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "default": "metric",
                        "description": "Temperature units"
                    }
                },
                "required": ["location"]
            },
            handler=self.get_weather
        )
        
        # Stock price tool
        stock_tool = MCPTool(
            name="stock_price",
            description="Get current stock price",
            input_schema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol (e.g., AAPL, GOOGL)"
                    },
                    "currency": {
                        "type": "string",
                        "enum": ["USD", "EUR", "GBP"],
                        "default": "USD",
                        "description": "Currency for price"
                    }
                },
                "required": ["symbol"]
            },
            handler=self.get_stock_price
        )
        
        # Image analysis tool
        image_tool = MCPTool(
            name="analyze_image",
            description="Analyze image content",
            input_schema={
                "type": "object",
                "properties": {
                    "image_url": {
                        "type": "string",
                        "description": "URL of image to analyze"
                    },
                    "analysis_type": {
                        "type": "string",
                        "enum": ["objects", "text", "faces", "labels"],
                        "default": "objects",
                        "description": "Type of analysis to perform"
                    }
                },
                "required": ["image_url"]
            },
            handler=self.analyze_image
        )
        
        # Register tools
        self.tools["weather"] = weather_tool
        self.tools["stock_price"] = stock_tool
        self.tools["analyze_image"] = image_tool
    
    async def get_weather(self, arguments: dict) -> dict:
        """Get weather information"""
        
        location = arguments.get("location")
        units = arguments.get("units", "metric")
        
        try:
            # Call weather API
            weather_data = await self.call_weather_api(location, units)
            
            return {
                "location": location,
                "temperature": weather_data["temperature"],
                "condition": weather_data["condition"],
                "humidity": weather_data["humidity"],
                "units": units,
                "timestamp": datetime.now().isoformat()
            }
        
        except Exception as e:
            return {
                "error": str(e),
                "location": location
            }
    
    async def get_stock_price(self, arguments: dict) -> dict:
        """Get stock price information"""
        
        symbol = arguments.get("symbol")
        currency = arguments.get("currency", "USD")
        
        try:
            # Call stock API
            stock_data = await self.call_stock_api(symbol, currency)
            
            return {
                "symbol": symbol,
                "price": stock_data["price"],
                "currency": currency,
                "change": stock_data["change"],
                "change_percent": stock_data["change_percent"],
                "timestamp": datetime.now().isoformat()
            }
        
        except Exception as e:
            return {
                "error": str(e),
                "symbol": symbol
            }
    
    async def analyze_image(self, arguments: dict) -> dict:
        """Analyze image content"""
        
        image_url = arguments.get("image_url")
        analysis_type = arguments.get("analysis_type", "objects")
        
        try:
            # Call vision API
            analysis_result = await self.call_vision_api(image_url, analysis_type)
            
            return {
                "image_url": image_url,
                "analysis_type": analysis_type,
                "results": analysis_result,
                "confidence": analysis_result.get("confidence"),
                "timestamp": datetime.now().isoformat()
            }
        
        except Exception as e:
            return {
                "error": str(e),
                "image_url": image_url
            }
    
    async def call_weather_api(self, location: str, units: str) -> dict:
        """Call weather API"""
        # Implementation would call actual weather API
        return {
            "temperature": 22.5,
            "condition": "Partly cloudy",
            "humidity": 65
        }
    
    async def call_stock_api(self, symbol: str, currency: str) -> dict:
        """Call stock API"""
        # Implementation would call actual stock API
        return {
            "price": 150.25,
            "change": 2.50,
            "change_percent": 1.69
        }
    
    async def call_vision_api(self, image_url: str, analysis_type: str) -> dict:
        """Call vision API"""
        # Implementation would call actual vision API
        return {
            "objects": ["car", "building", "street"],
            "confidence": 0.92
        }

# Register custom tools with MCP server
custom_tools = CustomMCPTools()
for tool_name, tool in custom_tools.tools.items():
    mcp_server.register_tool(tool)
```

### 2. **MCP Resource Provider**
Provide resources through MCP

```python
from google_adk import MCPResource, MCPResourceHandler

class CustomMCPResources(MCPResourceHandler):
    def __init__(self):
        self.resources = {}
        self.setup_resources()
    
    def setup_resources(self):
        """Setup custom MCP resources"""
        
        # Knowledge base resource
        knowledge_resource = MCPResource(
            name="knowledge_base",
            description="Company knowledge base",
            uri="knowledge://company",
            mime_type="application/json",
            handler=self.get_knowledge_base
        )
        
        # Configuration resource
        config_resource = MCPResource(
            name="system_config",
            description="System configuration",
            uri="config://system",
            mime_type="application/json",
            handler=self.get_system_config
        )
        
        # Data source resource
        data_resource = MCPResource(
            name="data_source",
            description="Access to data sources",
            uri="data://sources",
            mime_type="application/json",
            handler=self.get_data_sources
        )
        
        # Register resources
        self.resources["knowledge_base"] = knowledge_resource
        self.resources["system_config"] = config_resource
        self.resources["data_source"] = data_resource
    
    async def get_knowledge_base(self, params: dict) -> dict:
        """Get knowledge base content"""
        
        category = params.get("category", "all")
        
        # Load knowledge base
        knowledge_data = self.load_knowledge_base()
        
        if category != "all":
            knowledge_data = {
                key: value for key, value in knowledge_data.items()
                if category in key.lower() or category == "all"
            }
        
        return {
            "data": knowledge_data,
            "category": category,
            "total_entries": len(knowledge_data),
            "timestamp": datetime.now().isoformat()
        }
    
    async def get_system_config(self, params: dict) -> dict:
        """Get system configuration"""
        
        config_key = params.get("key")
        
        # Load configuration
        config_data = self.load_system_config()
        
        if config_key:
            return {
                "key": config_key,
                "value": config_data.get(config_key),
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {
                "config": config_data,
                "total_keys": len(config_data),
                "timestamp": datetime.now().isoformat()
            }
    
    async def get_data_sources(self, params: dict) -> dict:
        """Get available data sources"""
        
        source_type = params.get("type", "all")
        
        # Load data sources
        data_sources = self.load_data_sources()
        
        if source_type != "all":
            data_sources = [
                source for source in data_sources
                if source.get("type") == source_type
            ]
        
        return {
            "sources": data_sources,
            "type": source_type,
            "total_sources": len(data_sources),
            "timestamp": datetime.now().isoformat()
        }
    
    def load_knowledge_base(self) -> dict:
        """Load knowledge base from storage"""
        # Implementation would load from database or file
        return {
            "company_info": "Founded in 2020, specializes in AI solutions",
            "products": ["ADK", "AI Agents", "MCP Integration"],
            "contact": "info@company.com",
            "support": "support@company.com"
        }
    
    def load_system_config(self) -> dict:
        """Load system configuration"""
        # Implementation would load from config file
        return {
            "max_concurrent_requests": 100,
            "default_timeout": 30,
            "log_level": "INFO",
            "cache_enabled": True,
            "cache_ttl": 3600
        }
    
    def load_data_sources(self) -> list:
        """Load data sources"""
        # Implementation would load from registry
        return [
            {
                "name": "customer_database",
                "type": "database",
                "description": "Customer information database",
                "access_level": "restricted"
            },
            {
                "name": "analytics_api",
                "type": "api",
                "description": "Analytics and metrics API",
                "access_level": "public"
            },
            {
                "name": "file_storage",
                "type": "storage",
                "description": "File storage system",
                "access_level": "authenticated"
            }
        ]

# Register custom resources with MCP server
custom_resources = CustomMCPResources()
for resource_name, resource in custom_resources.resources.items():
    mcp_server.register_resource(resource)
```

---

## 📊 MCP Monitoring & Management

### 1. **MCP Server Monitoring**
Monitor MCP server performance

```python
class MCPServerMonitor:
    def __init__(self, mcp_server):
        self.mcp_server = mcp_server
        self.metrics = {
            "requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "active_connections": 0,
            "tool_usage": {},
            "resource_usage": {}
        }
        self.start_time = time.time()
    
    def start_monitoring(self):
        """Start monitoring MCP server"""
        
        # Register request handlers
        self.mcp_server.register_request_handler(self.on_request)
        self.mcp_server.register_connection_handler(self.on_connection)
        self.mcp_server.register_tool_call_handler(self.on_tool_call)
        self.mcp_server.register_resource_access_handler(self.on_resource_access)
    
    def on_request(self, request_data: dict):
        """Handle incoming request"""
        
        self.metrics["requests"] += 1
        
        if request_data.get("success"):
            self.metrics["successful_requests"] += 1
        else:
            self.metrics["failed_requests"] += 1
        
        # Log request details
        self.log_request(request_data)
    
    def on_connection(self, connection_data: dict):
        """Handle connection events"""
        
        event_type = connection_data.get("type")
        
        if event_type == "connected":
            self.metrics["active_connections"] += 1
        elif event_type == "disconnected":
            self.metrics["active_connections"] = max(0, self.metrics["active_connections"] - 1)
        
        # Log connection event
        self.log_connection(connection_data)
    
    def on_tool_call(self, tool_call_data: dict):
        """Handle tool call events"""
        
        tool_name = tool_call_data.get("tool_name")
        
        if tool_name not in self.metrics["tool_usage"]:
            self.metrics["tool_usage"][tool_name] = 0
        
        self.metrics["tool_usage"][tool_name] += 1
        
        # Log tool call
        self.log_tool_call(tool_call_data)
    
    def on_resource_access(self, resource_data: dict):
        """Handle resource access events"""
        
        resource_name = resource_data.get("resource_name")
        
        if resource_name not in self.metrics["resource_usage"]:
            self.metrics["resource_usage"][resource_name] = 0
        
        self.metrics["resource_usage"][resource_name] += 1
        
        # Log resource access
        self.log_resource_access(resource_data)
    
    def get_metrics(self) -> dict:
        """Get current metrics"""
        
        uptime = time.time() - self.start_time
        
        return {
            "uptime_seconds": uptime,
            "total_requests": self.metrics["requests"],
            "successful_requests": self.metrics["successful_requests"],
            "failed_requests": self.metrics["failed_requests"],
            "success_rate": (
                self.metrics["successful_requests"] / max(1, self.metrics["requests"])
            ),
            "active_connections": self.metrics["active_connections"],
            "tool_usage": self.metrics["tool_usage"],
            "resource_usage": self.metrics["resource_usage"],
            "requests_per_minute": self.metrics["requests"] / (uptime / 60),
            "timestamp": datetime.now().isoformat()
        }
    
    def log_request(self, request_data: dict):
        """Log request details"""
        # Implementation would log to file or monitoring system
        pass
    
    def log_connection(self, connection_data: dict):
        """Log connection details"""
        # Implementation would log to file or monitoring system
        pass
    
    def log_tool_call(self, tool_call_data: dict):
        """Log tool call details"""
        # Implementation would log to file or monitoring system
        pass
    
    def log_resource_access(self, resource_data: dict):
        """Log resource access details"""
        # Implementation would log to file or monitoring system
        pass

# Setup monitoring
monitor = MCPServerMonitor(mcp_server)
monitor.start_monitoring()
```

---

## 🎯 Best Practices

### 1. **MCP Server Design**
- **Standard Compliance**: Follow MCP protocol specifications
- **Error Handling**: Provide clear error messages
- **Rate Limiting**: Implement appropriate rate limits
- **Security**: Validate all inputs and requests
- **Documentation**: Provide clear tool and resource documentation

### 2. **MCP Client Integration**
- **Connection Management**: Handle connection failures gracefully
- **Tool Discovery**: Dynamically discover available tools
- **Resource Caching**: Cache frequently accessed resources
- **Timeout Handling**: Set appropriate timeouts for operations
- **Retry Logic**: Implement retry mechanisms for failures

### 3. **Tool Development**
- **Input Validation**: Validate all tool inputs
- **Output Standards**: Return standardized output format
- **Error Handling**: Provide meaningful error messages
- **Performance**: Optimize tool execution time
- **Security**: Sanitize inputs and secure operations

### 4. **Resource Management**
- **Access Control**: Implement proper access controls
- **Versioning**: Track resource versions
- **Caching**: Cache resource data appropriately
- **Monitoring**: Track resource usage patterns
- **Backup**: Maintain backup copies of critical resources

---

## 📚 Next Steps

1. **Build MCP Servers** → Create custom MCP servers
2. **Develop MCP Tools** → Build specialized tools
3. **Integrate with ADK** → Connect agents to MCP ecosystems
4. **Deploy to Production** → Scale MCP deployments

---

**🔗 Master MCP integration for extensible AI systems!**
