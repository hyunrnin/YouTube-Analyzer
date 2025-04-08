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

def get_video_info(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        print("Invalid video URL")
        return None

    api_url = (
        f"https://www.googleapis.com/youtube/v3/videos"
        f"?part=snippet,statistics&id={video_id}&key={YOUTUBE_API_KEY}"
    )

    response = requests.get(api_url)
    data = response.json()

    if "items" not in data:
        print(f"API 오류: {data.get('error', {}).get('message', '알 수 없는 오류')}")
        return None

    item = data["items"][0]
    snippet = item["snippet"]
    stats = item["statistics"]

    return {
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "published": snippet["publishedAt"][:10],
        "description": snippet.get("description", ""),
        "views": int(stats.get("viewCount", 0)),
        "likes": int(stats.get("likeCount", 0)),
        "comments": int(stats.get("commentCount", 0))
    }
