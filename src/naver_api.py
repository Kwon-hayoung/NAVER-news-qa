import os
import requests
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def search_news(query, display=5, start=1, sort="date"):
    """
    네이버 뉴스 검색 API 호출
    :param query: 검색어
    :param display: 가져올 뉴스 개수 (최대 100)
    :param start: 검색 시작 위치
    :param sort: 정렬 (sim:유사도, date:날짜순)
    :return: 뉴스 JSON 결과
    """
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": display,
        "start": start,
        "sort": sort
    }

    res = requests.get(url, headers=headers, params=params)
    res.raise_for_status()
    return res.json()
