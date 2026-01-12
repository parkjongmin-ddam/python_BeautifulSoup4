"""
유틸리티 함수 모음
Q4: 이 파일의 함수들을 완성하세요.
"""

import os
import time
import logging
from pathlib import Path


def setup_logging(log_file="crawler.log", level=logging.INFO):
    """
    로깅 설정 함수
    Q4-1: 로깅을 어떻게 설정해야 할까요?
    
    힌트:
    - logging.basicConfig()를 사용합니다
    - 파일과 콘솔에 모두 로그를 출력하도록 설정하세요
    - 포맷: 시간, 레벨, 메시지
    """
    # TODO: 로깅 설정 코드 작성
    pass


def ensure_directory(directory_path):
    """
    디렉토리가 없으면 생성하는 함수
    Q4-2: 디렉토리를 안전하게 생성하려면?
    
    힌트:
    - os.path.exists() 또는 Path.exists() 사용
    - os.makedirs() 또는 Path.mkdir() 사용
    - exist_ok=True 옵션 고려
    """
    # TODO: 디렉토리 생성 코드 작성
    pass


def delay(seconds):
    """
    요청 간 대기 시간 처리 함수
    Q4-3: time.sleep()을 사용하여 대기 시간을 구현하세요.
    """
    # TODO: 대기 시간 구현
    pass


def format_timestamp():
    """
    현재 시간을 문자열로 반환하는 함수 (선택사항)
    파일명에 타임스탬프를 추가할 때 사용
    """
    # TODO: 타임스탬프 포맷팅 (예: "2024-01-01_12-00-00")
    pass
