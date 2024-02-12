import sqlite3
import traceback
from datetime import datetime
import requests
import os
import csv
from urllib import parse
from bs4 import BeautifulSoup

BASE_URL = "https://ko.wikisource.org/"
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)
IN_CSV = os.path.join(DIR_PATH, "base_url.csv")
OUT_CSV = os.path.join(DIR_PATH, "in_raw.csv")

def read_csv():
    in_csv_file = open(IN_CSV, 'r', encoding="UTF-8")
    url_infos = []
    line = in_csv_file.readline()
    line = line.strip()
    chapter, url = line.split(",")
    for line in in_csv_file:
        line = line.strip()
        chapter, url = line.split(",")
        item = dict(chapter=chapter, url=url)
        url_infos.append(item)
    return url_infos

def read_page(chapter, url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    page_info = {}
    tags = soup.select(".mw-parser-output dl dd a")
    url_infos = []
    for tag in tags:
        title = tag.text
        url = BASE_URL + tag.get("href")
        categorys = tag.get("title")
        depth1, depth2, depth3 = split_category(categorys)
        item = dict(chapter=chapter, 
            depth1=depth1, depth2=depth2, depth3=depth3,
            title=title, url=url)
        url_infos.append(item)
    return url_infos

def split_category(categorys):
    category_list = categorys.split("/")
    depth1 = ""
    depth2 = ""
    depth3 = ""
    if len(category_list) == 5:
        depth1, depth2, depth3 = category_list[2:]
    elif len(category_list) == 4:
        depth1, depth2 = category_list[2:]
    elif len(category_list) == 3:
        depth1, = category_list[2:]
    return depth1, depth2, depth3

def write_csv(url_infos):
    csv_file = open(OUT_CSV,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['chapter', 'depth1', 'depth2', 'depth3', 'title', 'url']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()
    for info in url_infos:
        csv_write.writerow(info)
    csv_file.close()


def main():
    url_infos = read_csv()
    total_sub_url_infos = []
    for url_info in url_infos:
        url = url_info["url"]
        chapter = url_info["chapter"]
        sub_url_infos = read_page(chapter, url)
        total_sub_url_infos.extend(sub_url_infos)
    write_csv(total_sub_url_infos)

if __name__ == "__main__":
    print("======== scrap start ========")
    main()
    print("======== scrap end ========")