"""
메인 실행 파일
Q7: 이 파일을 완성하여 전체 파이프라인을 실행하세요.
"""

# Q7-1: 필요한 모듈들을 import하세요.
# 힌트: config, utils, scraper, pipeline

# Q7-2: 로깅을 설정하세요.
# 힌트: utils.setup_logging() 사용


def main():
    """
    메인 함수
    Q7-3: 전체 파이프라인을 실행하는 코드를 작성하세요.
    
    프로세스:
    1. 설정 확인 (config에서 값 가져오기)
    2. NewsScraper 인스턴스 생성
    3. CrawlingPipeline 인스턴스 생성
    4. pipeline.run() 실행
    5. 에러 처리 (try-except)
    6. 결과 출력
    """
    # TODO: 메인 로직 작성
    
    # 예시 구조:
    # try:
    #     scraper = NewsScraper(...)
    #     pipeline = CrawlingPipeline(...)
    #     result = pipeline.run()
    #     print(f"크롤링 완료! {len(result)}개의 헤드라인을 수집했습니다.")
    # except Exception as e:
    #     logging.error(f"에러 발생: {e}")
    pass


if __name__ == "__main__":
    main()
