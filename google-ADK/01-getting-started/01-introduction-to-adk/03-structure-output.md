# Structure Output in ADK

> **Controlling and formatting agent responses effectively**

Structured output is crucial for building reliable AI applications. Google ADK provides powerful mechanisms to ensure agents return responses in predictable, parseable formats.

---

## 🎯 Why Structured Output?

### Benefits
- **Reliability**: Consistent response format
- **Parseability**: Easy to extract information
- **Integration**: Seamless API integration
- **Validation**: Built-in format validation
- **Type Safety**: Defined data types
- **Documentation**: Self-documenting responses

### Common Use Cases
- **API Responses**: JSON for web APIs
- **Data Extraction**: Structured data from unstructured text
- **Form Filling**: Automated form completion
- **Report Generation**: Structured reports and summaries
- **Configuration**: Parameterized responses

---

## 🏗️ Output Structure Types

### 1. **JSON Output**
Most common structured format for APIs and data exchange

```python
from google_adk import Agent
from typing import Dict, Any

# Configure agent for JSON output
json_agent = Agent(
    name="json_agent",
    description="Agent that returns structured JSON responses",
    model="text-bison@001",
    output_format="json",
    instructions="""
    Always return responses in valid JSON format.
    
    Example structure:
    {
        "status": "success|error",
        "data": {...},
        "message": "Human-readable message",
        "timestamp": "ISO timestamp"
    }
    """,
    output_schema={
        "type": "object",
        "properties": {
            "status": {"type": "string", "enum": ["success", "error"]},
            "data": {"type": "object"},
            "message": {"type": "string"},
            "timestamp": {"type": "string", "format": "date-time"}
        },
        "required": ["status", "message"]
    }
)

# Example usage
response = json_agent.run("Analyze this customer feedback: 'Great product, fast shipping!'")
# Returns: {"status": "success", "data": {"sentiment": "positive"}, "message": "Analysis complete", "timestamp": "2024-01-15T10:30:00Z"}
```

### 2. **XML Output**
Useful for legacy systems and specific data formats

```python
xml_agent = Agent(
    name="xml_agent",
    description="Agent that returns XML responses",
    model="text-bison@001",
    output_format="xml",
    instructions="""
    Always return responses in valid XML format.
    
    Example structure:
    <response>
        <status>success</status>
        <data>
            <result>...</result>
        </data>
        <message>...</message>
    </response>
    """,
    output_schema="""
    <!DOCTYPE response [
        <!ELEMENT response (status, data, message)>
        <!ELEMENT status (#PCDATA)>
        <!ELEMENT data (result)>
        <!ELEMENT result (#PCDATA)>
        <!ELEMENT message (#PCDATA)>
    ]>
    """
)
```

### 3. **YAML Output**
Human-readable configuration format

```python
yaml_agent = Agent(
    name="yaml_agent",
    description="Agent that returns YAML responses",
    model="text-bison@001",
    output_format="yaml",
    instructions="""
    Always return responses in valid YAML format.
    
    Example structure:
    status: success
    data:
      result: ...
    message: ...
    """,
    output_schema={
        "status": "string",
        "data": {
            "result": "any"
        },
        "message": "string"
    }
)
```

### 4. **CSV Output**
For tabular data and spreadsheets

```python
csv_agent = Agent(
    name="csv_agent",
    description="Agent that returns CSV responses",
    model="text-bison@001",
    output_format="csv",
    instructions="""
    Always return responses in valid CSV format.
    
    Include headers in the first row.
    Use comma as delimiter.
    Escape commas and quotes properly.
    """,
    output_schema={
        "headers": ["name", "age", "city", "occupation"],
        "types": ["string", "integer", "string", "string"]
    }
)
```

---

## 📝 Output Templates

### 1. **Response Templates**
Predefined response structures

```python
from google_adk import OutputTemplate

# Define response template
response_template = OutputTemplate(
    name="api_response",
    template="""
    {
        "success": {success},
        "data": {data},
        "error": {error},
        "metadata": {
            "timestamp": "{timestamp}",
            "request_id": "{request_id}",
            "processing_time": {processing_time}
        }
    }
    """,
    schema={
        "success": "boolean",
        "data": "object",
        "error": "string|null",
        "metadata": {
            "timestamp": "string",
            "request_id": "string",
            "processing_time": "number"
        }
    }
)

# Use template in agent
template_agent = Agent(
    name="template_agent",
    description="Agent using response templates",
    model="text-bison@001",
    output_template=response_template,
    instructions="""
    Use the provided template for all responses.
    Fill in the template fields based on your analysis.
    """
)
```

### 2. **Dynamic Templates**
Templates with conditional logic

```python
dynamic_template = OutputTemplate(
    name="dynamic_response",
    template="""
    {
        "status": "{status}",
        "result": {result},
        {if error}
        "error": {
            "code": "{error_code}",
            "message": "{error_message}",
            "details": {error_details}
        },
        {endif}
        "recommendations": {recommendations}
    }
    """,
    conditions={
        "error": "has_error"
    }
)
```

