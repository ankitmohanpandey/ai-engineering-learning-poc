# BigQuery Analysis Examples for CCAI Insights

## Overview

This guide provides SQL queries and analysis examples for CCAI Insights data exported to BigQuery.

---

## Schema Overview

After exporting from CCAI Insights, you'll have these main tables:

### conversations table
- conversation_id (STRING)
- agent_id (STRING)
- create_time (TIMESTAMP)
- duration (INT64) - in seconds
- medium (STRING) - PHONE_CALL or CHAT
- language_code (STRING)
- agent_sentiment_score (FLOAT64)
- client_sentiment_score (FLOAT64)
- turn_count (INT64)
- labels (RECORD/STRUCT)

### sentences table
- conversation_id (STRING)
- sentence_id (STRING)
- text (STRING)
- participant_role (STRING) - AGENT or CUSTOMER
- sentiment_score (FLOAT64)
- sentiment_magnitude (FLOAT64)
- create_time (TIMESTAMP)

### entities table
- conversation_id (STRING)
- entity_id (STRING)
- entity_type (STRING)
- entity_value (STRING)
- salience (FLOAT64)

### topics table
- conversation_id (STRING)
- topic_id (STRING)
- topic_name (STRING)
- confidence_score (FLOAT64)

---

## Basic Queries

### 1. Total Conversations

```sql
SELECT 
  COUNT(*) as total_conversations,
  COUNT(DISTINCT agent_id) as unique_agents,
  AVG(duration) as avg_duration_seconds,
  AVG(turn_count) as avg_turns
FROM `project.dataset.conversations`
```

### 2. Conversations by Medium

```sql
SELECT 
  medium,
  COUNT(*) as conversation_count,
  ROUND(AVG(duration), 2) as avg_duration,
  ROUND(AVG(client_sentiment_score), 3) as avg_customer_sentiment
FROM `project.dataset.conversations`
GROUP BY medium
ORDER BY conversation_count DESC
```

### 3. Daily Conversation Volume

```sql
SELECT 
  DATE(create_time) as conversation_date,
  COUNT(*) as total_conversations,
  COUNT(CASE WHEN medium = 'PHONE_CALL' THEN 1 END) as phone_calls,
  COUNT(CASE WHEN medium = 'CHAT' THEN 1 END) as chats
FROM `project.dataset.conversations`
WHERE create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY conversation_date
ORDER BY conversation_date DESC
```

---

## Sentiment Analysis Queries

### 4. Average Sentiment by Agent

```sql
SELECT 
  agent_id,
  COUNT(*) as conversation_count,
  ROUND(AVG(agent_sentiment_score), 3) as avg_agent_sentiment,
  ROUND(AVG(client_sentiment_score), 3) as avg_customer_sentiment,
  ROUND(AVG(duration), 2) as avg_duration
FROM `project.dataset.conversations`
GROUP BY agent_id
HAVING conversation_count >= 10
ORDER BY avg_customer_sentiment DESC
```

### 5. Negative Sentiment Conversations

```sql
SELECT 
  conversation_id,
  agent_id,
  create_time,
  client_sentiment_score,
  duration,
  medium
FROM `project.dataset.conversations`
WHERE client_sentiment_score < -0.3
ORDER BY client_sentiment_score ASC
LIMIT 100
```

### 6. Sentiment Trends Over Time

```sql
SELECT 
  DATE_TRUNC(create_time, WEEK) as week,
  ROUND(AVG(client_sentiment_score), 3) as avg_customer_sentiment,
  ROUND(AVG(agent_sentiment_score), 3) as avg_agent_sentiment,
  COUNT(*) as conversation_count
FROM `project.dataset.conversations`
WHERE create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
GROUP BY week
ORDER BY week DESC
```

### 7. Sentiment Distribution

