from yt_video_info import get_video_info
from yt_comments import get_comments
from sentiment_analysis import analyze_sentiments

def main():
    video_url = input("유튜브 영상 URL을 입력하세요: ")
    
    print("[1] 영상 정보 수집 중...")
    try:
        # 영상 정보 수집
        info = get_video_info(video_url)
        if info:
            print(f"제목: {info['title']}")
            print(f"채널: {info['channel']}")
            print(f"업로드: {info['published']}")
            print(f"조회수: {info['views']:,}")
            print(f"좋아요: {info['likes']:,}")
            print(f"댓글 수: {info['comments']:,}")
        else:
            print("영상 정보를 가져오는 데 실패했습니다.")
            return

        print("\n[2] 댓글 수집 중...")
        comments = get_comments(video_url, max_results=100)
        if comments:
            print(f"{len(comments)}개의 댓글을 수집했습니다.")
        else:
            print("댓글 수집에 실패했습니다.")
            return

        print("\n[3] 감성 분석 중...")
        results = analyze_sentiments(comments)

        # 분석 요약
        positive = sum(1 for _, sentiment, _ in results if sentiment == 'positive')
        neutral = sum(1 for _, sentiment, _ in results if sentiment == 'neutral')
        negative = sum(1 for _, sentiment, _ in results if sentiment == 'negative')

        total = len(results)
        if total == 0:
            print("[4] 분석 요약: 분석 가능한 댓글이 없습니다.")
        else:
            overall_sentiment = "Neutral"
            if positive > negative:
                overall_sentiment = "Positive"
            elif negative > positive:
                overall_sentiment = "Negative"

            print(f"[4] 분석 요약: 이 영상은 {overall_sentiment} 평가를 받았습니다.")
            print(f"분석된 댓글 수: {total}")
            print(f"긍정적: {positive}, 중립적: {neutral}, 부정적: {negative}")

    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
