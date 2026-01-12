# BeautifulSoup4 크롤링 파이프라인 학습 프로젝트

## 📚 프로젝트 소개

이 프로젝트는 BeautifulSoup4를 이용한 웹 크롤링 파이프라인을 단계별로 학습할 수 있도록 구성되었습니다.
**Q&A 형식**으로 진행하며, 각 질문에 답하면서 코드를 완성해나갑니다.

### 학습 주제
**뉴스 헤드라인 크롤링 파이프라인** - 간단한 뉴스 사이트에서 헤드라인을 수집하고 저장하는 시스템

---

## 🕷️ 웹 크롤링(Web Crawling)이란?

### 개념
**웹 크롤링(Web Crawling)**은 인터넷에서 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 기술입니다.
인간이 브라우저에서 웹사이트를 방문하여 정보를 읽는 것과 유사하지만, 프로그램을 통해 자동화된 방식으로 수행됩니다.

### 크롤링의 동작 과정
1. **웹 페이지 요청**: HTTP 요청을 통해 웹 페이지의 HTML을 가져옴
2. **HTML 파싱**: 가져온 HTML을 분석하여 구조를 이해
3. **데이터 추출**: 원하는 정보(텍스트, 링크, 이미지 등)를 추출
4. **데이터 저장**: 추출한 데이터를 파일이나 데이터베이스에 저장
5. **다음 페이지 탐색**: 링크를 따라 다른 페이지로 이동 (선택사항)

### 크롤링의 활용 분야
- **데이터 수집**: 뉴스, 상품 정보, 가격 비교 등
- **시장 조사**: 경쟁사 분석, 트렌드 파악
- **연구 및 분석**: 논문 데이터, 통계 정보 수집
- **콘텐츠 모니터링**: 특정 키워드나 주제 추적
- **자동화**: 정기적인 데이터 업데이트

### 크롤링 vs 스크래핑
| 용어 | 설명 | 차이점 |
|------|------|--------|
| **크롤링(Crawling)** | 여러 웹 페이지를 자동으로 탐색하고 방문하는 과정 | 여러 페이지를 순회 |
| **스크래핑(Scraping)** | 특정 웹 페이지에서 데이터를 추출하는 과정 | 단일 페이지에서 데이터 추출 |

**실제로는 두 용어가 혼용되어 사용되며, 일반적으로 "크롤링"으로 통칭됩니다.**

### 크롤링 시 고려사항
1. **로봇 배제 표준(robots.txt)**: 웹사이트가 크롤링을 허용하는지 확인
2. **요청 간격**: 서버에 부하를 주지 않도록 적절한 delay 설정
3. **저작권**: 크롤링한 데이터의 사용 목적과 범위 확인
4. **법적 준수**: 웹사이트의 이용약관 및 관련 법규 준수
5. **에러 처리**: 네트워크 오류, 페이지 구조 변경 등에 대비

### 크롤링 도구
- **BeautifulSoup4**: HTML 파싱 및 데이터 추출 (정적 페이지)
- **Selenium**: 브라우저 자동화 (동적 페이지, JavaScript 필요)
- **Scrapy**: 대규모 크롤링 프레임워크
- **Requests**: HTTP 요청 라이브러리

**이 프로젝트에서는 BeautifulSoup4를 사용하여 정적 HTML 페이지를 크롤링합니다.**

---

## 🔍 BeautifulSoup4란?

### 개념
**BeautifulSoup4(BS4)**는 Python에서 HTML과 XML 문서를 파싱하고 탐색하기 위한 라이브러리입니다. 
웹 크롤링에서 가장 널리 사용되는 도구 중 하나로, 복잡한 HTML 구조에서 원하는 데이터를 쉽게 추출할 수 있게 해줍니다.

### 주요 특징
- **직관적인 API**: CSS 선택자, 태그명, 클래스명 등으로 쉽게 요소를 찾을 수 있음
- **유연한 파싱**: 여러 파서(html.parser, lxml, html5lib) 지원
- **견고한 에러 처리**: 깨진 HTML도 자동으로 수정하여 파싱 가능
- **다양한 탐색 방법**: find(), find_all(), select(), select_one() 등

### 왜 BeautifulSoup4를 사용할까요?

1. **간단한 문법**: 복잡한 정규표현식 없이도 HTML 요소를 쉽게 찾을 수 있음
   ```python
   # BeautifulSoup4 사용
   soup.find('div', class_='headline')  # 직관적!
   
   # 정규표현식 사용 (복잡함)
   import re
   re.search(r'<div class="headline">.*?</div>', html)  # 복잡함
   ```

2. **CSS 선택자 지원**: 웹 개발에 익숙한 CSS 선택자를 그대로 사용 가능
   ```python
   soup.select('div.headline > a')  # CSS 선택자 사용
   ```