```sql
SELECT 
  CASE 
    WHEN client_sentiment_score >= 0.3 THEN 'Positive'
    WHEN client_sentiment_score <= -0.3 THEN 'Negative'
    ELSE 'Neutral'
  END as sentiment_category,
  COUNT(*) as conversation_count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM `project.dataset.conversations`
GROUP BY sentiment_category
ORDER BY conversation_count DESC
```

---

## Topic Analysis Queries

### 8. Top Topics

```sql
SELECT 
  t.topic_name,
  COUNT(DISTINCT t.conversation_id) as conversation_count,
  ROUND(AVG(t.confidence_score), 3) as avg_confidence,
  ROUND(AVG(c.client_sentiment_score), 3) as avg_sentiment
FROM `project.dataset.topics` t
JOIN `project.dataset.conversations` c
  ON t.conversation_id = c.conversation_id
GROUP BY t.topic_name
HAVING conversation_count >= 10
ORDER BY conversation_count DESC
LIMIT 20
```

### 9. Topics by Sentiment

```sql
SELECT 
  t.topic_name,
  COUNT(*) as total_conversations,
  COUNT(CASE WHEN c.client_sentiment_score >= 0.3 THEN 1 END) as positive_count,
  COUNT(CASE WHEN c.client_sentiment_score <= -0.3 THEN 1 END) as negative_count,
  ROUND(AVG(c.client_sentiment_score), 3) as avg_sentiment
FROM `project.dataset.topics` t
JOIN `project.dataset.conversations` c
  ON t.conversation_id = c.conversation_id
GROUP BY t.topic_name
HAVING total_conversations >= 20
ORDER BY negative_count DESC
LIMIT 15
```

### 10. Topic Trends Over Time

```sql
SELECT 
  DATE_TRUNC(c.create_time, MONTH) as month,
  t.topic_name,
  COUNT(*) as conversation_count
FROM `project.dataset.topics` t
JOIN `project.dataset.conversations` c
  ON t.conversation_id = c.conversation_id
WHERE c.create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 6 MONTH)
  AND t.topic_name IN ('Billing', 'Technical Support', 'Account Issues')
GROUP BY month, t.topic_name
ORDER BY month DESC, conversation_count DESC
```

---

## Agent Performance Queries

### 11. Agent Leaderboard

```sql
SELECT 
  agent_id,
  COUNT(*) as total_conversations,
  ROUND(AVG(client_sentiment_score), 3) as avg_customer_sentiment,
  ROUND(AVG(duration), 2) as avg_duration_seconds,
  ROUND(AVG(turn_count), 1) as avg_turns,
  COUNT(CASE WHEN client_sentiment_score >= 0.3 THEN 1 END) as positive_conversations,
  ROUND(COUNT(CASE WHEN client_sentiment_score >= 0.3 THEN 1 END) * 100.0 / COUNT(*), 2) as positive_rate
FROM `project.dataset.conversations`
WHERE create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY agent_id
HAVING total_conversations >= 50
ORDER BY avg_customer_sentiment DESC
LIMIT 20
```

### 12. Agent Performance by Topic

```sql
SELECT 
  c.agent_id,
  t.topic_name,
  COUNT(*) as conversation_count,
  ROUND(AVG(c.client_sentiment_score), 3) as avg_sentiment,
  ROUND(AVG(c.duration), 2) as avg_duration
FROM `project.dataset.conversations` c
JOIN `project.dataset.topics` t
  ON c.conversation_id = t.conversation_id
WHERE c.create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY c.agent_id, t.topic_name
HAVING conversation_count >= 10
ORDER BY c.agent_id, conversation_count DESC
```

---

## Entity Analysis Queries

### 13. Most Common Entities

```sql
SELECT 
  entity_type,
  entity_value,
  COUNT(*) as mention_count,
  COUNT(DISTINCT conversation_id) as conversation_count
FROM `project.dataset.entities`
GROUP BY entity_type, entity_value
HAVING conversation_count >= 5
ORDER BY mention_count DESC
LIMIT 50
```

