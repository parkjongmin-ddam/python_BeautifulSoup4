"""
크롤링 파이프라인 클래스
Q6: 이 클래스를 완성하세요.
"""

import json
import csv
import logging
from pathlib import Path
from utils import ensure_directory, format_timestamp
import config


class CrawlingPipeline:
    """
    크롤링 데이터를 처리하고 저장하는 파이프라인 클래스
    """
    
    def __init__(self, scraper, save_path=None, save_format="json"):
        """
        파이프라인 초기화
        Q6-1: 필요한 속성들을 초기화하세요.
        
        힌트:
        - scraper: NewsScraper 인스턴스
        - save_path: 데이터 저장 경로
        - save_format: 저장 형식 ("json", "csv", "txt")
        """
        # TODO: 초기화 코드 작성
        pass
    
    def clean_data(self, headlines):
        """
        데이터 정제 메서드
        Q6-2: 수집한 헤드라인 데이터를 정제하세요.
        
        질문:
        - 공백을 어떻게 제거할까요? (strip())
        - 빈 문자열은 어떻게 처리할까요?
        - 중복된 헤드라인은 어떻게 제거할까요?
        - 텍스트 정규화가 필요한가요?
        
        반환값: 정제된 헤드라인 리스트
        """
        # TODO: 데이터 정제 코드 작성
        # 힌트: list comprehension, set()을 사용한 중복 제거
        pass
    
    def save_to_json(self, data, filepath):
        """
        JSON 형식으로 저장하는 메서드
        Q6-3: 데이터를 JSON 파일로 저장하세요.
        
        힌트:
        - json.dump() 또는 json.dumps() 사용
        - ensure_ascii=False로 한글 지원
        - indent=2로 가독성 향상
        """
        # TODO: JSON 저장 코드 작성
        pass
    
    def save_to_csv(self, data, filepath):
        """
        CSV 형식으로 저장하는 메서드
        Q6-4: 데이터를 CSV 파일로 저장하세요.
        
        힌트:
        - csv.writer() 또는 pandas.to_csv() 사용
        - 헤더 행 추가 고려
        """
        # TODO: CSV 저장 코드 작성
        pass
    
    def save_to_txt(self, data, filepath):
        """
        TXT 형식으로 저장하는 메서드
        Q6-5: 데이터를 텍스트 파일로 저장하세요.
        
        힌트:
        - 각 헤드라인을 한 줄씩 저장
        - 인코딩: utf-8
        """
        # TODO: TXT 저장 코드 작성
        pass
    
    def save_data(self, data, filename=None):
        """
        데이터를 파일로 저장하는 메서드
        Q6-6: 저장 형식에 따라 적절한 메서드를 호출하세요.
        
        프로세스:
        1. 저장 디렉토리 생성 (ensure_directory)
        2. 파일명 생성 (타임스탬프 포함 고려)
        3. 저장 형식에 따라 적절한 메서드 호출
        """
        # TODO: 데이터 저장 코드 작성
        pass
    
    def run(self):
        """
        전체 파이프라인 실행 메서드
        Q6-7: 전체 프로세스를 연결하세요.
        
        프로세스:
        1. scraper.scrape()로 데이터 수집
        2. clean_data()로 데이터 정제
        3. save_data()로 데이터 저장
        4. 로깅 및 결과 반환
        """
        # TODO: 전체 파이프라인 실행 코드 작성
        pass
