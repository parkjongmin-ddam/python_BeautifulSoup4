"""
크롤링 파이프라인 설정 파일
Q3: 이 파일을 완성하세요.
"""

# 크롤링할 뉴스 사이트 URL
# Q3-1: 어떤 뉴스 사이트를 크롤링할까요?
# 
# 🎯 안전한 크롤링 사이트 추천 (저작권 및 보안 문제 없음):
# 1. "https://quotes.toscrape.com" - 크롤링 연습용 명언 사이트 (추천!)
# 2. "https://books.toscrape.com" - 크롤링 연습용 서점 사이트
# 3. "https://news.ycombinator.com" - Hacker News (크롤링 허용)
# 4. "https://httpbin.org/html" - HTTP 테스트용 사이트
#
# 예시: "https://quotes.toscrape.com"
NEWS_URL = ""

# User-Agent 설정
# Q3-2: User-Agent는 왜 필요할까요? 적절한 값을 설정하세요.
# 힌트: 브라우저의 User-Agent 문자열을 모방합니다
USER_AGENT = ""

# 데이터 저장 경로
# Q3-3: 크롤링한 데이터를 어디에 저장할까요?
SAVE_PATH = ""

# 요청 간 대기 시간 (초)
# Q3-4: 서버에 부하를 주지 않기 위해 몇 초로 설정할까요?
REQUEST_DELAY = 0

# 요청 타임아웃 (초)
REQUEST_TIMEOUT = 10

# 저장 파일 형식
# Q3-5: 데이터를 어떤 형식으로 저장할까요? ("json", "csv", "txt")
SAVE_FORMAT = ""

# 로그 파일 경로
LOG_FILE = "crawler.log"