### 14. Product Mentions with Sentiment

```sql
SELECT 
  e.entity_value as product_name,
  COUNT(DISTINCT e.conversation_id) as mention_count,
  ROUND(AVG(c.client_sentiment_score), 3) as avg_sentiment,
  COUNT(CASE WHEN c.client_sentiment_score < -0.3 THEN 1 END) as negative_mentions
FROM `project.dataset.entities` e
JOIN `project.dataset.conversations` c
  ON e.conversation_id = c.conversation_id
WHERE e.entity_type = 'PRODUCT'
GROUP BY e.entity_value
HAVING mention_count >= 10
ORDER BY negative_mentions DESC
LIMIT 20
```

---

## Advanced Analysis Queries

### 15. Conversation Duration Analysis

```sql
SELECT 
  CASE 
    WHEN duration < 120 THEN '0-2 min'
    WHEN duration < 300 THEN '2-5 min'
    WHEN duration < 600 THEN '5-10 min'
    WHEN duration < 900 THEN '10-15 min'
    ELSE '15+ min'
  END as duration_bucket,
  COUNT(*) as conversation_count,
  ROUND(AVG(client_sentiment_score), 3) as avg_sentiment,
  ROUND(AVG(turn_count), 1) as avg_turns
FROM `project.dataset.conversations`
WHERE medium = 'PHONE_CALL'
GROUP BY duration_bucket
ORDER BY 
  CASE duration_bucket
    WHEN '0-2 min' THEN 1
    WHEN '2-5 min' THEN 2
    WHEN '5-10 min' THEN 3
    WHEN '10-15 min' THEN 4
    ELSE 5
  END
```

### 16. Hour of Day Analysis

```sql
SELECT 
  EXTRACT(HOUR FROM create_time) as hour_of_day,
  COUNT(*) as conversation_count,
  ROUND(AVG(client_sentiment_score), 3) as avg_sentiment,
  ROUND(AVG(duration), 2) as avg_duration
FROM `project.dataset.conversations`
WHERE create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY hour_of_day
ORDER BY hour_of_day
```

### 17. Cohort Analysis

```sql
WITH first_conversation AS (
  SELECT 
    agent_id,
    MIN(DATE(create_time)) as first_date
  FROM `project.dataset.conversations`
  GROUP BY agent_id
),
cohorts AS (
  SELECT 
    c.agent_id,
    fc.first_date as cohort_month,
    DATE_DIFF(DATE(c.create_time), fc.first_date, DAY) as days_since_start,
    c.client_sentiment_score
  FROM `project.dataset.conversations` c
  JOIN first_conversation fc
    ON c.agent_id = fc.agent_id
)
SELECT 
  cohort_month,
  CASE 
    WHEN days_since_start < 7 THEN 'Week 1'
    WHEN days_since_start < 14 THEN 'Week 2'
    WHEN days_since_start < 30 THEN 'Week 3-4'
    ELSE 'Month 2+'
  END as period,
  COUNT(*) as conversation_count,
  ROUND(AVG(client_sentiment_score), 3) as avg_sentiment
FROM cohorts
GROUP BY cohort_month, period
ORDER BY cohort_month, period
```

### 18. Sentiment Recovery Analysis

```sql
WITH sentiment_changes AS (
  SELECT 
    s.conversation_id,
    s.sentence_id,
    s.sentiment_score,
    s.participant_role,
    ROW_NUMBER() OVER (PARTITION BY s.conversation_id ORDER BY s.create_time) as turn_number,
    LAG(s.sentiment_score) OVER (PARTITION BY s.conversation_id ORDER BY s.create_time) as prev_sentiment
  FROM `project.dataset.sentences` s
  WHERE s.participant_role = 'CUSTOMER'
)
SELECT 
  COUNT(DISTINCT conversation_id) as conversations_with_recovery,
  ROUND(AVG(sentiment_score - prev_sentiment), 3) as avg_sentiment_improvement
FROM sentiment_changes
WHERE prev_sentiment < -0.3
  AND sentiment_score > 0
```

