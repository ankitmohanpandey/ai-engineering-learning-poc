# Conversation Data Formats for CCAI Insights

## Overview

This guide provides detailed information about conversation data formats for importing into CCAI Insights.

---

## Chat Conversation Format (JSON)

### Complete JSON Schema

```json
{
  "medium": "CHAT",
  "agent_id": "agent-123",
  "language_code": "en-US",
  "create_time": "2024-01-15T10:30:00Z",
  "duration": "PT5M30S",
  "turn_count": 10,
  "labels": {
    "department": "billing",
    "priority": "high"
  },
  "transcript": {
    "transcript_segments": [
      {
        "text": "Hello, how can I help you today?",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T10:30:00Z",
        "segment_participant": {
          "user_id": "agent-123"
        }
      },
      {
        "text": "I need help with my billing",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T10:30:15Z",
        "segment_participant": {
          "user_id": "customer-456"
        }
      }
    ]
  }
}
```

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| medium | string | Must be "CHAT" | "CHAT" |
| agent_id | string | Unique agent identifier | "agent-123" |
| language_code | string | BCP-47 language code | "en-US" |
| create_time | string | ISO 8601 timestamp | "2024-01-15T10:30:00Z" |
| transcript | object | Conversation transcript | See below |

### Optional Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| duration | string | ISO 8601 duration | "PT5M30S" |
| turn_count | integer | Number of turns | 10 |
| labels | object | Custom metadata | {"dept": "sales"} |

### Transcript Segment Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| text | string | Yes | Message text |
| participant_role | string | Yes | "AGENT" or "CUSTOMER" |
| message_time | string | Yes | ISO 8601 timestamp |
| segment_participant | object | No | Participant details |

### Example: Simple Chat Conversation

```json
{
  "medium": "CHAT",
  "agent_id": "agent-001",
  "language_code": "en-US",
  "create_time": "2024-01-15T14:30:00Z",
  "transcript": {
    "transcript_segments": [
      {
        "text": "Hi! Welcome to TechSupport. How can I assist you?",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T14:30:00Z"
      },
      {
        "text": "My internet is not working",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T14:30:30Z"
      },
      {
        "text": "I'm sorry to hear that. Let me help you troubleshoot.",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T14:30:45Z"
      },
      {
        "text": "Have you tried restarting your router?",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T14:30:50Z"
      },
      {
        "text": "Yes, I did but it didn't help",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T14:31:10Z"
      }
    ]
  }
}
```

### Example: Chat with Labels

```json
{
  "medium": "CHAT",
  "agent_id": "agent-042",
  "language_code": "en-US",
  "create_time": "2024-01-15T09:15:00Z",
  "duration": "PT8M45S",
  "turn_count": 16,
  "labels": {
    "department": "billing",
    "issue_type": "refund_request",
    "priority": "high",
    "customer_tier": "premium"
  },
  "transcript": {
    "transcript_segments": [
      {
        "text": "Hello, I'd like to request a refund",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T09:15:00Z"
      },
      {
        "text": "I'd be happy to help with that. Can I have your account number?",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T09:15:15Z"
      }
    ]
  }
}
```

---

## Audio Conversation Format

### Audio File Requirements

| Specification | Recommended | Minimum | Notes |
|---------------|-------------|---------|-------|
| Format | WAV, FLAC | WAV, FLAC, MP3 | Lossless preferred |
| Sample Rate | 16 kHz or higher | 8 kHz | Higher is better |
| Bit Depth | 16-bit | 16-bit | Standard |
| Channels | 2 (stereo) | 1 (mono) | Separate channels preferred |
| Duration | Under 3 hours | Any | Split longer files |
| File Size | Under 1 GB | Any | Affects processing time |

### Channel Configuration

**Option 1: Separate Channels (Recommended)**
- Channel 0: Agent
- Channel 1: Customer
- Enables better speaker diarization
- More accurate sentiment analysis per participant

**Option 2: Mixed/Mono**
- Single channel with both speakers
- Requires speaker diarization
- Less accurate participant attribution

### Audio File Naming Convention

Recommended naming pattern:
```
{date}_{call_id}_{agent_id}.wav

Examples:
20240115_call001_agent123.wav
20240115_call002_agent456.wav
```

### Metadata for Audio Import

When importing audio, provide:

```json
{
  "gcs_uri": "gs://bucket/audio/call001.wav",
  "medium": "PHONE_CALL",
  "agent_id": "agent-123",
  "language_code": "en-US",
  "audio_config": {
    "sample_rate_hertz": 16000,
    "audio_channel_count": 2,
    "enable_separate_recognition_per_channel": true,
    "model": "phone_call"
  }
}
```

### Speech-to-Text Models

| Model | Use Case | Accuracy | Cost |
|-------|----------|----------|------|
| default | General purpose | Good | Standard |
| phone_call | Phone conversations | Better | Standard |
| video | Video content | Good | Standard |
| enhanced | High accuracy needed | Best | 2x cost |

---

## Dialogflow Integration Format

### Automatic Import from Dialogflow

If using Dialogflow, conversations can be automatically imported.

Enable integration:
1. Go to CCAI Insights settings
2. Enable Dialogflow integration
3. Select Dialogflow agent
4. Configure sync frequency

