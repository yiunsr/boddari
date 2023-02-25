# boddari
* 한국어 문장 수집 프로젝트


## LICENSE
* 소스코드가 존재하는 경우 
  * Apache License
* 한국어문장 라이선스는 사용하는 말뭉치 자체 리소스에 따라 결정됩니다. 해당 리소스의 설명을 확인하세요.
  * cc 라이선스(크리에이티브 커먼즈 라이선스)
    * http://ccl.cckorea.org/about/
    * https://gongu.copyright.or.kr/gongu/main/contents.do?menuNo=200093
  * 공공누리 라이센스
    * https://www.data.go.kr/ugs/selectPortalPolicyView.do
    * https://www.kogl.or.kr/info/license.do

## 사용법
* 모든 폴더는 말뭉치 종류입니다. 
* 해당 말뭉치를 수집이 필요한 경우 해당 프로젝트 하위의 scrap.py 를 통해 수집할 수 있습니다.
  * in 폴더가 존재하는 경우 

## 말뭉치 종류
* 위키뉴스
  * https://ko.wikinews.org/wiki/
  * 라이선스
    * 크리에이티브 커먼즈 저작자표시 2.5 라이선스(CC-BY)
    * https://creativecommons.org/licenses/by/2.5/deed.ko
  * 웹에서 수집하는 소스코드는 wikinews 디렉토리 밑에 존재합니다.
  * 수집결과는 boddari/wikinews.csv 로 저장됩니다.

* 책서평
  * https://www.nanet.go.kr/datasearch/commant/selectWeekCommantList.do
  * 국회도서관 책 서평
  * 라이센스
    * 크리에이티브 커먼즈 저작자표시 라이선스(CC-BY)
    * 일부 다른 라이센스가 있어서 해당 부분은 제외함
    * 수집결과는 boddari/book_review01.csv 로 저장됩니다.

