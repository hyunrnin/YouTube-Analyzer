import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YT_API_KEY")

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:\?|$)"
    match = re.search(regex, url)
    return match.group(1) if match else None

def clean_text(text):
    clean_text = re.sub(r'<.*?>', '', text)
    clean_text = re.sub(r'&[a-zA-Z0-9]+;', '', clean_text)
    clean_text = re.sub(r'http\S+', '', clean_text)
    clean_text = re.sub(r'[^\x00-\x7F]+', '', clean_text)
    clean_text = re.sub(r'^\s*$', '', clean_text)
    
    if len(clean_text) < 3:
        return ""
    
    return clean_text

def get_comments(video_url, max_results=200):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("유효한 유튜브 URL이 아닙니다.")

    comments = []
    url = (
        f"https://www.googleapis.com/youtube/v3/commentThreads"
        f"?part=snippet&videoId={video_id}&maxResults={max_results}&key={YOUTUBE_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        print(f"API 오류: {data.get('error', {}).get('message', '알 수 없는 오류')}")
        return []

    for item in data.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        clean_comment = clean_text(comment)
        if clean_comment:
            comments.append(clean_comment)

    return comments
