from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd

language_key = 'HVfg7PedDIFJDTEoL8WK6igx3IVtxkDvcpwNU3PG17TBddWY0nVnJQQJ99BAACYeBjFXJ3w3AAAaACOGSsWz'
language_endpoint = 'https://textanalytics2166.cognitiveservices.azure.com/'

def authenticate_client():
    credential = AzureKeyCredential(language_key)
    return TextAnalyticsClient(endpoint=language_endpoint, credential=credential)

client = authenticate_client()

feedback_data = [
    "The roads in my area are full of potholes and need urgent repair.",
    "The garbage collection service has improved significantly.",
    "The streetlights in Sector 5 are not working properly.",
    "Excellent response from the water supply department, quick action taken!",
    "Public transport is unreliable, and buses are often delayed."
]

def analyze_feedback(feedback_list):
    response = client.analyze_sentiment(feedback_list, show_opinion_mining=True)
    results = []

    for idx, feedback in enumerate(response):
        if not feedback.is_error:
            result = {
                "Feedback": feedback_list[idx],
                "Sentiment": feedback.sentiment,
                "Positive Score": feedback.confidence_scores.positive,
                "Neutral Score": feedback.confidence_scores.neutral,
                "Negative Score": feedback.confidence_scores.negative,
                "Key Phrases": ", ".join([phrase for phrase in client.extract_key_phrases([feedback_list[idx]])[0].key_phrases])
            }
            results.append(result)
        else:
            print(f"Error in feedback {idx + 1}: {feedback.error.message}")
    
    return pd.DataFrame(results)

feedback_analysis = analyze_feedback(feedback_data)

feedback_analysis.to_csv("feedback_analysis.csv", index=False)
print("Feedback analysis results saved to 'feedback_analysis.csv'.")
print(feedback_analysis)
