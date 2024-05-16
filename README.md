# 시네마 미슐랭가이드 

## 구성원(역할)
**오승주** 
```
유튜브댓글 크롤링 및 정제, 데이터 분석해 키워드, 영화 평가 분석
```
**유윤태** 
```
유튜브댓글 크롤링 및 정제, 데이터 분석해 키워드, 영화 평가 분석
```
**윤혜진** 
```
영화정보 크롤링 or 영화정보 api 이용, 가져온 데이터 정제, 정제된 데이터를 활용해 영화 추천, 정보,찜 기능 제작
```

**추희정**
```
영화정보 크롤링 or 영화정보 api 이용, 가져온 데이터 정제, 정제된 데이터를 활용해 영화 추천, 정보,찜 기능 제작
```


## 목표(목적)
- 사용자 입력을 기반으로 해당 영화의 정보 제공 및 추천 시스템
- 유튜브 댓글을 통해 다른 사용자들의 의견이나 반응을 수집, 분석하여 해당영화 리뷰 제공

## 예상산출물 개요
**영화정보제공, 추천어플**
- 유형별 추천(검색항목)
    - 비슷한장르
    - 같은 감독 작품
    - 개봉 연도별
    - 배우별 추천
- 영화정보 제공(제목검색)
    - 영화 관련 키워드 제공(5가지정도)
    - 영화평가
- 부가기능
  - 영화 찜기능
  

## 사용기술(툴)
- python, KoNLPy 패키지 
- pandas, BeautifulSoup, selenium
- MySQL, vscode
- Youtube Data API, 영화진흥 위원회 API
- 협업툴
  - github
  - 
## 구현방법
- OpenAPI 영화정보를 가져와서 DB에 저장
- 유형별 추천은 DB에서 정보를 가져와서 키워드별 랜덤으로 영화 추천
- 영화를 검색하면 DB에서 데이터를 가져오고 유튜브에 검색 후 댓글크롤링 -> 많이 나온 키워드5가지 제공 및 간략한 영화 평가 제공
- 원하는 영화는 따로 찜기능(db에 저장)
  
## 데이터출처
- [공공데이터포털](https://www.data.go.kr/data/3076402/openapi.do)
- [영화진흥위원회](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)
- [Youtube](https://www.youtube.com/)
  
## 향후 개선 방향
- 추천시스템알고리즘 구축
