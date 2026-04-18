# CCAI Insights Quick Reference Card

## 🚀 Quick Start

```bash
# Enable APIs
gcloud services enable contactcenterinsights.googleapis.com

# Create bucket
gsutil mb gs://ccai-conversations

# Upload conversations
gsutil cp conversations/*.json gs://ccai-conversations/chat/
```

## 📋 Core Components

### Conversation Medium Types
- `PHONE_CALL` - Audio conversations
- `CHAT` - Text-based conversations

### Participant Roles
- `AGENT` - Contact center agent
- `CUSTOMER` - End user/customer

### Sentiment Scores
- `+1.0` - Very positive
- `0.0` - Neutral
- `-1.0` - Very negative

## 📊 Chat JSON Format

### Minimal Required Structure
```json
{
  "medium": "CHAT",
  "agent_id": "agent-123",
  "language_code": "en-US",
  "create_time": "2024-01-15T10:30:00Z",
  "transcript": {
    "transcript_segments": [
      {
        "text": "Message text",
        "participant_role": "AGENT",
        "message_time": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```

### Required Fields
- `medium` - Must be "CHAT" or "PHONE_CALL"
- `agent_id` - Agent identifier
- `language_code` - BCP-47 code (e.g., "en-US")
- `create_time` - ISO 8601 timestamp
- `transcript.transcript_segments` - Array of messages

### Optional Fields
- `duration` - ISO 8601 duration (e.g., "PT5M30S")
- `turn_count` - Number of conversation turns
- `labels` - Custom metadata object

## 🎙️ Audio File Requirements

| Specification | Recommended | Minimum |
|---------------|-------------|---------|
| Format | WAV, FLAC | WAV, FLAC, MP3 |
| Sample Rate | 16 kHz+ | 8 kHz |
| Channels | 2 (stereo) | 1 (mono) |
| Duration | < 3 hours | Any |

### Audio Import Configuration
```json
{
  "gcs_uri": "gs://bucket/audio/call.wav",
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

## 🔧 Common gcloud Commands

### Enable APIs
```bash
gcloud services enable contactcenterinsights.googleapis.com
gcloud services enable speech.googleapis.com
gcloud services enable dialogflow.googleapis.com
gcloud services enable bigquery.googleapis.com
```

### Grant IAM Roles
```bash
PROJECT_ID="your-project"
USER_EMAIL="user@example.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$USER_EMAIL" \
    --role="roles/contactcenterinsights.editor"
```

### Cloud Storage Operations
```bash
# Create bucket
gsutil mb -l us-central1 gs://bucket-name

# Upload files
gsutil cp file.json gs://bucket-name/chat/

