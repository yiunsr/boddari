import sqlite3
import os
import csv
import io
import zipfile
from pathlib import Path

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIR_PATH)

SQLITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".db")
CSV_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".csv")

def get_infos():
    conn = sqlite3.connect(SQLITE_FILE)
    cur = conn.cursor()
    sql = """select DISTINCT  category, 
        depth1, depth2, depth3, title,
        body from scrap s
        where s.title is not null and s.title != '' and length(s.body) >30
    order by id asc
    """
    cur.execute(sql)
    rows = cur.fetchall()
    infos =[]
    for row in rows:
        item = {}
        item["카테고리"] = row[0]
        item["depth1"] = row[1]
        item["depth2"] = row[2]
        item["depth3"] = row[3]
        item["제목"] = row[4]
        item["내용"] = row[5]
        infos.append(item)
    return infos


def write_csv(total_infos, file_len):
    info_len = len(total_infos)
    split_size = int(info_len / file_len)
    start = 0
    for file_idx in range(file_len):
        if file_idx + 1 == file_len:
            infos = total_infos[start:]
        else:
            end = split_size * (file_idx + 1)
            infos = total_infos[start:end]
            start = end
        file_idx_str = str(file_idx + 1).zfill(2)
        zip_file_path = os.path.join(
            DIR_PATH, "csv", PROJECT_NAME + "." + file_idx_str + ".csv.zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_BZIP2) as zip_file:
            io_csv = io.StringIO()
            fieldnames = ['카테고리', 'depth1', 'depth2', 'depth3', '제목', '내용']
            csv_write = csv.DictWriter(io_csv, fieldnames=fieldnames)
            csv_write.writeheader()
            for info in infos:
                csv_write.writerow(info)
            zip_file.writestr(PROJECT_NAME + "." + file_idx_str + ".csv",
                              io_csv.getvalue())

def write_txt(total_infos, file_len):
    info_len = len(total_infos)
    split_size = int(info_len / file_len)
    start = 0
    for file_idx in range(file_len):
        if file_idx + 1 == file_len:
            infos = total_infos[start:]
        else:
            end = split_size * (file_idx + 1)
            infos = total_infos[start:end]
            start = end
        file_idx_str = str(file_idx + 1).zfill(2)
        zip_file_path = os.path.join(
            DIR_PATH, "txt", PROJECT_NAME + "." + file_idx_str + ".txt.zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_BZIP2) as zip_file:
            io_file = io.StringIO()
            for info in infos:
                io_file.write(info['제목'])
                io_file.write("\n")
                io_file.write(info['내용'])
                io_file.write("\n\n")
            zip_file.writestr(PROJECT_NAME + "." + file_idx_str + ".txt",
                              io_file.getvalue())

def main():
    csv_folder = os.path.join(DIR_PATH, "csv")
    Path(csv_folder).mkdir(parents=True, exist_ok=True)

    txt_folder = os.path.join(DIR_PATH, "txt")
    Path(txt_folder).mkdir(parents=True, exist_ok=True)

    infos = get_infos()
    write_csv(infos, 2)
    write_txt(infos, 2)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