Dialogflow conversation format (auto-generated):
```json
{
  "medium": "CHAT",
  "agent_id": "dialogflow-agent-id",
  "language_code": "en-US",
  "create_time": "2024-01-15T10:00:00Z",
  "dialogflow_conversation": {
    "conversation_name": "projects/PROJECT/conversations/CONV_ID",
    "conversation_profile": "projects/PROJECT/conversationProfiles/PROFILE_ID"
  },
  "transcript": {
    "transcript_segments": [...]
  }
}
```

---

## Validation and Testing

### Validate JSON Format

Python script to validate chat JSON:

```python
import json
from datetime import datetime

def validate_chat_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Check required fields
    required_fields = ['medium', 'agent_id', 'language_code', 'create_time', 'transcript']
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False
    
    # Validate medium
    if data['medium'] != 'CHAT':
        print("Medium must be 'CHAT'")
        return False
    
    # Validate transcript segments
    if 'transcript_segments' not in data['transcript']:
        print("Missing transcript_segments")
        return False
    
    for i, segment in enumerate(data['transcript']['transcript_segments']):
        if 'text' not in segment:
            print(f"Segment {i}: Missing text")
            return False
        if 'participant_role' not in segment:
            print(f"Segment {i}: Missing participant_role")
            return False
        if segment['participant_role'] not in ['AGENT', 'CUSTOMER']:
            print(f"Segment {i}: Invalid participant_role")
            return False
    
    print("Validation passed!")
    return True

# Usage
validate_chat_json('conversation.json')
```

### Validate Audio Files

```bash
# Check audio file properties using ffprobe
ffprobe -v error -show_entries stream=sample_rate,channels,codec_name \
    -of default=noprint_wrappers=1 audio_file.wav

# Expected output:
# codec_name=pcm_s16le
# sample_rate=16000
# channels=2
```

### Test Import with Sample Data

Create a minimal test conversation:

```json
{
  "medium": "CHAT",
  "agent_id": "test-agent",
  "language_code": "en-US",
  "create_time": "2024-01-15T12:00:00Z",
  "transcript": {
    "transcript_segments": [
      {
        "text": "Test message from agent",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T12:00:00Z"
      },
      {
        "text": "Test message from customer",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T12:00:10Z"
      }
    ]
  }
}
```

Upload and import to verify setup is correct.

---

## Common Formatting Errors

### Error 1: Invalid JSON Syntax

**Problem:**
```json
{
  "medium": "CHAT",
  "agent_id": "agent-123",  // Comments not allowed
  "transcript": {...}
}
```

**Solution:**
Remove comments, ensure proper JSON syntax

### Error 2: Incorrect Timestamp Format

**Problem:**
```json
"create_time": "2024-01-15 10:30:00"  // Wrong format
```

**Solution:**
```json
"create_time": "2024-01-15T10:30:00Z"  // ISO 8601 format
```

### Error 3: Missing Required Fields

**Problem:**
```json
{
  "medium": "CHAT",
  "transcript": {...}
  // Missing agent_id, language_code, create_time
}
```

**Solution:**
Include all required fields

### Error 4: Invalid Participant Role

**Problem:**
```json
"participant_role": "USER"  // Invalid
```

**Solution:**
```json
"participant_role": "CUSTOMER"  // or "AGENT"
```

---

## Batch Conversion Scripts

### Convert CSV to CCAI JSON

```python
import csv
import json
from datetime import datetime

def csv_to_ccai_json(csv_file, output_dir):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            conversation = {
                "medium": "CHAT",
                "agent_id": row['agent_id'],
                "language_code": "en-US",
                "create_time": row['timestamp'],
                "transcript": {
                    "transcript_segments": []
                }
            }
            
            # Parse conversation turns (assuming format: "AGENT: text | CUSTOMER: text")
            turns = row['conversation'].split('|')
            for turn in turns:
                role, text = turn.split(':', 1)
                segment = {
                    "text": text.strip(),
                    "participant_role": role.strip(),
                    "message_time": row['timestamp']
                }
                conversation['transcript']['transcript_segments'].append(segment)
            
            # Save to file
            filename = f"{output_dir}/conversation_{row['conversation_id']}.json"
            with open(filename, 'w') as out:
                json.dump(conversation, out, indent=2)

# Usage
csv_to_ccai_json('conversations.csv', 'output_json/')
```

---

## Best Practices

### Data Quality

✅ **Clean transcripts**: Remove PII if needed  
✅ **Accurate timestamps**: Ensure chronological order  
✅ **Complete conversations**: Include full interaction  
✅ **Consistent formatting**: Use same structure  
✅ **Proper encoding**: UTF-8 encoding  

### Performance

✅ **Batch uploads**: Upload multiple files at once  
✅ **Organized structure**: Use folders for organization  
✅ **Compressed audio**: Use FLAC for smaller files  
✅ **Reasonable file sizes**: Split very large files  

### Metadata

✅ **Meaningful labels**: Add relevant metadata  
✅ **Agent IDs**: Use consistent agent identifiers  
✅ **Timestamps**: Include accurate timestamps  
✅ **Language codes**: Specify correct language  

---

## Resources

- JSON Schema Validator: https://www.jsonschemavalidator.net/
- ISO 8601 Format: https://en.wikipedia.org/wiki/ISO_8601
- BCP-47 Language Codes: https://tools.ietf.org/html/bcp47
- Audio Conversion Tools: FFmpeg (https://ffmpeg.org/)
