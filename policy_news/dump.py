import csv
import glob
import os
import io
import zipfile
from pathlib import Path
from multiprocessing import Pool

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
            id_ = row["정책정보 뉴스 아이디"]
            section = row["정책정보 섹션 아이디"]
            date_str = row["정책정보 등록 일자"]
            date_str = date_str[:10]
            license_type =  row["공공저작물 유형"]
            if license_type != "유형1":
                continue
            title = row["정책정보 메인 제목"].strip()
            body = row["정책정보 본문 내용"].strip()
            if len(body) < 100:
                continue
            item = {"id":id_, "section": section, "작성일": date_str,
                        "제목": title, "내용": body}
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
            DIR_PATH, "csv", PROJECT_NAME + "." + file_idx_str + ".csv.zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_BZIP2) as zip_file:
            io_csv = io.StringIO()
            fieldnames = ['id', '작성일', 'section', '제목', '내용']
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

    infos = read_files()
    write_csv(infos, 4)
    write_txt(infos, 4)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
