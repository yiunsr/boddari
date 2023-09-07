# 보따리 프로젝트
* 한국어 문장 수집 프로젝트
* 한국어 말뭉치 프로젝트들이 많이 존재하지만 회원가입을 해야하고 약정서를 제출해야하는 경우가 있다.
 이러한 제약없이 문제없는 글들을 수집하는 프로젝트입니다. 
* 가능한 public domain, 지적재산권이 만료된 저작물, CCL 라이선스 데이터(가능한 CC-BY, CC-BY-SA),  공공누리 라이선스(가능한 제 1유형 : 출처표시), 기증 저작물을 수집한다.


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
* book_review02
  * http://www.acornpub.co.kr/blog
  * 에이콘출판사 블로그
  * 블로그 내용 중 책서평만 정리함
  * 라이선스
    *  크리에이티브 커먼즈 코리아 저작자표시 2.0 대한민국 라이센스(CC BY 2.0 KR)

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

* fairytale01
  * 상세 출처는 [README.md](/fairytale01/README.md)를 참고 하세요.
  * Andersen 단편선 번역
    * 라이선스
      * 기증저작물 자유이용
  * 방정환 단편소설
    * 라이선스
      * 저작권 만료
  * [두루책방](http://xn--hu1b40go5ck8x.com/)
    * 라이선스
      * CC BY 4.0

* unesco
  * 유네스크 출판물 또는 자료
  * 라이선스
    * CC-BY-SA 3.0 IGO
      * IGO는 정부간 국제기구(International organization)를 의미함
  * 세계시민교육: 학습 주제 및 학습 목표
    * unesco-0001.txt
    * https://www.gcedclearinghouse.org/sites/default/files/resources/150020kor.pdf
  * 함께 그려보는 우리의 미래 : 교육을 위한 새로운 사회계약
    * unesco-0002.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000381212
  * 다시 생각하는 교육: 교육은 전지구적 공동재를 향해 가고 있는가?
    * unesco-0003.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000374901
  * 문화 | 2030 지표
    * unesco-0004.txt
    * https://www.unesco.or.kr/assets/data/report/kbdZbkXjWpc6t1HdNB5orL9Xox4oOO_1640158506_2.pdf
  * 저널리즘, 가짜뉴스 & 허위정보 
    * unesco-0005.txt
	  * https://www.unesco.or.kr/assets/data/report/AaBXrdz4A1nLK30vxcsNH0OHWwI1fn_1604555429_2.pdf
  * 2020년 UN 세계물개발보고서: 물과 기후변화, 요약보고서
    * unesco-0006.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000372882_kor
  * 2021년 세계물개발보고서: 물의 가치 평가: 요약보고서
    * unesco-0007.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000375750_kor
  * 2022년 유엔 세계물개발 보고서: 지하수 보이지 않는 것을 보이게 요약보고서
    * unesco-0008.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000380726_kor
  * 문화정책의 (재)구성 : 전지구적 공공재로서 문화를 바라보다
    * unesco-0009.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000380475_kor
  * 문화정책의 재구성:지속가능성한 성장을 위한 10년 동안의 문화다양성 표현 증진
    * unesco-0010.txt
	  * https://en.unesco.org/creativity/sites/creativity/files/gmr_summary_korean.pdf
  * 저널리즘과 미디어·정보 리터러시
    * unesco-0011.txt
	  * https://www.unesco.or.kr/assets/data/report/Z0mxZ1iXuUW6H7k2lu3zw87FgC6GbQ_1640257390_2.pdf
  * 유네스코 과학보고서: 보다 똑똑한 발전을 위한 시간과의 경주 – 요약본 한국어판
    * unesco-0012.txt
	  * https://www.unesco.or.kr/assets/data/report/bhP8oIGvWPWY6WfPIiz8aRGMIWZ4Or_1636445084_2.pdf
  * 신중한 대화:여성폭력 담론을 위한 미디어 활용 핸드북
    * unesco-0013.txt
    * https://unesdoc.unesco.org/ark:/48223/pf0000380007
  * 인공지능과 교육 - 정책입안자를 위한 지침
    * unesco-0014.txt
	  * https://www.unesco.or.kr/assets/data/report/UQ2Cd7pByyvIsMqVIsjyoVtPou9Z3i_1638430937_2.pdf
  * 평생학습 문화 수용하기
    * unesco-0015.txt
    * https://www.gcedclearinghouse.org/sites/default/files/resources/200503kor.pdf
