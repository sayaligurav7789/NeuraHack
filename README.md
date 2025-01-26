# NeuraHack
Azure Text Analytics to analyze public feedback and complaints, enabling  local authorities to improve their services effectively. 

---

# Public Feedback Analysis Using Azure Text Analytics

## Project Overview

This project leverages **Azure Text Analytics** to analyze public feedback and complaints. The goal is to provide insights into the sentiment, key phrases, and overall sentiment scores of the feedback. These insights can be utilized by **local authorities** to improve their services and address issues effectively.

## Features

- **Sentiment Analysis**: Classifies feedback into positive, neutral, or negative categories with corresponding scores.
- **Key Phrase Extraction**: Identifies key phrases from the feedback for targeted insights.
- **Detailed Scoring**: Provides positive, neutral, and negative sentiment scores for each feedback entry.
- **Actionable Insights**: Enables local authorities to prioritize and resolve key issues based on the feedback.

---

## Workflow

1. **Input Data**:  
   Public feedback and complaints are collected and structured into a table format (e.g., CSV/Excel).

2. **Azure Text Analytics**:  
   - Each feedback entry is analyzed for:
     - Sentiment (Positive/Negative/Neutral)
     - Key Phrases
     - Sentiment Scores (Positive, Neutral, Negative)
   - Outputs are generated in a tabular format for easy interpretation.

3. **Insights Generation**:  
   - Sentiment trends are identified (e.g., recurring negative issues).
   - Key phrases highlight specific areas needing improvement.

---

## Example Output

| Feedback                                                         | Sentiment  | Positive Score | Neutral Score | Negative Score | Key Phrases                             |
|------------------------------------------------------------------|------------|----------------|---------------|----------------|------------------------------------------|
| The roads in my area are full of potholes and need urgent repair.| Negative   | 0.0            | 0.11          | 0.89           | urgent repair, roads, area, potholes    |
| The garbage collection service has improved significantly.       | Positive   | 0.78           | 0.12          | 0.1            | garbage collection service              |
| The streetlights in Sector 5 are not working properly.           | Negative   | 0.0            | 0.0           | 1.0            | streetlights, Sector 5                  |
| Excellent response from the water supply department!             | Positive   | 1.0            | 0.0           | 0.0            | water supply department, quick action   |
| Public transport is unreliable, and buses are often delayed.     | Negative   | 0.0            | 0.03          | 0.97           | Public transport, buses                 |

---

## How to Use

### Prerequisites:
1. **Azure Subscription**:  
   Set up an Azure account and enable the **Text Analytics API**.
2. **Data Preparation**:  
   Prepare the feedback data in a structured format (CSV or Excel).
3. **Python or Azure SDK**:  
   Use Python scripts or the Azure SDK to interact with the Text Analytics API.

### Steps:
1. **Connect to Azure Text Analytics API**:
   - Obtain your API key and endpoint URL from the Azure portal.
   - Authenticate using the Azure SDK or REST API.

2. **Analyze Feedback**:
   - Send feedback data to the API for analysis.
   - Retrieve sentiment, scores, and key phrases.

3. **Generate Reports**:
   - Store the output in a readable format (e.g., Excel, CSV, or dashboard).
   - Visualize the data for actionable insights.

---

## Technology Stack

- **Azure Cognitive Services**:
  - Text Analytics API
- **Programming Language**:
  - Python / Azure SDK
- **Data Visualization**:
  - Excel / Power BI / Dashboards
- **Data Storage**:
  - CSV / Excel / Database

---

## Benefits

1. **Improved Decision-Making**:
   - Local authorities can address critical issues by identifying trends in feedback.
2. **Proactive Service Enhancement**:
   - Positive feedback can guide authorities on what to maintain or improve further.
3. **Efficient Resource Allocation**:
   - Prioritization of issues based on sentiment and key phrases.

---

## Future Enhancements

1. **Real-Time Feedback Analysis**:
   - Automate the analysis process for immediate insights.
2. **Integration with Dashboards**:
   - Visualize trends using tools like Power BI or Tableau.
3. **Multilingual Feedback Support**:
   - Analyze feedback in regional languages.

---

Feel free to contribute or reach out for queries!
