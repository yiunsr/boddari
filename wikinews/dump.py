import sqlite3
import os
import csv
from pathlib import Path

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")

def get_infos():
    conn = sqlite3.connect(SQLITE_FILE)
    cur = conn.cursor()
    sql = """select DISTINCT  title, body, content_date, url from scrap s
        where s.title is not null and s.title != '' and length(s.body) >30
    order by content_date asc, id asc
    """
    cur.execute(sql)
    rows = cur.fetchall()
    infos =[]
    for row in rows:
        item = {}
        item["제목"] = row[0]
        item["내용"] = row[1]
        item["작성일"] = row[2]
        item["출처"] = row[3]
        infos.append(item)
    return infos

def write_csv(infos):
    file_path = os.path.join(DIR_PATH, "csv", PROJECT_NAME + ".csv")
    csv_file = open(file_path,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['작성일', '출처', '제목', '내용']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()

    for info in infos:
        csv_write.writerow(info)
    csv_file.close()

def write_txt(infos):
    file_path = os.path.join(DIR_PATH, "txt", PROJECT_NAME + ".txt")
    txt_file = open(file_path,'w', newline='', encoding="UTF-8")
    for info in infos:
        title = info["제목"]
        body = info["내용"]
        txt_file.write(title + "\n")
        txt_file.write(body + "\n")
        txt_file.write("\n")
    txt_file.close()

def main():
    csv_folder = os.path.join(DIR_PATH, "csv")
    Path(csv_folder).mkdir(parents=True, exist_ok=True)

    txt_folder = os.path.join(DIR_PATH, "txt")
    Path(txt_folder).mkdir(parents=True, exist_ok=True)

    infos = get_infos()
    write_csv(infos)
    write_txt(infos)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
