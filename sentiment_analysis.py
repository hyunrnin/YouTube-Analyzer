import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def analyze_sentiments(comments):
    results = []

    for comment in comments:
        try:
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": comment[:512]})
            output = response.json()

            first_result = output[0][0]

            label = first_result["label"]
            if label == 'LABEL_2':
                sentiment = "positive"
            elif label == 'LABEL_1':
                sentiment = "neutral"
            elif label == 'LABEL_0':
                sentiment = "negative"
            else:
                sentiment = "error"

            results.append((comment, sentiment, round(first_result["score"], 4)))

        except Exception as e:
            results.append((comment, "error", 0.0))

    return results
