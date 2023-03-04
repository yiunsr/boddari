import csv
import glob
import os
import io
import zipfile
from multiprocessing import Pool

csv.field_size_limit(2147483647)

NUM_PROCESS = 6
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "in/")
PROJECT_NAME = os.path.basename(DIR_PATH)
CSV_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".csv")

def read_file(filepath):
    rows = []
    print("read_file : "  + filepath)
    idx = 0
    with open(filepath, mode="r", encoding="CP949") as csv_file:
        csv_read = csv.DictReader(csv_file, delimiter = ',',quotechar='"')
        for row in csv_read:
            id_ = row["부처뉴스 뉴스 아이디"]
            section = row["부처뉴스 섹션 아이디"]
            date_str = row["부처뉴스 등록 일자"]
            date_str = date_str[:10]
            license_type =  row["공공저작물 유형"]
            if license_type != "유형1":
                continue
            title = row["부처뉴스 메인 제목"]
            body = row["부처뉴스 본문 내용"]
            if len(body) < 100:
                continue
            item = dict(id=id_, section=section, date=date_str,
                        title=title, body=body)
            rows.append(item)
    return rows

def read_files():
    in_files = glob.glob(IN_PATH  + '*.csv')
    in_files = sorted(in_files, key=os.path.getsize, reverse=True)
    
    with Pool(processes=NUM_PROCESS) as pool:
        items = pool.map(read_file, in_files)
    rows = []
    for item in items:
        rows.extend(item)
    return rows

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
            DIR_PATH, PROJECT_NAME + "." + file_idx_str + ".zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_BZIP2) as zip_file:
            io_csv = io.StringIO()
            fieldnames = ['id', 'date', 'section', 'title', 'body']
            csv_write = csv.DictWriter(io_csv, fieldnames=fieldnames)
            csv_write.writeheader()
            for info in infos:
                csv_write.writerow(info)
            zip_file.writestr(PROJECT_NAME + '.csv', io_csv.getvalue())

def main():
    infos = read_files()
    write_csv(infos, 10)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
