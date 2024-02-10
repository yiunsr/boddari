import glob
import os
import csv
from pypdf import PdfReader


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "in/")
PROJECT_NAME = os.path.basename(DIR_PATH)
CSV_FILE = os.path.join(DIR_PATH, PROJECT_NAME + ".csv")

def read_file(file_path):
    reader = PdfReader(file_path)
    for page in reader.pages:
        print(page.extract_text())
    

def read_files():
    in_files = glob.glob(IN_PATH  + '*.pdf')
    in_files = sorted(in_files)

    items = []
    for file_path in in_files:
        (title, writer, body) = read_file(file_path)
        item = dict(title=title, writer=writer, body=body)
        items.append(item)
    return items


def write_csv(infos):
    csv_file = open(CSV_FILE,'w', newline='', encoding="UTF-8")
    csv_write = csv.writer(csv_file)
    fieldnames = ['title', 'writer', 'body']
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