# Upload folder
gsutil -m cp -r local-folder/* gs://bucket-name/chat/

# List files
gsutil ls gs://bucket-name/chat/

# Get file URI
gsutil ls -l gs://bucket-name/chat/file.json
```

## 📈 BigQuery Quick Queries

### Total Conversations
```sql
SELECT COUNT(*) as total
FROM `project.dataset.conversations`
```

### Average Sentiment
```sql
SELECT 
  ROUND(AVG(client_sentiment_score), 3) as avg_sentiment
FROM `project.dataset.conversations`
```

### Top Topics
```sql
SELECT 
  topic_name,
  COUNT(*) as count
FROM `project.dataset.topics`
GROUP BY topic_name
ORDER BY count DESC
LIMIT 10
```

### Negative Conversations
```sql
SELECT *
FROM `project.dataset.conversations`
WHERE client_sentiment_score < -0.3
ORDER BY client_sentiment_score ASC
```

### Agent Performance
```sql
SELECT 
  agent_id,
  COUNT(*) as total,
  ROUND(AVG(client_sentiment_score), 3) as avg_sentiment
FROM `project.dataset.conversations`
GROUP BY agent_id
ORDER BY avg_sentiment DESC
```

## 🎯 Topic Model Settings

### Recommended Configuration
- **Training Data**: Minimum 1,000 conversations
- **Number of Topics**: 10-20 (start with 10)
- **Data Recency**: Last 30-90 days
- **Diversity**: Include various conversation types
- **Retrain Frequency**: Monthly or quarterly

## ✨ Custom Highlights

### Highlight Structure
```
Name: Cancellation Request
Description: Customer wants to cancel
Include phrases:
  - cancel subscription
  - want to cancel
  - stop service
Exclude phrases:
  - do not want to cancel
```

### Common Highlight Examples

**Escalation**
- speak to manager
- talk to supervisor
- escalate this

**Positive Feedback**
- thank you so much
- great service
- very helpful

**Technical Issues**
- not working
- error message
- technical problem

**Billing Concerns**
- wrong charge
- billing issue
- refund request

## 📤 Export to BigQuery

### Create Dataset
```bash
bq mk --dataset --location=us-central1 project:ccai_insights
```

### Create Table
```bash
bq mk --table project:ccai_insights.conversations
```

### Export from Console
1. Filter conversations
2. Click EXPORT
3. Enter BigQuery details:
   - Project: your-project
   - Dataset: ccai_insights
   - Table: conversations
4. Click EXPORT

## 🔍 Analysis Workflow

### Step-by-Step
1. **Import** conversations to Insights
2. **Create** topic model (if needed)
3. **Define** custom highlights
4. **Run** analysis on conversations
5. **Review** results in Insights UI
6. **Export** to BigQuery
7. **Analyze** with SQL queries
8. **Visualize** in Looker/Data Studio

## ⚡ Performance Tips

### Import
✅ Batch upload files to Cloud Storage  
✅ Use organized folder structure  
✅ Validate JSON before upload  
✅ Use correct file formats  

### Analysis
✅ Run analysis in batches  
✅ Filter conversations before analysis  
✅ Use appropriate analysis types  
✅ Monitor processing status  

### BigQuery
✅ Use partitioned tables  
✅ Add WHERE clauses to limit data  
✅ Cache query results  
✅ Use views for complex queries  

## 🎨 Looker Dashboard Metrics

### Key Metrics to Track
- Total conversations (daily/weekly/monthly)
- Average sentiment score
- Sentiment distribution (positive/neutral/negative)
- Top 10 topics
- Agent performance rankings
- Call duration trends
- Peak hours analysis
- Topic trends over time

### Recommended Charts
- **Line Chart**: Sentiment over time
- **Bar Chart**: Top topics
- **Pie Chart**: Medium distribution
- **Table**: Agent leaderboard
- **Heatmap**: Call volume by hour/day
- **Scorecard**: Key metrics (total calls, avg sentiment)

## 🚨 Common Issues

### Import Failures
**Problem**: JSON validation error  
**Solution**: Validate JSON syntax, check required fields

**Problem**: File not found  
**Solution**: Verify GCS URI format (gs://bucket/path)

**Problem**: Permission denied  
**Solution**: Check IAM roles, verify bucket permissions

### Poor Transcription
**Problem**: Low accuracy  
**Solution**: Use higher sample rate, enhanced model, custom vocabulary

### Topic Model Issues
**Problem**: Unclear topics  
**Solution**: Increase training data, adjust topic count, retrain

## 📊 Sentiment Interpretation

| Score Range | Interpretation | Action |
|-------------|----------------|--------|
| 0.5 to 1.0 | Very Positive | Identify best practices |
| 0.1 to 0.5 | Positive | Monitor for consistency |
| -0.1 to 0.1 | Neutral | Review for improvement |
| -0.5 to -0.1 | Negative | Investigate issues |
| -1.0 to -0.5 | Very Negative | Immediate review needed |

## 🔗 Important URIs

### GCS URI Format
```
gs://bucket-name/folder/file.json
gs://bucket-name/folder/
```

### BigQuery Table Format
```
project-id:dataset.table
project-id.dataset.table
```

## 💡 Best Practices Summary

### Data Preparation
✅ Clean, valid JSON for chat  
✅ High-quality audio (16kHz+, stereo)  
✅ Accurate timestamps  
✅ Consistent agent IDs  

### Topic Modeling
✅ 1000+ conversations for training  
✅ Recent, diverse data  
✅ Regular retraining  
✅ Validate and refine topics  

### Custom Highlights
✅ Specific, clear phrases  
✅ Include variations  
✅ Use exclude rules  
✅ Test on samples  

### Security
✅ Enable PII redaction  
✅ Limit access with IAM  
✅ Use encrypted storage  
✅ Monitor audit logs  

## 📚 Resources

- **Docs**: https://cloud.google.com/contact-center/insights/docs
- **API**: https://cloud.google.com/contact-center/insights/docs/reference
- **Pricing**: https://cloud.google.com/contact-center/insights/pricing
- **Support**: https://cloud.google.com/support

## 🎯 Quick Checklist

Setup:
- [ ] Enable required APIs
- [ ] Grant IAM roles
- [ ] Create Cloud Storage bucket
- [ ] Prepare conversation data

Implementation:
- [ ] Upload conversations to GCS
- [ ] Import to CCAI Insights
- [ ] Create topic model
- [ ] Define custom highlights
- [ ] Run analysis

Analysis:
- [ ] Review results in UI
- [ ] Export to BigQuery
- [ ] Create SQL queries
- [ ] Build Looker dashboard

---

**Pro Tip**: Start with a small batch of conversations to test your setup before processing thousands of conversations!
