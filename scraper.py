"""
뉴스 헤드라인 스크래퍼 클래스
Q5: 이 클래스를 완성하세요.
"""

import requests
from bs4 import BeautifulSoup
import logging
from utils import delay
import config


class NewsScraper:
    """
    뉴스 헤드라인을 크롤링하는 클래스
    """
    
    def __init__(self, url=None, user_agent=None, delay_seconds=1):
        """
        스크래퍼 초기화
        Q5-1: 필요한 속성들을 초기화하세요.
        
        힌트:
        - url: 크롤링할 웹사이트 URL
        - user_agent: HTTP 요청 헤더에 사용할 User-Agent
        - delay_seconds: 요청 간 대기 시간
        - session: requests.Session() 객체 (선택사항, 성능 향상)
        """
        # TODO: 초기화 코드 작성
        pass
    
    def fetch_page(self, url=None):
        """
        웹 페이지를 가져오는 메서드
        Q5-2: requests를 사용하여 페이지를 가져오세요.
        
        질문:
        - headers에 User-Agent를 어떻게 추가할까요?
        - timeout은 어떻게 설정할까요?
        - 에러 처리는 어떻게 할까요? (ConnectionError, Timeout 등)
        
        반환값: response.text (HTML 내용)
        """
        # TODO: 웹 페이지 요청 코드 작성
        # 힌트: requests.get(url, headers={...}, timeout=...)
        pass
    
    def parse_html(self, html_content):
        """
        HTML을 BeautifulSoup 객체로 파싱하는 메서드
        Q5-3: BeautifulSoup을 사용하여 HTML을 파싱하세요.
        
        질문:
        - 어떤 파서를 사용할까요? ("html.parser", "lxml", "html5lib")
        - 각 파서의 장단점은?
        
        반환값: BeautifulSoup 객체
        """
        # TODO: HTML 파싱 코드 작성
        # 힌트: BeautifulSoup(html_content, "html.parser")
        pass
    
    def extract_headlines(self, soup):
        """
        HTML에서 헤드라인을 추출하는 메서드
        Q5-4: CSS 선택자 또는 find() 메서드를 사용하여 헤드라인을 추출하세요.
        
        질문:
        - 크롤링할 사이트의 HTML 구조를 어떻게 파악할까요?
        - 어떤 CSS 선택자를 사용할까요?
        - find_all()과 select() 중 어떤 것을 사용할까요?
        
        반환값: 헤드라인 리스트
        """
        # TODO: 헤드라인 추출 코드 작성
        # 힌트: soup.select("CSS 선택자") 또는 soup.find_all("태그명", class_="클래스명")
        pass
    
    def scrape(self):
        """
        전체 크롤링 프로세스를 실행하는 메서드
        Q5-5: 위의 메서드들을 연결하여 전체 프로세스를 구현하세요.
        
        프로세스:
        1. fetch_page()로 페이지 가져오기
        2. parse_html()로 HTML 파싱
        3. extract_headlines()로 헤드라인 추출
        4. delay()로 대기 (다음 요청 전)
        
        반환값: 헤드라인 리스트
        """
        # TODO: 전체 크롤링 프로세스 구현
        pass
