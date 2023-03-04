## airbnb_review
 * http://insideairbnb.com/get-the-data/
 * airbnb 공개된 리뷰 중에 한국어 리뷰가 존재함. 해당 리뷰만 뽑은 데이터
 * 해당 리뷰에는 평점 정보는 없음
 * 라이선스
    * 크리에이티브 커먼즈 저작자표시 라이선스(CC-BY)

## 사용법
 * 국가별 review 파일을 다운받기
   * airbnb_review/in 폴더에 압축된 리뷰 파일인 다운로드 됩니다. 
   * 현재(2023-02-26)총 사이즈가 4~5GB 입니다.
```
python ./airbnb_review/scrap.py
```
 * csv 파일 만들기
```
python  ./airbnb_review/dump.py
```
