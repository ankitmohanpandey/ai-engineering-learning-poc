# GCP Contact Center AI Insights - Complete Guide

## Table of Contents
1. [What is CCAI Insights?](#what-is-ccai-insights)
2. [Core Concepts](#core-concepts)
3. [Architecture Overview](#architecture-overview)
4. [Setup & Prerequisites](#setup--prerequisites)
5. [Step-by-Step Implementation](#step-by-step-implementation)
6. [Advanced Features](#advanced-features)
7. [BigQuery Integration](#bigquery-integration)
8. [Real-World Use Cases](#real-world-use-cases)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## What is CCAI Insights?

**Contact Center AI Insights** is a Google Cloud Platform service that uses machine learning to analyze contact center conversations (calls and chats) to extract valuable business insights.

### Key Capabilities
- **Conversation Analysis**: Automatically analyze calls and chats
- **Sentiment Detection**: Identify agent and customer sentiment
- **Topic Modeling**: Discover conversation themes and call drivers
- **Entity Recognition**: Extract key information (names, dates, products)
- **Conversation Highlights**: Identify important moments
- **Speech-to-Text**: Convert audio to text with high accuracy
- **BigQuery Integration**: Export data for custom analysis
- **Visualization**: Create dashboards in Looker/Data Studio

### Why Use CCAI Insights?
✅ **Improve Customer Experience**: Understand customer pain points  
✅ **Operational Efficiency**: Identify training opportunities  
✅ **Business Intelligence**: Discover trends and patterns  
✅ **Quality Assurance**: Automated conversation review  
✅ **Compliance**: Monitor adherence to scripts and regulations  
✅ **Agent Performance**: Track sentiment and effectiveness  
✅ **Scalability**: Analyze thousands of conversations automatically  

---

## Core Concepts

### 1. Conversations
- **Definition**: Individual customer-agent interactions
- **Types**: Voice calls, chat transcripts
- **Format**: JSON for chat, audio files for calls
- **Metadata**: Agent ID, duration, timestamp, medium

### 2. Conversation Analysis
Automated processing that extracts:
- **Sentiment**: Positive, negative, neutral (agent and customer)
- **Entities**: Names, products, locations, dates
- **Topics**: Main themes discussed
- **Highlights**: Key moments in conversation
- **Summary**: AI-generated conversation summary

### 3. Topic Modeling
- **Purpose**: Discover common conversation themes
- **Method**: Unsupervised machine learning
- **Output**: Topics with confidence scores
- **Use Case**: Identify top call drivers

**Example Topics:**
- Billing inquiries
- Technical support
- Product returns
- Account changes

### 4. Conversation Highlights

#### Smart Highlights (System-Generated)
- Automatically detected important moments
- Based on ML models
- No configuration needed

#### Custom Highlights
- User-defined phrases or patterns
- Include/exclude rules
- Business-specific keywords

**Example Custom Highlights:**
- "cancel subscription"
- "speak to manager"
- "refund request"
- "technical issue"

### 5. Sentiment Analysis
- **Granularity**: Overall and turn-by-turn
- **Scores**: -1 (negative) to +1 (positive)
- **Visualization**: Sentiment timeline
- **Insights**: Identify frustration points

### 6. Entity Recognition
Automatically extracts:
- **Person names**: Customer and agent names
- **Organizations**: Company names
- **Locations**: Cities, addresses
- **Products**: Product names, SKUs
- **Dates/Times**: Appointment times, deadlines
- **Phone numbers**: Contact information
- **Custom entities**: Business-specific terms

---

## Architecture Overview

```
Data Sources
  - Audio Files (WAV, FLAC, MP3)
  - Chat JSON Files
  - Dialogflow Conversations
          ↓
Cloud Storage (Staging)
  gs://bucket-name/conversations/
          ↓
CCAI Insights Processing
  - Speech-to-Text
  - NLP Analysis
  - Topic Modeling
  - Sentiment Analysis
          ↓
Analyzed Conversations
  - Transcripts
  - Sentiment Scores
  - Topics
  - Highlights
  - Entities
          ↓
BigQuery Export
  - Custom Analysis
  - Reporting
  - Data Warehouse
          ↓
Visualization
  - Looker Dashboards
  - Data Studio Reports
  - Trend Analysis
```

---

## Setup & Prerequisites

### 1. GCP Project Setup

#### Create or Select Project
```bash
# List projects
gcloud projects list

# Create new project
gcloud projects create ccai-insights-project

# Set active project
gcloud config set project ccai-insights-project
```

### 2. Required IAM Roles

For the user/service account using CCAI Insights:

| Role | Purpose |
|------|---------|
| Contact Center AI Insights Editor | Create and manage insights |
| Dialogflow API Admin | Manage Dialogflow integration |
| Storage Admin | Upload conversation files |
| BigQuery Data Editor | Export to BigQuery |
| Cloud Speech Administrator | Speech-to-Text processing |

#### Grant Roles via Console
1. Navigate to IAM and Admin - IAM
2. Click Grant Access
3. Enter user email under New principals
4. Click Select a role and add each role above
5. Click Add another role for multiple roles
6. Click Save

### 3. Enable Required APIs

```bash
# Enable APIs
gcloud services enable contactcenterinsights.googleapis.com
gcloud services enable speech.googleapis.com
gcloud services enable dialogflow.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
```

Or via Console:
1. Navigate to APIs and Services - Library
2. Search for each API:
   - Contact Center AI Insights API
   - Cloud Speech-to-Text API
   - Dialogflow API
   - Cloud Storage API
   - BigQuery API
3. Click Enable for each

---

## Step-by-Step Implementation

See detailed guide in SETUP_GUIDE.md

### Quick Overview

**Step 1**: Create Cloud Storage bucket  
**Step 2**: Upload conversation files  
**Step 3**: Import conversations to Insights  
**Step 4**: Create topic model  
**Step 5**: Create custom highlights  
**Step 6**: Run conversation analysis  
**Step 7**: Export to BigQuery  
**Step 8**: Create visualizations  

---

## Advanced Features

### 1. Conversation Summarization
- AI-generated summaries of conversations
- Highlights key points and outcomes
- Saves time in conversation review

### 2. Silence Detection
- Identifies periods of silence
- May indicate customer confusion or frustration
- Useful for quality assurance

### 3. Interruptions Tracking
- Detects when speakers talk over each other
- Indicates conversation flow issues
- Agent training opportunity

### 4. Speech Pace Analysis
- Measures words per minute
- Identifies rushed or slow conversations
- Helps optimize conversation pacing

### 5. Custom Vocabularies
- Add industry-specific terms
- Improve transcription accuracy
- Better entity recognition

### 6. Phrase Matchers
- Define specific phrases to track
- More precise than topic modeling
- Compliance and quality monitoring

---

## BigQuery Integration

### Schema Overview

Main tables created after export:

#### conversations table
- conversation_id
- agent_id
- create_time
- duration
- medium (PHONE_CALL or CHAT)
- language_code
- agent_sentiment_score
- client_sentiment_score

#### sentences table
- conversation_id
- sentence_id
- text
- participant_role (AGENT or CUSTOMER)
- sentiment_score
- create_time

#### entities table
- conversation_id
- entity_id
- entity_type
- entity_value
- salience

#### topics table
- conversation_id
- topic_id
- topic_name
- confidence_score

### Sample Queries

See BIGQUERY_EXAMPLES.md for detailed queries

---

## Real-World Use Cases

### 1. Customer Experience Improvement
**Goal**: Identify common customer pain points

**Approach**:
- Analyze conversations with negative sentiment
- Identify recurring topics in complaints
- Track resolution times
- Monitor customer satisfaction trends

**Metrics**:
- Average sentiment score
- Top negative topics
- Resolution rate
- Escalation frequency

### 2. Agent Performance Monitoring
**Goal**: Evaluate and improve agent effectiveness

**Approach**:
- Track agent sentiment scores
- Monitor adherence to scripts
- Identify training needs
- Recognize top performers

**Metrics**:
- Agent sentiment vs customer sentiment
- Average handle time
- First call resolution rate
- Script compliance percentage

### 3. Product Issue Detection
**Goal**: Identify product defects or issues early

**Approach**:
- Monitor product-related topics
- Track sentiment around specific products
- Identify spike in complaints
- Alert product teams

**Metrics**:
- Product mention frequency
- Product-related negative sentiment
- Issue escalation rate
- Time to detection

### 4. Compliance Monitoring
**Goal**: Ensure regulatory compliance

**Approach**:
- Create custom highlights for required disclosures
- Monitor prohibited phrases
- Track script adherence
- Generate compliance reports

**Metrics**:
- Disclosure compliance rate
- Prohibited phrase detection
- Script deviation frequency
- Audit readiness score

### 5. Call Volume Forecasting
**Goal**: Predict staffing needs

**Approach**:
- Analyze historical call patterns
- Identify seasonal trends
- Track topic distribution
- Predict future volumes

**Metrics**:
- Calls per hour/day/week
- Topic distribution over time
- Peak hour identification
- Forecast accuracy

---

## Best Practices

### Data Preparation

#### Audio Files
✅ **Format**: WAV, FLAC (lossless) preferred  
✅ **Sample Rate**: 16 kHz or higher  
✅ **Channels**: Separate channels for agent/customer  
✅ **Duration**: Under 3 hours per file  
✅ **Quality**: Clear audio, minimal background noise  

❌ Avoid: MP3 (lossy), low sample rates, mono mixed audio

#### Chat Transcripts
✅ **Format**: Valid JSON  
✅ **Structure**: Follow CCAI Insights schema  
✅ **Timestamps**: Include for each turn  
✅ **Participant Roles**: Clearly marked (agent/customer)  
✅ **Metadata**: Agent ID, conversation ID  

### Topic Modeling

✅ **Training Data**: Minimum 1000 conversations  
✅ **Diversity**: Include various conversation types  
✅ **Recency**: Use recent conversations  
✅ **Regular Updates**: Retrain monthly or quarterly  
✅ **Validation**: Review and refine topics  

❌ Avoid: Too few conversations, outdated data, no validation

### Custom Highlights

✅ **Specific Phrases**: Use exact phrases when possible  
✅ **Variations**: Include common variations  
✅ **Exclusions**: Use exclude rules to reduce false positives  
✅ **Testing**: Test on sample conversations  
✅ **Documentation**: Document purpose of each highlight  

### Performance Optimization

✅ **Batch Processing**: Import conversations in batches  
✅ **Parallel Analysis**: Analyze multiple conversations simultaneously  
✅ **Incremental Export**: Export to BigQuery regularly  
✅ **Data Retention**: Archive old conversations  
✅ **Monitoring**: Track processing times and errors  

### Security and Privacy

✅ **PII Redaction**: Enable automatic PII redaction  
✅ **Access Control**: Limit access to sensitive data  
✅ **Encryption**: Use encrypted storage  
✅ **Audit Logs**: Enable and monitor audit logs  
✅ **Compliance**: Follow GDPR, CCPA, HIPAA as needed  

---

## Troubleshooting

### Common Issues

#### 1. Import Failures

**Issue**: Conversations fail to import

**Causes**:
- Invalid JSON format
- Incorrect file path
- Missing required fields
- File size too large

**Solutions**:
- Validate JSON schema
- Check gsutil URI format
- Verify all required fields present
- Split large files

#### 2. Poor Transcription Quality

**Issue**: Speech-to-Text accuracy is low

**Causes**:
- Poor audio quality
- Background noise
- Low sample rate
- Accents or dialects

**Solutions**:
- Use higher quality audio
- Enable noise reduction
- Increase sample rate to 16kHz+
- Add custom vocabulary
- Use enhanced models

#### 3. Topic Model Not Converging

**Issue**: Topic model produces unclear topics

**Causes**:
- Insufficient training data
- Too many/few topics specified
- Low-quality conversations
- Lack of diversity

**Solutions**:
- Increase training data (1000+ conversations)
- Adjust number of topics
- Filter low-quality conversations
- Include diverse conversation types
- Retrain with better parameters

#### 4. Slow Analysis Processing

**Issue**: Analysis takes too long

**Causes**:
- Large batch size
- Complex custom highlights
- High API quota usage
- Resource constraints

**Solutions**:
- Reduce batch size
- Simplify highlight rules
- Request quota increase
- Distribute processing over time

#### 5. BigQuery Export Errors

**Issue**: Export to BigQuery fails

**Causes**:
- Insufficient permissions
- Invalid dataset/table
- Schema mismatch
- Quota exceeded

**Solutions**:
- Verify BigQuery permissions
- Create dataset and table first
- Use correct schema
- Check and increase quotas

---

## Pricing Considerations

### Cost Components

1. **Speech-to-Text**: Per minute of audio
2. **Storage**: Cloud Storage costs
3. **BigQuery**: Storage and query costs
4. **Insights Processing**: Per conversation analyzed

### Cost Optimization

✅ Use standard STT models (not enhanced) when possible  
✅ Archive old conversations to cheaper storage  
✅ Export only needed data to BigQuery  
✅ Use BigQuery partitioning and clustering  
✅ Set up budget alerts  

---

## Resources

- **Official Documentation**: https://cloud.google.com/contact-center/insights/docs
- **API Reference**: https://cloud.google.com/contact-center/insights/docs/reference
- **Pricing**: https://cloud.google.com/contact-center/insights/pricing
- **Best Practices**: https://cloud.google.com/contact-center/insights/docs/best-practices
- **Support**: https://cloud.google.com/support

---

## Next Steps

1. Complete setup (see SETUP_GUIDE.md)
2. Import sample conversations
3. Create your first topic model
4. Set up custom highlights
5. Run analysis and review results
6. Export to BigQuery
7. Build dashboards in Looker
8. Implement in production

---

**Remember**: CCAI Insights transforms raw conversation data into actionable business intelligence!
