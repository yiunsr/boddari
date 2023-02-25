import sqlite3
import traceback
from datetime import datetime
import requests
import os
from urllib import parse
from bs4 import BeautifulSoup

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")
BASE_URL = "https://ko.wikinews.org/wiki/"
START_URLS = [
    "https://ko.wikinews.org/wiki/%EC%9C%84%ED%82%A4%EB%89%B4%EC%8A%A4:%EB%8C%80%EB%AC%B8"
]

_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS scrap(
    id integer primary key AUTOINCREMENT, 
   	url text unique NOT NULL ,
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
    
    def create_table(self):
        try:
            cur = self.conn.cursor()
            cur.execute(_CREATE_TABLE)
        except:
            print(traceback.format_exc())
    
    def get_urls(self):
        cur = self.conn.cursor()
        cur.execute("select url from scrap where update_dt is null")
        rows = cur.fetchall()
        if len(rows) == 0:
            return START_URLS
        urls = []
        for row in rows:
            urls.append(row[0])
        return urls

    def access_page(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        page_info = {}
        page_info["url"] = self.url_from_soup(url, soup)
        (title, date_str, body) = self.body_from_soup(soup)
        page_info["title"] = title
        page_info["date"] = date_str
        page_info["body"] = body
        return page_info
    
    def url_from_soup(self, baseurl, soup):
        link_tags = soup.select("#mw-content-text a")
        urls = []
        for tag in link_tags:
            href = tag.attrs.get("href")
            if href is None:
                continue
            href = parse.urljoin(baseurl, href)
            if href.startswith("https://ko.wikinews.org/wiki/") is False:
                continue
            if '분류:' not in parse.unquote(href) and\
                    ":" in parse.urlparse(href).path:
                continue
            pos = href.find("?")
            if pos > 0:
                href = href[:pos]
            pos = href.find("#")
            if pos > 0:
                href = href[:pos]
            urls.append(href)
        return urls

    def body_from_soup(self, soup):
        title = soup.select("#firstHeading")[0].get_text()
        tags = soup.select("#mw-content-text .mw-parser-output p")
        body = ""
        for tag in tags:
            body += tag.get_text()
            body = body.split("\n공유하기")[0]
        if body.startswith("【") is False:
            return "", "", ""
        date_pos = body.find("】")
        date_str = body[1:date_pos]
        body = body[date_pos+1:]
        body = body.strip()
        date_dt = datetime.strptime(date_str, "%Y년 %m월 %d일")
        date_str2 = datetime.strftime(date_dt,'%Y-%m-%d')
        return title, date_str2, body

    def add_urls(self, urls):
        urls = list(set(urls))
        params = []
        for url in urls:
            params.append((url,))
        cursor = self.conn.cursor()
        cursor.execute("BEGIN;");
        cursor.executemany("""INSERT OR IGNORE INTO scrap(url) VALUES(?);""", params);
        cursor.execute("COMMIT;");

    def add_content(self, url, title, date_str, body):
        cursor = self.conn.cursor()
        param_dict = {"url": url, "title": title,
            "body": body, "date": date_str}
        cursor.execute("BEGIN;");
        sql = """UPDATE scrap SET title = :title, content_date = :date, 
            body = :body, update_dt = strftime('%Y-%m-%d %H-%M-%S','now') 
            WHERE url = :url"""
        cursor.execute(sql, param_dict)
        cursor.execute("COMMIT;");

    def do(self):
        urls = self.get_urls()
        for url in urls:
            page_info = self.access_page(url)
            new_urls = page_info["url"]
            self.add_urls(new_urls)
            title = page_info["title"]
            date_str = page_info["date"]
            body = page_info["body"]
            if body is None:
                continue
            self.add_content(url, title, date_str, body)

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