---

## 🔧 Output Validation

### 1. **Schema Validation**
Ensure responses match expected structure

```python
from google_adk import OutputValidator

# Define validation schema
validation_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string", "pattern": "^USER_[0-9]+$"},
        "action": {"type": "string", "enum": ["create", "update", "delete"]},
        "parameters": {
            "type": "object",
            "additionalProperties": False
        },
        "timestamp": {"type": "string", "format": "date-time"}
    },
    "required": ["user_id", "action", "timestamp"]
}

# Create validator
validator = OutputValidator(schema=validation_schema)

# Use with agent
validated_agent = Agent(
    name="validated_agent",
    description="Agent with output validation",
    model="text-bison@001",
    output_validator=validator,
    instructions="""
    Always return responses that match the validation schema.
    If validation fails, retry with corrected format.
    """
)
```

### 2. **Custom Validation**
Business logic validation

```python
def validate_business_logic(response: Dict[str, Any]) -> bool:
    """Custom validation function"""
    
    # Check business rules
    if response.get("action") == "delete" and not response.get("confirmation"):
        return False
    
    if response.get("amount", 0) > 10000 and not response.get("approval"):
        return False
    
    return True

# Agent with custom validation
business_agent = Agent(
    name="business_agent",
    description="Agent with business logic validation",
    model="text-bison@001",
    custom_validator=validate_business_logic,
    instructions="""
    Follow business rules in your responses:
    - Delete actions require confirmation
    - Amounts over $10,000 require approval
    """
)
```

---

## 🎨 Output Formatting

### 1. **Pretty Printing**
Human-readable formatted output

```python
from google_adk import OutputFormatter

# Define pretty print formatter
pretty_formatter = OutputFormatter(
    name="pretty_print",
    format_function=lambda data: f"""
    ╔════════════════════════════════════════╗
    ║             ANALYSIS RESULTS              ║
    ╚════════════════════════════════════════╝
    
    Status: {data.get('status', 'N/A')}
    Confidence: {data.get('confidence', 'N/A')}%
    
    Key Findings:
    {chr(10).join(f"• {finding}" for finding in data.get('findings', []))}
    
    Recommendations:
    {chr(10).join(f"• {rec}" for rec in data.get('recommendations', []))}
    """
)

# Agent with pretty printing
pretty_agent = Agent(
    name="pretty_agent",
    description="Agent with formatted output",
    model="text-bison@001",
    output_formatter=pretty_formatter,
    instructions="""
    Provide analysis results in a structured format.
    Include status, confidence, findings, and recommendations.
    """
)
```

### 2. **Conditional Formatting**
Different formats based on content

```python
def conditional_formatter(data: Dict[str, Any]) -> str:
    """Format output based on data content"""
    
    if data.get("error"):
        return f"❌ ERROR: {data['error']}"
    
    if data.get("success"):
        return f"✅ SUCCESS: {data.get('message', 'Operation completed')}"
    
    if data.get("warning"):
        return f"⚠️  WARNING: {data['warning']}"
    
    return f"ℹ️  INFO: {data.get('message', 'No specific message')}"

# Agent with conditional formatting
conditional_agent = Agent(
    name="conditional_agent",
    description="Agent with conditional formatting",
    model="text-bison@001",
    output_formatter=conditional_formatter,
    instructions="""
    Provide responses that can be formatted based on content type.
    Include appropriate status indicators.
    """
)
```

---

## 🔄 Output Processing Pipeline

### 1. **Multi-stage Processing**
Chain multiple output processors

```python
from google_adk import OutputPipeline

# Create processing pipeline
pipeline = OutputPipeline([
    ("validate", OutputValidator(schema=validation_schema)),
    ("sanitize", OutputSanitizer(remove_pii=True)),
    ("format", OutputFormatter(format_function=format_response)),
    ("log", OutputLogger(log_level="INFO"))
])

# Agent with pipeline
pipeline_agent = Agent(
    name="pipeline_agent",
    description="Agent with output processing pipeline",
    model="text-bison@001",
    output_pipeline=pipeline,
    instructions="""
    Generate responses that will pass through the processing pipeline.
    Ensure responses are valid, safe, and properly formatted.
    """
)
```

### 2. **Error Recovery**
Handle output format errors gracefully