3. **데이터 추출 용이**: 텍스트, 속성값 등을 간단하게 추출
   ```python
   element.text  # 텍스트 추출
   element['href']  # 속성값 추출
   ```

4. **활발한 커뮤니티**: 널리 사용되어 자료와 도움을 쉽게 얻을 수 있음

### BeautifulSoup4 vs 다른 도구
- **정규표현식**: HTML 구조가 복잡할수록 유지보수가 어려움
- **lxml 직접 사용**: 더 빠르지만 API가 복잡함
- **Selenium**: 브라우저 자동화가 필요할 때만 사용 (무거움)

**결론**: BeautifulSoup4는 정적 HTML 크롤링에 최적화된 간단하고 강력한 도구입니다!

---

## 🎯 학습 목표

1. BeautifulSoup4 기본 사용법 이해
2. 웹 크롤링 파이프라인 아키텍처 설계
3. 코드 모듈화 및 재사용성 향상
4. 에러 처리 및 로깅 구현
5. 데이터 저장 및 관리

---

## 📋 사전 준비사항

### Q1: 필요한 패키지들을 설치하기 위해 `requirements.txt` 파일을 만들어야 합니다.
**질문**: BeautifulSoup4 크롤링에 필요한 주요 패키지들은 무엇일까요?
- 웹 페이지 요청: `requests`
- HTML 파싱: `beautifulsoup4`
- 데이터 저장: `pandas` (선택사항)
- 로깅: Python 내장 `logging` 모듈 사용

**과제**: `requirements.txt` 파일을 작성하세요.

---

## 🏗️ 아키텍처 설계

### Q2: 크롤링 파이프라인을 어떻게 구성하면 좋을까요?
**질문**: 크롤링 파이프라인은 보통 어떤 단계로 나뉠까요?

**힌트**:
1. **설정 관리** (config.py) - URL, 저장 경로 등 설정
2. **웹 요청** (scraper.py) - HTTP 요청 및 응답 처리
3. **데이터 파싱** (scraper.py) - BeautifulSoup으로 HTML 파싱
4. **데이터 처리** (pipeline.py) - 데이터 정제 및 변환
5. **데이터 저장** (pipeline.py) - 파일 또는 DB 저장
6. **에러 처리** (utils.py) - 예외 처리 및 로깅

**과제**: 각 모듈의 역할을 이해하고, 파일 구조를 파악하세요.

---

## 📝 단계별 학습 가이드

### Step 1: 설정 파일 작성 (config.py)

#### Q3: 크롤링에 필요한 설정 정보는 무엇일까요?
**질문**: 
- 크롤링할 웹사이트 URL은?
- User-Agent는 왜 필요한가?
- 데이터를 저장할 경로는?
- 요청 간 대기 시간(delay)은 얼마나?

**과제**: `config.py` 파일을 완성하세요.

##### 🎯 안전한 크롤링 사이트 추천

크롤링 연습을 위해 **저작권 및 보안 문제가 없는** 안전한 사이트들을 추천합니다:

1. **Quotes to Scrape** (추천 ⭐)
   - URL: `https://quotes.toscrape.com`
   - 특징: 크롤링 연습을 위해 만들어진 사이트, 명언과 작가 정보
   - 장점: 구조가 단순하고 명확함, robots.txt 허용
   - 추출 가능: 명언 텍스트, 작가명, 태그

2. **Books to Scrape**
   - URL: `https://books.toscrape.com`
   - 특징: 크롤링 연습용 가상 서점 사이트
   - 장점: 여러 페이지, 다양한 데이터 구조
   - 추출 가능: 책 제목, 가격, 평점, 재고 상태

3. **Hacker News**
   - URL: `https://news.ycombinator.com`
   - 특징: 기술 뉴스 사이트, 크롤링 허용
   - 장점: 실전 연습에 적합, API도 제공
   - 추출 가능: 뉴스 제목, 링크, 점수, 댓글 수

4. **httpbin.org** (테스트용)
   - URL: `https://httpbin.org/html`
   - 특징: HTTP 테스트용 사이트
   - 장점: 간단한 HTML 구조로 테스트하기 좋음

**⚠️ 주의**: 실제 상업 사이트를 크롤링하기 전에 반드시 `robots.txt`를 확인하고, 서비스 약관을 읽어보세요!

```python
# 예시 구조 (완성하지 말고, 스켈레톤만 참고)
# 추천: Quotes to Scrape 사용
NEWS_URL = "https://quotes.toscrape.com"  # 크롤링할 사이트
USER_AGENT = "..."  # 무엇을 넣어야 할까요?
SAVE_PATH = "..."  # 어디에 저장할까요?
REQUEST_DELAY = ...  # 몇 초로 설정할까요?
```

