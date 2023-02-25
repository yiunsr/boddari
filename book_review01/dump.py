import sqlite3
import os
import csv

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")
CSV_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".csv")

def get_infos():
    conn = sqlite3.connect(SQLITE_FILE)
    cur = conn.cursor()
    sql = """select DISTINCT book_title, title, body, content_date from scrap s
        where s.title is not null and s.title != '' and length(s.body) >30
    order by content_date asc, id asc
    """
    cur.execute(sql)
    rows = cur.fetchall()
    infos =[]
    for row in rows:
        item = {}
        item["책제목"] = row[0]
        item["제목"] = row[1]
        item["내용"] = row[2]
        item["작성일"] = row[3]
        infos.append(item)
    return infos

def write_csv(infos):
    csv_file = open(CSV_FILE,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['작성일', '책제목', '제목', '내용']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()
    for info in infos:
        csv_write.writerow(info)
    csv_file.close()

def main():
    infos = get_infos()
    write_csv(infos)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
