import csv
import gzip
import glob
import os
from multiprocessing import Pool

NUM_PROCESS = 6
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "in/")
PROJECT_NAME = os.path.basename(DIR_PATH)
CSV_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".csv")

def check_korean(line):
    char_count = 0
    # 속도를 위해 앞의 30자만 읽는다.
    for char in line[:30]:
        # 가~힣
        if 0xAC00 <= ord(char) <= 0xD7A3:
            char_count +=1
    # 읽은 글자 중 한국어가 10자 이상일 때만 한국어로 생각하자.
    if char_count > 9:
        return True
    return False

def read_file(filepath):
    rows = []
    print("read_file : "  + filepath)
    with gzip.open(filepath, mode="rt", encoding="UTF-8") as csv_file:
        filename = os.path.basename(filepath)
        city = filename.replace("_reviews.csv.gz", "")
        csv_read = csv.reader(csv_file, delimiter = ',',quotechar='"')
        for row in csv_read:
            if check_korean(row[5]) is False:
                continue
            comment=row[5].replace("<br/>", "")
            item = dict(city=city, date=row[2], comment=comment)
            rows.append(item)
    return rows

def read_files():
    gz_files = glob.glob(IN_PATH  + '*.csv.gz')
    gz_files = sorted(gz_files, key=os.path.getsize, reverse=True)
    
    with Pool(processes=NUM_PROCESS) as pool:
        items = pool.map(read_file, gz_files)
    rows = []
    for item in items:
        rows.extend(item)
    return rows

def write_csv(infos):
    csv_file = open(CSV_FILE,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['city', 'date', 'comment']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()
    for info in infos:
        csv_write.writerow(info)
    csv_file.close()


def main():
    infos = read_files()
    write_csv(infos)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
