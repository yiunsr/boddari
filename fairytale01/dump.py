import glob
import os
import csv
import chardet
from pathlib import Path

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "in/")
PROJECT_NAME = os.path.basename(DIR_PATH)

def read_file(file_path):
    with open(file_path, 'rb') as txt_file:
        result = chardet.detect(txt_file.read(200))
    encoding = result["encoding"]
    if encoding == "EUC-KR":
        encoding = "CP949"

    with open(file_path, encoding=encoding) as txt_file:
        title = next(txt_file)
        title = title.strip()
        writer = next(txt_file)
        writer = writer.strip()
        body = ""
        for line in txt_file:
            line = line.strip()
            body = body + line + "\n"
    return title, writer, body

def read_files():
    in_files = glob.glob(IN_PATH  + '*.txt')
    in_files = sorted(in_files)

    items = []
    for file_path in in_files:
        (title, writer, body) = read_file(file_path)
        item = dict(title=title, writer=writer, body=body)
        items.append(item)
    return items


def write_csv(infos):
    file_path = os.path.join(DIR_PATH, "csv", PROJECT_NAME + ".csv")
    csv_file = open(file_path,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['title', 'writer', 'body']
    csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_write.writeheader()
    for info in infos:
        csv_write.writerow(info)
    csv_file.close()

def write_txt(infos):
    file_path = os.path.join(DIR_PATH, "txt", PROJECT_NAME + ".txt")
    txt_file = open(file_path,'w', newline='', encoding="UTF-8")
    for info in infos:
        title = info["title"]
        body = info["body"]
        txt_file.write(title + "\n")
        txt_file.write(body + "\n")
        txt_file.write("\n")
    txt_file.close()

def main():
    csv_folder = os.path.join(DIR_PATH, "csv")
    Path(csv_folder).mkdir(parents=True, exist_ok=True)

    txt_folder = os.path.join(DIR_PATH, "txt")
    Path(txt_folder).mkdir(parents=True, exist_ok=True)

    infos = read_files()
    write_csv(infos)
    write_txt(infos)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