```python
def error_recovery_handler(error: Exception, raw_response: str) -> Dict[str, Any]:
    """Handle output format errors"""
    
    if isinstance(error, ValidationError):
        return {
            "status": "error",
            "error": "Invalid format",
            "message": "Response format validation failed",
            "raw_response": raw_response
        }
    
    if isinstance(error, SerializationError):
        return {
            "status": "error",
            "error": "Serialization failed",
            "message": "Could not serialize response",
            "raw_response": raw_response
        }
    
    return {
        "status": "error",
        "error": "Unknown error",
        "message": str(error),
        "raw_response": raw_response
    }

# Agent with error recovery
recovery_agent = Agent(
    name="recovery_agent",
    description="Agent with error recovery",
    model="text-bison@001",
    error_recovery_handler=error_recovery_handler,
    max_retries=3,
    instructions="""
    Generate responses in the correct format.
    If format errors occur, the system will attempt recovery.
    """
)
```

---

## 📊 Advanced Output Patterns

### 1. **Streaming Output**
Handle large responses incrementally

```python
from google_adk import StreamingOutput

# Configure streaming output
streaming_agent = Agent(
    name="streaming_agent",
    description="Agent with streaming output",
    model="text-bison@001",
    streaming=True,
    output_format="json_stream",
    instructions="""
    Provide responses as a stream of JSON objects.
    Each object should be a complete, valid JSON.
    Use for long-running analyses or large datasets.
    """
)

# Process streaming output
for chunk in streaming_agent.stream("Analyze this large dataset"):
    data = json.loads(chunk)
    print(f"Progress: {data.get('progress', 0)}%")
    print(f"Current result: {data.get('partial_result', '')}")
```

### 2. **Batch Output**
Process multiple items in single response

```python
batch_agent = Agent(
    name="batch_agent",
    description="Agent for batch processing",
    model="text-bison@001",
    output_format="json_batch",
    instructions="""
    Process multiple items and return results in a batch format.
    
    Expected format:
    {
        "batch_id": "unique_identifier",
        "total_items": 10,
        "results": [
            {"item_id": 1, "status": "success", "data": {...}},
            {"item_id": 2, "status": "error", "error": "..."}
        ],
        "summary": {
            "success_count": 8,
            "error_count": 2,
            "processing_time": 15.5
        }
    }
    """
)
```

### 3. **Hierarchical Output**
Nested structured data

```python
hierarchical_agent = Agent(
    name="hierarchical_agent",
    description="Agent with hierarchical output",
    model="text-bison@001",
    output_format="json_hierarchical",
    instructions="""
    Return responses in hierarchical structure.
    
    Example:
    {
        "report": {
            "metadata": {
                "title": "Analysis Report",
                "date": "2024-01-15",
                "author": "AI Agent"
            },
            "sections": [
                {
                    "title": "Executive Summary",
                    "content": "...",
                    "subsections": [...]
                }
            ]
        }
    }
    """
)
```

---

## 🛠️ Practical Examples

### 1. **API Response Agent**
```python
api_agent = Agent(
    name="api_response_agent",
    description="Agent for API responses",
    model="text-bison@001",
    output_format="json",
    output_schema={
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "data": {"type": "object"},
            "error": {"type": "string"},
            "metadata": {
                "type": "object",
                "properties": {
                    "timestamp": {"type": "string"},
                    "request_id": {"type": "string"},
                    "version": {"type": "string"}
                }
            }
        }
    },
    instructions="""
    Always return responses in API-compatible JSON format.
    Include success status, data or error, and metadata.
    """
)
```

### 2. **Data Analysis Report Agent**
```python
report_agent = Agent(
    name="report_agent",
    description="Agent for data analysis reports",
    model="text-bison@001",
    output_format="json",
    output_schema={
        "type": "object",
        "properties": {
            "report_id": {"type": "string"},
            "analysis_date": {"type": "string"},
            "dataset_info": {
                "type": "object",
                "properties": {
                    "rows": {"type": "integer"},
                    "columns": {"type": "integer"},
                    "data_types": {"type": "array"}
                }
            },
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "description": {"type": "string"},
                        "confidence": {"type": "number"},
                        "details": {"type": "object"}
                    }
                }
            },
            "recommendations": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    },
    instructions="""
    Analyze data and return structured reports.
    Include dataset information, findings, and recommendations.
    Use confidence scores for findings.
    """
)
```

---

## 📚 Best Practices

### 1. **Schema Design**
- **Be Specific**: Define exact types and constraints
- **Use Enums**: For known value sets
- **Add Validation**: Business logic validation
- **Document Fields**: Clear field descriptions

### 2. **Error Handling**
- **Graceful Degradation**: Fallback formats
- **Clear Error Messages**: Helpful error information
- **Retry Logic**: Automatic format correction
- **Logging**: Track format issues

### 3. **Performance**
- **Minimize Size**: Efficient data structures
- **Use Streaming**: For large responses
- **Cache Formats**: Reuse common formats
- **Batch Processing**: Handle multiple items

---

## 📚 Next Steps

1. **Learn Model Configuration** → `04-configuring-model.md`
2. **Master Tools in ADK** → `05-tools-in-adk.md`
3. **Build Structured Agents** → Create agents with output formatting
4. **Practice Examples** → Try structured output examples

---

**📝 Master structured output for reliable AI applications!**
