def summarize_sentiment(results):
    counts = {"positive": 0, "neutral": 0, "negative": 0}
    total = 0

    for _, sentiment, _ in results:
        if sentiment in counts:
            counts[sentiment] += 1
            total += 1

    if total == 0:
        return "분석 가능한 댓글이 없습니다."

    pos_ratio = counts["positive"] / total
    neg_ratio = counts["negative"] / total

    if pos_ratio > 0.5:
        return "이 영상은 긍정적으로 평가되었습니다."
    elif neg_ratio > 0.5:
        return "이 영상은 부정적인 반응이 많습니다."
    else:
        return "이 영상은 중립적인 평가를 받고 있습니다."
