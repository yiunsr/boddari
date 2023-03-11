# 보따리 프로젝트
* 한국어 문장 수집 프로젝트
* 한국어 말뭉치 프로젝트들이 많이 존재하지만 회원가입을 해야하고 약정서를 제출해야하는 경우가 있다.
 이러한 제약없이 문제없는 글들을 수집하는 프로젝트입니다. 
* 가능한 publick domain, 지적재산권이 만료된 저작물, CCL 라이선스 데이터(가능한 CC-BY, CC-BY-SA),  공공누리 라이선스(가능한 제 1유형 : 출처표시), 기증 저작물을 수집한다.


## LICENSE
* 소스코드가 존재하는 경우 
  * Apache License
* 한국어문장 라이선스는 사용하는 말뭉치 자체 리소스에 따라 결정됩니다. 해당 리소스의 설명을 확인하세요.
  * cc 라이선스(크리에이티브 커먼즈 라이선스)
    * http://ccl.cckorea.org/about/
    * https://gongu.copyright.or.kr/gongu/main/contents.do?menuNo=200093
  * 공공누리 라이선스
    * https://www.data.go.kr/ugs/selectPortalPolicyView.do
    * https://www.kogl.or.kr/info/license.do

## 사용법
* 모든 폴더는 말뭉치 종류입니다. 
* 결과 파일만 필요한 경우 boddari 폴더에서 다운받으세요.
* 해당 말뭉치를 수집이 필요한 경우 해당 프로젝트 하위의 scrap.py 를 통해 수집할 수 있습니다.
  * 프로젝트에 따라서 파일을 다운받거나 sqlite database 를 생성하게 됩니다.
* 수집된 파일이나 db에 대해 csv 파일이 필요한 경우 프로젝트 하위의 dump.py 를 이용해야 합니다.
* 필수적으로 설치 필요한 Python library 는 pip 를 이용해 설치하기 바랍니다. 

## 말뭉치 종류
* 위키뉴스
  * https://ko.wikinews.org/wiki/
  * 라이선스
    * 크리에이티브 커먼즈 저작자표시 2.5 라이선스(CC-BY)
    * https://creativecommons.org/licenses/by/2.5/deed.ko
  * 웹에서 수집하는 소스코드는 wikinews 디렉토리 밑에 존재합니다.
  * 수집결과는 boddari/wikinews.csv 로 저장됩니다.

* book_review01
  * https://www.nanet.go.kr/datasearch/commant/selectWeekCommantList.do
  * 국회도서관 책 서평
  * 라이선스
    * 크리에이티브 커먼즈 저작자표시 라이선스(CC-BY)
    * 일부 다른 라이선스가 있어서 해당 부분은 제외함
    * 수집결과는 boddari/book_review01.csv 로 저장됩니다.

* airbnb_review
  * http://insideairbnb.com/get-the-data/
  * airbnb 공개된 리뷰 중에 한국어 리뷰가 존재함. 해당 리뷰만 뽑은 데이터
  * 해당 리뷰에는 평점 정보는 없음
  * 라이선스
    * 크리에이티브 커먼즈 저작자표시 라이선스(CC-BY)

* encyclopedia01
  * https://ko.wikisource.org/wiki/%EA%B8%80%EB%A1%9C%EB%B2%8C_%EC%84%B8%EA%B3%84_%EB%8C%80%EB%B0%B1%EA%B3%BC%EC%82%AC%EC%A0%84
  * 다음 커뮤니케이션(현 카카오)에서 기증한 백과사전
  * 라이선스
    * GFDL과 CC-BY-SA 3.0
  * 모든 내용이 존재하는 것이 아니라서 내용 중 일부 내용만을 csv 파일로 만들었음

* policy_news
  * 문화체육관광부_정책브리핑_정책뉴스
  * https://www.data.go.kr/data/15092236/fileData.do 에서 다운로드 가능
  * [대한민국 정책브리핑 사이트](korea.kr)에서 기사내용을 볼 수 있음
    * https://www.korea.kr/news/policyNewsView.do?newsId=(id값) 형태로 기사하나하나 접속 가능함
  * 라이선스
    * data.go.kr 에서는 "이용허락범위 제한 없음" 으로 나오는데 [대한민국 정책브리핑 사이트](korea.kr)에서 실제 기사에 접속하다보면 라이선스가 다르게 표시되어 있음. 그래서 "유형1"(출처표시)에 대해서만 취합했음

* press_release
  * 문화체육관광부_정책브리핑_보도자료
  * https://www.data.go.kr/data/15092245/fileData.do 에서 다운로드 가능
  * [대한민국 정책브리핑 사이트](korea.kr)에서 기사내용을 볼 수 있음
    * https://www.korea.kr/news/pressReleaseView.do?newsId=(id값) 형태로 기사하나하나 접속 가능함
  * 라이선스
    * data.go.kr 에서는 "이용허락범위 제한 없음" 으로 나오는데 [대한민국 정책브리핑 사이트](korea.kr)에서 실제 기사에 접속하다보면 라이선스가 다르게 표시되어 있음. 그래서 "유형1"(출처표시)에 대해서만 취합했음

* fairytale
  * Andersen 단편선 번역
    * [공유마당](https://gongu.copyright.or.kr/)
    * 미운 아기 오리
      * fairytale01.txt
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13287194&menuNo=200019
      * 원작: 안데르센, 번역 : [김선희](https://blog.naver.com/thinkwalden)
    * 성냥팔이 소녀
      * fairytale02.txt
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13287193&menuNo=200019
      * 원작: 안데르센, 번역 : [김선희](https://blog.naver.com/thinkwalden)
    * 눈의 여왕
      * fairytale03.txt
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13287190&menuNo=200019
      * 원작: 안데르센, 번역 : [김선희](https://blog.naver.com/thinkwalden)
    * 엄지 공주
      * fairytale04.txt
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13287191&menuNo=200019
      * 원작: 안데르센, 번역 : [김선희](https://blog.naver.com/thinkwalden)
    * 인어 공주
      * fairytale05.txt
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13287192&menuNo=200019
      * 원작: 안데르센, 번역 : [김선희](https://blog.naver.com/thinkwalden)
    * 라이선스
      * 기증저작물 자유이용
  * 방정환 단편소설
    * 라이선스
      * 저작권 만료
    *  이상한 샘물
      * fairytale06.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%EC%9D%B4%EC%83%81%ED%95%9C_%EC%83%98%EB%AC%BC
    * 나비의 꿈
      * fairytale07.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%EB%82%98%EB%B9%84%EC%9D%98_%EA%BF%88
    * 금도끼
      * fairytale08.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%EA%B8%88%EB%8F%84%EB%81%BC
    * 4월 그믐날 밤
      * fairytale09.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/4%EC%9B%94_%EA%B7%B8%EB%AF%90%EB%82%A0_%EB%B0%A4
    * 시골쥐 서울 구경
      * fairytale10.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%EC%8B%9C%EA%B3%A8%EC%A5%90_%EC%84%9C%EC%9A%B8_%EA%B5%AC%EA%B2%BD
    * 욕심쟁이 땅차지
      * fairytale11.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%EC%9A%95%EC%8B%AC%EC%9F%81%EC%9D%B4_%EB%95%85%EC%B0%A8%EC%A7%80
    * 호랑이 형님
      * fairytale12.txt
      * 저자: 방정환
      * https://ko.wikisource.org/wiki/%ED%98%B8%EB%9E%91%EC%9D%B4_%ED%98%95%EB%8B%98
    * 황금 거위
      * fairytale13.txt
      * 저자: 방정환
      * https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=9029668&menuNo=200019
