import urllib
import sqlite3
import traceback
import copy
import glob
from multiprocessing import cpu_count
from multiprocessing import Pool

from datetime import datetime
import requests
import os
from bs4 import BeautifulSoup

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)
IN_PATH = os.path.join(DIR_PATH, "in/")

DATA_LIST_PAGE = "http://insideairbnb.com/get-the-data/"

def download_from_url(arg):
    filename, url = arg
    print("download : " + filename)
    file_full_path = os.path.join(IN_PATH, filename)

    req = requests.get(url, stream=True)
    if req.status_code == requests.codes.ok:
        with open(file_full_path, 'wb') as gz_file:
            for data in req:
                gz_file.write(data)


class Scrap:
    def __init__(self):
        self.get_file_list()
        self.get_data_list()

    def get_file_list(self):
        gz_files = glob.glob(IN_PATH  + '*.csv.gz')
        file_dict = {}
        for gz_file in gz_files:
            filename = os.path.basename(gz_file)
            file_dict[filename] = ""
        self.file_dict = file_dict

    def get_data_list(self):
        res = requests.get(DATA_LIST_PAGE)
        soup = BeautifulSoup(res.text, "html.parser")
        table_eles = soup.select(".table")
        download_dict = {}
        idx = -1
        data_eles = soup.select("h4")
        for table_ele in table_eles:
            idx += 1
            date_str = data_eles[idx].text
            date_str = date_str.split("(")[0]
            # date_str = table_ele.find_all("td")[0].text
            date_obj = datetime.strptime(date_str, '%d %B, %Y ')
            date_str = datetime.strftime(date_obj, "%Y-%m-%d")
            city = table_ele.find_all("td")[0].text
            href = table_ele.find_all("a")[2].attrs.get("href")
            filename = city + "--" + date_str + "--reviews.csv.gz"
            if filename in self.file_dict:
                continue
            download_dict[filename] = href
        self.download_dict = download_dict

    def do(self):
        cpus = cpu_count()
        # cpus = 1
        with Pool(processes=cpus) as pool:
            pool.map(download_from_url, self.download_dict.items())

def main():
    scrap = Scrap()
    scrap.do()

if __name__ == "__main__":
    print("======== scrap start ========")
    main()
    print("======== scrap end ========")