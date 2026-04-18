# CCAI Insights - Detailed Setup Guide

## Complete Step-by-Step Implementation

This guide walks you through setting up Contact Center AI Insights from scratch.

---

## Prerequisites Checklist

Before starting, ensure you have:

- GCP account with billing enabled
- Project owner/editor access OR required IAM roles
- Conversation data (audio files or chat transcripts)
- Basic understanding of GCP Console

---

## Step 1: Project Setup and Permissions

### 1.1 Create or Select GCP Project

Via Console:
1. Go to Google Cloud Console
2. Click project dropdown at top
3. Click New Project
4. Enter project name: ccai-insights-prod
5. Select billing account
6. Click Create

Via gcloud CLI:
```bash
gcloud projects create ccai-insights-prod --name="CCAI Insights Production"
gcloud config set project ccai-insights-prod
```

### 1.2 Grant IAM Roles

Required Roles:
- Contact Center AI Insights Editor
- Dialogflow API Admin
- Storage Admin
- BigQuery Data Editor
- Cloud Speech Administrator

Grant via Console:
1. Navigate to IAM and Admin - IAM
2. Click GRANT ACCESS
3. Enter user email
4. Add each role listed above
5. Click SAVE

Grant via gcloud:
```bash
PROJECT_ID="ccai-insights-prod"
USER_EMAIL="analyst@company.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/contactcenterinsights.editor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/dialogflow.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/bigquery.dataEditor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/speech.admin"
```

### 1.3 Enable Required APIs

Via gcloud:
```bash
gcloud services enable contactcenterinsights.googleapis.com
gcloud services enable speech.googleapis.com
gcloud services enable dialogflow.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
```

---

## Step 2: Prepare Cloud Storage

### 2.1 Create Storage Bucket

```bash
gsutil mb -l us-central1 gs://ccai-conversations-prod
```

### 2.2 Create Folder Structure

```bash
gsutil mkdir gs://ccai-conversations-prod/audio/
gsutil mkdir gs://ccai-conversations-prod/chat/
gsutil mkdir gs://ccai-conversations-prod/archive/
```

### 2.3 Upload Conversation Files

For Audio Files:
```bash
gsutil cp local-audio-files/*.wav gs://ccai-conversations-prod/audio/
```

For Chat JSON Files:
```bash
gsutil cp chat-transcripts/*.json gs://ccai-conversations-prod/chat/
```

### 2.4 Note File Paths

Single file path format:
```
gs://ccai-conversations-prod/audio/call-001.wav
```

Folder path format (for batch import):
```
gs://ccai-conversations-prod/audio/
```

---

## Step 3: Prepare Conversation Data

### 3.1 Audio File Requirements

Best Practices:
- Format: WAV or FLAC (lossless)
- Sample Rate: 16 kHz minimum (higher is better)
- Channels: Stereo with separate agent/customer channels
- Duration: Under 3 hours per file
- Quality: Clear audio, minimal background noise

Example audio file naming:
```
call-20240101-001-agent123.wav
call-20240101-002-agent456.wav
```

### 3.2 Chat JSON Format

Required JSON structure:
```json
{
  "medium": "CHAT",
  "agent_id": "agent-123",
  "language_code": "en-US",
  "create_time": "2024-01-15T10:30:00Z",
  "turn_count": 10,
  "transcript": {
    "transcript_segments": [
      {
        "text": "Hello, how can I help you today?",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T10:30:00Z"
      },
      {
        "text": "I need help with my billing",
        "participant_role": "CUSTOMER",
        "message_time": "2024-01-15T10:30:15Z"
      }
    ]
  }
}
```

Validate JSON:
```bash
python -m json.tool conversation.json
```

---

## Step 4: Import Conversations to CCAI Insights

### 4.1 Navigate to Insights Console

1. Go to Contact Center AI Insights
2. Select your project from dropdown
3. Click IMPORT button

### 4.2 Import Audio Conversations

Fill in import form:
- Conversation medium: PHONE_CALL
- GCS URI: gs://ccai-conversations-prod/audio/
- Agent ID: agent-123 (or leave blank for auto-detection)
- Language code: en-US
- Speech config:
  - Model: default or enhanced (phone_call recommended)
  - Sample rate: 16000
  - Audio channel count: 2
  - Enable separate recognition per channel: Yes

Click IMPORT

### 4.3 Import Chat Conversations

Fill in import form:
- Conversation medium: CHAT
- GCS URI: gs://ccai-conversations-prod/chat/
- Agent ID: (included in JSON)

Click IMPORT

### 4.4 Monitor Import Status

1. Click hourglass icon (top-right)
2. View import progress
3. Check for errors
4. Wait for completion

Typical import times:
- Chat: 1-2 minutes per conversation
- Audio: 5-10 minutes per conversation (depends on duration)

---

## Step 5: Create Topic Model

### 5.1 Navigate to Topic Models

1. Click Topic Models icon (left sidebar)
2. Click CREATE NEW MODEL

### 5.2 Configure Topic Model

Model settings:
- Model name: customer-support-topics-v1
- Description: Main topics in customer support calls
- Number of topics: 10-20 (start with 10)
- Training data: Select conversations
  - Date range: Last 30 days
  - Minimum: 1000 conversations
  - Include diverse conversation types

### 5.3 Select Training Conversations

Filter criteria:
- Date range: 2024-01-01 to 2024-01-31
- Medium: PHONE_CALL and CHAT
- Agent sentiment: All
- Duration: Greater than 60 seconds

Click SELECT ALL or manually select conversations

