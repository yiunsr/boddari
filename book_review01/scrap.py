import sqlite3
import traceback
import copy
from datetime import datetime
import requests
import os
from urllib import parse
from bs4 import BeautifulSoup

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")
BASE_URL_INFOS = [
    {
        # 금주의 서평
        "base_url": "https://www.nanet.go.kr/datasearch/commant/selectWeekCommantDetail.do?searchSeq=",
        "path": "selectWeekCommantDetail",
        "start": 282, "end": 2651,
    },
    {
        # 전문가 서평
        "base_url": "https://www.nanet.go.kr/datasearch/commant/selectHumanCommantDetail.do?searchSeq=",
        "path": "selectHumanCommantDetail",
        "start": 5, "end": 69,
    },
    {
        # 열린 서평
        "base_url": "https://www.nanet.go.kr/datasearch/commant/selectOpenCommantDetail.do?searchSeq=",
        "path": "selectOpenCommantDetail",
        "start": 5, "end": 55,
    },
]

_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS scrap(
    id integer primary key AUTOINCREMENT, 
   	url text unique NOT NULL,
    book_title text DEFAULT NULL,
    title text DEFAULT NULL,
	body text DEFAULT NULL,
    content_date DATE,
    update_dt INTEGER 
);
"""

class Scrap:
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_FILE)
        self.create_table()
        base_url_infos = []
        for baseinfo in BASE_URL_INFOS:
            new_baseinfo = copy.deepcopy(baseinfo)
            path = baseinfo["path"]
            start = baseinfo["start"]
            new_start = self.get_start(path, start)
            new_baseinfo["start"] = new_start
            base_url_infos.append(new_baseinfo)
        self.base_url_infos = base_url_infos
    
    def create_table(self):
        try:
            cur = self.conn.cursor()
            cur.execute(_CREATE_TABLE)
        except:
            print(traceback.format_exc())

    def get_start(self, path, start):
        cur = self.conn.cursor()
        sql = """select max(cast(substr(s.url, instr(s.url, '=') + 1 ) as integer))
            from scrap s where instr( s.url, :path) > 0
        """
        cur.execute(sql, {"path": path});
        row = cur.fetchone()
        return int(row[0] or start)

    def access_page(self, url):
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            page_info = {}
            page_info["title"] = soup.select(".box01")[0].text.strip()
            date_str = soup.select(".box01")[2].text.strip()
            date_str_idx = date_str.find("(")
            date_str = date_str[date_str_idx + 1:-1]
            book_title = soup.select(".bookInfo .bg03 .con")[1].text.strip()

            img_ele = soup.select(".list02 img")[0]
            ccl_img_src = img_ele.attrs.get("src")
            # CCL BY 이미지가 아니면 continue
            if "ccl01" not in ccl_img_src:
                return None
            body = soup.select(".bodyBox005 .txt01")[0].text.strip()
            page_info["date"] = date_str
            page_info["body"] = body
            page_info["book_title"] = book_title
            return page_info
        except:
            print(traceback.format_exc())

    def add_content(self, param_dict):
        cursor = self.conn.cursor()
        cursor.execute("BEGIN;");
        sql = """INSERT OR IGNORE INTO 
            scrap(url, book_title, title, body, 
                content_date, update_dt) 
            VALUES(:url, :book_title, :title, :body, 
                :date, strftime('%Y-%m-%d %H-%M-%S','now')
            );
        """
        cursor.execute(sql, param_dict)
        cursor.execute("COMMIT;");

    def do(self):
        for base_url_info in self.base_url_infos:
            base_url = base_url_info["base_url"]
            start = base_url_info["start"]
            end = base_url_info["end"]
            for index in range(start, end+1):
                url = base_url + str(index)
                page_info = self.access_page(url)
                if page_info is None:
                    continue
                page_info["url"] = url
                self.add_content(page_info)
    def close(self):
        self.conn.close()

def main():
    scrap = Scrap()
    scrap.do()
    scrap.close()

if __name__ == "__main__":
    print("======== scrap start ========")
    main()
    print("======== scrap end ========")