---

### Step 2: 유틸리티 함수 작성 (utils.py)

#### Q4: 크롤링 시 필요한 유틸리티 함수들은?
**질문**:
1. 로깅을 설정하려면 어떻게 해야 할까요?
2. 파일 경로를 안전하게 생성하려면?
3. 요청 간 대기 시간을 처리하려면?

**과제**: `utils.py`에 다음 함수들을 구현하세요:
- `setup_logging()` - 로깅 설정
- `ensure_directory()` - 디렉토리 생성
- `delay()` - 요청 간 대기

---

### Step 3: 스크래퍼 클래스 작성 (scraper.py)

#### Q5: 스크래퍼 클래스는 어떤 메서드가 필요할까요?
**질문**:
1. 웹 페이지를 요청하는 메서드는?
2. HTML을 파싱하는 메서드는?
3. 헤드라인을 추출하는 메서드는?
4. 에러 처리는 어떻게 할까요?

**과제**: `scraper.py`의 `NewsScraper` 클래스를 완성하세요.

**힌트**:
```python
class NewsScraper:
    def __init__(self, url, user_agent):
        # 초기화 코드 작성
    
    def fetch_page(self):
        # requests로 페이지 가져오기
        # 에러 처리 추가
    
    def parse_html(self, html_content):
        # BeautifulSoup으로 파싱
        # 어떤 파서를 사용할까요?
    
    def extract_headlines(self, soup):
        # CSS 선택자 또는 find() 메서드 사용
        # 어떤 선택자를 사용할까요?
```

---

### Step 4: 파이프라인 작성 (pipeline.py)

#### Q6: 파이프라인은 어떻게 데이터를 처리할까요?
**질문**:
1. 스크래퍼에서 받은 데이터를 어떻게 정제할까요?
2. 데이터를 어떤 형식으로 저장할까요? (JSON, CSV, TXT?)
3. 중복 데이터는 어떻게 처리할까요?

**과제**: `pipeline.py`의 `CrawlingPipeline` 클래스를 완성하세요.

**힌트**:
```python
class CrawlingPipeline:
    def __init__(self, scraper, save_path):
        # 초기화
    
    def clean_data(self, headlines):
        # 데이터 정제 (공백 제거, 중복 제거 등)
    
    def save_data(self, data, filename):
        # 파일로 저장 (JSON 또는 CSV)
    
    def run(self):
        # 전체 파이프라인 실행
        # 1. 스크래퍼로 데이터 수집
        # 2. 데이터 정제
        # 3. 데이터 저장
```

---

### Step 5: 메인 실행 파일 작성 (main.py)

#### Q7: 메인 파일에서는 무엇을 해야 할까요?
**질문**:
1. 모든 모듈을 어떻게 연결할까요?
2. 에러 처리는 어디서 할까요?
3. 사용자에게 결과를 어떻게 보여줄까요?

**과제**: `main.py`를 완성하여 전체 파이프라인을 실행하세요.

---

## 🚀 실행 방법

각 단계를 완성한 후:

```bash
# 패키지 설치
pip install -r requirements.txt

# 실행
python main.py
```

---

## 💡 추가 학습 과제

### Q8: 파이프라인을 개선하려면?
1. **멀티페이지 크롤링**: 여러 페이지를 순회하며 크롤링
2. **데이터베이스 저장**: SQLite나 MySQL에 저장
3. **스케줄링**: 정기적으로 크롤링 실행
4. **병렬 처리**: 여러 페이지를 동시에 크롤링
5. **데이터 분석**: 수집한 데이터로 간단한 분석

---

## 📖 참고 자료

- [BeautifulSoup4 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests 라이브러리 문서](https://requests.readthedocs.io/)
- [Python 로깅 가이드](https://docs.python.org/3/howto/logging.html)

---

## ⚠️ 주의사항

1. **로봇 배제 표준(robots.txt) 확인**: 크롤링 전에 웹사이트의 robots.txt를 확인하세요
2. **요청 간격**: 서버에 부하를 주지 않도록 적절한 delay를 설정하세요
3. **저작권**: 크롤링한 데이터의 사용 목적을 확인하세요
4. **에러 처리**: 네트워크 오류, 파싱 오류 등을 적절히 처리하세요

---

## 🎓 학습 체크리스트

- [ ] Step 1: config.py 완성
- [ ] Step 2: utils.py 완성
- [ ] Step 3: scraper.py 완성
- [ ] Step 4: pipeline.py 완성
- [ ] Step 5: main.py 완성
- [ ] 전체 파이프라인 실행 및 테스트
- [ ] 에러 처리 및 로깅 확인
- [ ] 추가 개선 사항 구현

---

**Happy Crawling! 🕷️**
