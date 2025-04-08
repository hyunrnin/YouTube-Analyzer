# 🎥 YouTube 영상 분석기

YouTube 영상의 댓글을 수집하고 감성 분석을 진행하는 프로그램입니다.  
영상의 제목, 조회수, 좋아요 수 등 메타데이터를 수집하고, 댓글에 대한 **긍정/중립/부정** 감성 분석을 수행합니다.

---

## 👤 MADE BY

- **김현민**

---

## ✅ 주요 기능

- YouTube API를 이용해 영상의 메타데이터 수집 (제목, 채널명, 조회수 등)
- 영상의 댓글을 수집하고 감성 분석을 진행
- Hugging Face 모델을 활용한 감성 분석 (긍정적, 중립적, 부정적 평가)
- 감성 분석 결과를 **콘솔**에 출력

---

## 📦 설치 방법

1. 레포 클론

```bash
git clone https://github.com/your-username/youtube-analyzer.git
cd youtube-analyzer
```

2. 패키지 설치

```bash
pip install -r requirements.txt
```

---

## ⚙️ 환경 설정 (.env 파일)

1. `.env.example` 파일을 복사하여 `.env` 파일 생성

```bash
cp .env.example .env
```

2. 아래 정보를 입력

```env
YT_API_KEY=your_youtube_api_key_here
HF_API_KEY=your_huggingface_api_key_here
```

---

## ▶️ 실행 방법

```bash
python main.py
```

유튜브 영상 URL을 입력하면, 해당 영상의 **메타데이터**와 **댓글**에 대한 감성 분석 결과가 출력됩니다.

---

## 📂 GitHub에 포함되지 않는 파일

`.gitignore`에 의해 아래 파일은 업로드되지 않습니다:

- `.env` (API 키 보안)
- `__pycache__/` (파이썬 캐시)

---

## 💡 확장 아이디어

- 웹 인터페이스 (Gradio, Streamlit 등)
- 댓글 분석 결과를 시각화 (그래프 등)
- 여러 개의 영상에 대해 분석 자동화

---

## 🧠 라이선스 & 출처

- YouTube API: [YouTube Data API v3](https://developers.google.com/youtube/v3)
- 감성 분석 모델: [Hugging Face Transformers](https://huggingface.co/transformers/)

---
