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
            # Hugging Face API로 감성 분석 요청
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": comment[:512]})
            output = response.json()  # response.json()이 리스트 안에 리스트 형태로 반환됨

            # 이중 인덱싱을 사용하여 첫 번째 결과에 접근
            first_result = output[0][0]

            # 레이블을 감정으로 매핑 (모델의 레이블을 긍정, 중립, 부정으로 변환)
            label = first_result["label"]
            if label == 'LABEL_2':  # 긍정
                sentiment = "positive"
            elif label == 'LABEL_1':  # 중립
                sentiment = "neutral"
            elif label == 'LABEL_0':  # 부정
                sentiment = "negative"
            else:
                sentiment = "error"

            results.append((comment, sentiment, round(first_result["score"], 4)))

        except Exception as e:
            results.append((comment, "error", 0.0))

    return results