---

## Dashboard Queries

### 19. Executive Dashboard Summary

```sql
WITH metrics AS (
  SELECT 
    COUNT(*) as total_conversations,
    ROUND(AVG(client_sentiment_score), 3) as avg_sentiment,
    ROUND(AVG(duration), 2) as avg_duration,
    COUNT(CASE WHEN client_sentiment_score < -0.3 THEN 1 END) as negative_conversations,
    COUNT(DISTINCT agent_id) as active_agents
  FROM `project.dataset.conversations`
  WHERE DATE(create_time) = CURRENT_DATE()
),
previous_metrics AS (
  SELECT 
    COUNT(*) as prev_total_conversations,
    ROUND(AVG(client_sentiment_score), 3) as prev_avg_sentiment
  FROM `project.dataset.conversations`
  WHERE DATE(create_time) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
)
SELECT 
  m.*,
  p.prev_total_conversations,
  p.prev_avg_sentiment,
  m.total_conversations - p.prev_total_conversations as volume_change,
  ROUND((m.avg_sentiment - p.prev_avg_sentiment) * 100, 2) as sentiment_change_pct
FROM metrics m
CROSS JOIN previous_metrics p
```

### 20. Real-Time Alerts Query

```sql
SELECT 
  conversation_id,
  agent_id,
  create_time,
  client_sentiment_score,
  duration,
  'Negative sentiment spike' as alert_type
FROM `project.dataset.conversations`
WHERE create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
  AND client_sentiment_score < -0.5

UNION ALL

SELECT 
  c.conversation_id,
  c.agent_id,
  c.create_time,
  c.client_sentiment_score,
  c.duration,
  'Long duration call' as alert_type
FROM `project.dataset.conversations` c
WHERE c.create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
  AND c.duration > 1800
  AND c.medium = 'PHONE_CALL'

ORDER BY create_time DESC
```

---

## Export Queries for Visualization

### 21. Data for Looker Dashboard

```sql
CREATE OR REPLACE VIEW `project.dataset.dashboard_metrics` AS
SELECT 
  DATE(c.create_time) as date,
  c.agent_id,
  c.medium,
  t.topic_name,
  COUNT(*) as conversation_count,
  ROUND(AVG(c.client_sentiment_score), 3) as avg_customer_sentiment,
  ROUND(AVG(c.agent_sentiment_score), 3) as avg_agent_sentiment,
  ROUND(AVG(c.duration), 2) as avg_duration,
  COUNT(CASE WHEN c.client_sentiment_score >= 0.3 THEN 1 END) as positive_count,
  COUNT(CASE WHEN c.client_sentiment_score <= -0.3 THEN 1 END) as negative_count
FROM `project.dataset.conversations` c
LEFT JOIN `project.dataset.topics` t
  ON c.conversation_id = t.conversation_id
WHERE c.create_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
GROUP BY date, c.agent_id, c.medium, t.topic_name
```

---

## Best Practices

### Query Optimization

✅ Use partitioned tables (by create_time)  
✅ Cluster tables by frequently filtered columns  
✅ Use WHERE clauses to limit data scanned  
✅ Avoid SELECT * in production queries  
✅ Use materialized views for complex aggregations  

### Cost Management

✅ Preview query costs before running  
✅ Use query results caching  
✅ Set up cost controls and alerts  
✅ Archive old data to cheaper storage  
✅ Use approximate aggregation functions when exact precision not needed  

---

## Resources

- BigQuery Documentation: https://cloud.google.com/bigquery/docs
- SQL Reference: https://cloud.google.com/bigquery/docs/reference/standard-sql
- Query Optimization: https://cloud.google.com/bigquery/docs/best-practices-performance-overview
