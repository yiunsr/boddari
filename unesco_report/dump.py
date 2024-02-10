import glob
import os
import csv
import chardet


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "in_txt/")
PROJECT_NAME = os.path.basename(DIR_PATH)
WRITE_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".txt")

def read_file(file_path):
    with open(file_path, 'rb') as txt_file:
        result = chardet.detect(txt_file.read(200))
    encoding = result["encoding"]
    if encoding == "EUC-KR":
        encoding = "CP949"

    with open(file_path, encoding=encoding) as txt_file:
        title = next(txt_file)
        title = title.strip()
        body = ""
        for line in txt_file:
            line = line.strip()
            body = body + line + "\n"
    return title, body

def read_files():
    in_files = glob.glob(IN_PATH  + '*.txt')
    in_files = sorted(in_files)

    items = []
    for file_path in in_files:
        (title, body) = read_file(file_path)
        item = dict(title=title, body=body)
        items.append(item)
    return items


# def write_csv(infos):
#     csv_file = open(CSV_FILE,'w', newline='', encoding="UTF-8")
#     csv_write = csv.writer(csv_file)
#     fieldnames = ['title', 'body']
#     csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     csv_write.writeheader()
#     for info in infos:
#         csv_write.writerow(info)
#     csv_file.close()

def write_txt(infos):
    write_file = open(WRITE_FILE,'w', encoding="UTF-8")
    fieldnames = ['title', 'body']
    for info in infos:
        write_file.write(info['title'])
        write_file.write("\n")
        write_file.write(info['body'])
        write_file.write("\n\n")
    write_file.close()

def main():
    infos = read_files()
    write_txt(infos)

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
