import sqlite3
import traceback
from datetime import datetime
import requests
import os
import csv
from urllib import parse
from bs4 import BeautifulSoup


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)
IN_CSV = os.path.join(DIR_PATH, "in.csv")

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")

_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS scrap(
    id integer primary key AUTOINCREMENT, 
   	url text unique NOT NULL ,
    category text DEFAULT NULL,
    depth1 text DEFAULT NULL,
    depth2 text DEFAULT NULL,
    depth3 text DEFAULT NULL,
    title text DEFAULT NULL,
	body text DEFAULT NULL,
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
        cur.execute("select url from scrap")
        rows = cur.fetchall()
        scrapped_urls = []
        for row in rows:
            scrapped_urls.append(row[0])

        url_infos = []
        with open(IN_CSV, encoding="UTF-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                chapter = row[0]
                depth1 = row[1]
                depth2 = row[2]
                depth3 = row[3]
                title = row[4]
                url = row[5]
                if url in scrapped_urls:
                    continue
                url_infos.append(dict(category=chapter,
                    depth1=depth1, depth2=depth2, depth3=depth3,
                    title=title, url=url))
        return url_infos

    def access_page(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        page_info = {}
        body = self.body_from_soup(soup)
        page_info["body"] = body
        return page_info

    def body_from_soup(self, soup):
        tags = soup.select(".mw-parser-output p, .mw-headline")
        body = ""
        for tag in tags:
            body += tag.text.strip()
            body = body + "\n"
        return body

    def add_content(self, url, category, depth1, depth2, depth3, title, body):
        cursor = self.conn.cursor()
        cursor.execute("BEGIN;");
        param_dict = {"url": url, "category": category,
            "depth1": depth1, "depth2": depth2, "depth3": depth3,
            "title": title, "body": body,}
        sql = """INSERT OR IGNORE INTO 
            scrap(url, category, title, depth1, depth2, depth3, body, update_dt) 
            VALUES(:url,  :category, :title, 
                :depth1, :depth2, :depth3, :body, 
                strftime('%Y-%m-%d %H-%M-%S','now')
            );
        """
        cursor.execute(sql, param_dict)
        cursor.execute("COMMIT;");

    def do(self):
        url_infos = self.get_urls()
        for url_info in url_infos:
            category = url_info["category"]
            depth1 = url_info["depth1"]
            depth2 = url_info["depth2"]
            depth3 = url_info["depth3"]
            title = url_info["title"]
            url = url_info["url"]
            page_info = self.access_page(url)
            body = page_info["body"]
            if body is None:
                continue
            self.add_content(url, category, depth1, depth2, depth3, title, body)

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