### 5.4 Train Model

1. Review settings
2. Click CREATE AND TRAIN
3. Wait for training (30 minutes to 2 hours)
4. Check training status

### 5.5 Review and Deploy Model

Once trained:
1. Review discovered topics
2. Rename topics for clarity
3. Merge similar topics if needed
4. Click DEPLOY MODEL

---

## Step 6: Create Custom Highlights

### 6.1 Navigate to Conversation Highlights

1. Click Conversation Highlights icon (left sidebar)
2. Go to CUSTOM HIGHLIGHTS tab
3. Click CREATE HIGHLIGHT

### 6.2 Define Highlight Rules

Example 1: Cancellation Requests
- Name: Cancellation Request
- Description: Customer wants to cancel service
- Include phrases:
  - cancel my subscription
  - want to cancel
  - cancel my account
  - stop my service
- Exclude phrases:
  - do not want to cancel
  - not canceling

Example 2: Escalation
- Name: Escalation Request
- Description: Customer asks for manager
- Include phrases:
  - speak to manager
  - talk to supervisor
  - escalate this
  - need to speak to someone else

Example 3: Positive Feedback
- Name: Positive Feedback
- Description: Customer expresses satisfaction
- Include phrases:
  - thank you so much
  - great service
  - very helpful
  - appreciate your help

### 6.3 Test Highlights

1. Create highlight
2. Apply to sample conversations
3. Review matches
4. Refine rules as needed

---

## Step 7: Run Conversation Analysis

### 7.1 Single Conversation Analysis

1. Go to Conversation Hub
2. Click on a conversation
3. Click ANALYZE button
4. Select analyses:
   - Sentiment analysis
   - Entity extraction
   - Topic detection
   - Conversation highlights
   - Conversation summary
5. Click RUN ANALYSIS
6. Wait for completion (1-2 minutes)

### 7.2 Batch Analysis

1. Go to Conversation Hub
2. Filter conversations:
   - Date range
   - Agent
   - Medium
   - Duration
3. Select multiple conversations
4. Click ANALYZE (bulk action)
5. Select analyses
6. Click RUN ANALYSIS
7. Monitor progress

### 7.3 Review Analysis Results

For each conversation, view:
- Transcript with timestamps
- Sentiment timeline
- Detected topics with confidence scores
- Highlighted phrases
- Extracted entities
- AI-generated summary
- Silence periods
- Interruptions

Navigate using:
- Conversation spotlight (key moments)
- Annotations panel
- Click highlights to jump to location

---

## Step 8: Export to BigQuery

### 8.1 Create BigQuery Dataset

Via Console:
1. Go to BigQuery
2. Click your project
3. Click CREATE DATASET
4. Dataset ID: ccai_insights
5. Location: us-central1
6. Click CREATE DATASET

Via bq CLI:
```bash
bq mk --dataset --location=us-central1 ccai-insights-prod:ccai_insights
```

### 8.2 Create Export Table

```bash
bq mk --table ccai-insights-prod:ccai_insights.conversations
```

### 8.3 Export from Insights

1. Go to Insights Console
2. Filter conversations to export
3. Click EXPORT button
4. Fill in details:
   - BigQuery project: ccai-insights-prod
   - Dataset: ccai_insights
   - Table: conversations
5. Click EXPORT
6. Wait for completion

### 8.4 Verify Export

```bash
bq query --use_legacy_sql=false '
SELECT COUNT(*) as total_conversations
FROM `ccai-insights-prod.ccai_insights.conversations`
'
```

---

## Step 9: Create Dashboards

### 9.1 Connect Looker to BigQuery

1. Go to Looker Studio
2. Create new data source
3. Select BigQuery
4. Choose project: ccai-insights-prod
5. Choose dataset: ccai_insights
6. Choose table: conversations

### 9.2 Build Dashboard

Key metrics to visualize:
- Total conversations over time
- Average sentiment score
- Top topics distribution
- Agent performance metrics
- Call duration trends
- Highlight frequency

Example charts:
- Line chart: Sentiment over time
- Bar chart: Top 10 topics
- Pie chart: Medium distribution
- Table: Agent leaderboard
- Heatmap: Call volume by hour/day

---

## Step 10: Automation and Monitoring

### 10.1 Set Up Scheduled Imports

Create Cloud Function or Cloud Scheduler to:
- Automatically import new conversations
- Run analysis on imported conversations
- Export to BigQuery daily

### 10.2 Set Up Alerts

Create alerts for:
- Spike in negative sentiment
- Increase in specific topics
- Low agent sentiment scores
- Processing failures

### 10.3 Monitor Costs

1. Set up budget alerts
2. Monitor API usage
3. Review BigQuery costs
4. Optimize storage

---

## Troubleshooting

### Import Failures

Check:
- File format and structure
- GCS permissions
- File path correctness
- JSON validity

### Poor Transcription

Solutions:
- Use higher quality audio
- Enable enhanced models
- Add custom vocabulary
- Check sample rate

### Topic Model Issues

Solutions:
- Increase training data
- Adjust number of topics
- Filter low-quality conversations
- Retrain with better parameters

---

## Next Steps

1. Set up production pipeline
2. Train team on Insights UI
3. Create custom reports
4. Integrate with existing systems
5. Establish regular review process
6. Continuously refine topic models and highlights

---

## Resources

- Official Docs: https://cloud.google.com/contact-center/insights/docs
- API Reference: https://cloud.google.com/contact-center/insights/docs/reference
- Best Practices: https://cloud.google.com/contact-center/insights/docs/best-practices
