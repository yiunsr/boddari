import glob
import os
from io import StringIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_pages
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text
from pdfminer.layout import LTTextContainer

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IN_PATH = os.path.join(DIR_PATH, "unesco_report/in/")

def is_body(page_layout, element):
    margin_percent = 0.08
    margin_y = page_layout.height * margin_percent
    margin_top_end = page_layout.y0 + margin_y
    margin_bottom_start = page_layout.y1 - margin_y
    if element.y0 < margin_top_end:  # 머리말
        return False
    if element.y1 > margin_bottom_start:  # 꼬리말
        return False
    return True



def read_file(file_path):
    # output_string = StringIO()
    # with open(file_path, 'rb') as fp:
    #     tt = extract_text(fp)
    #     pass
    page_dict = {}
    for page_layout in extract_pages(file_path):
        page_id = page_layout.pageid
        page_dict[page_id] = {}
        out_text = ""
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if is_body(page_layout, element) is False:
                    continue
                out_text += element.get_text() + "\n"
        page_dict[page_id]["text"] = out_text
    return page_dict


def read_files():
    in_files = glob.glob(IN_PATH  + '*.pdf')
    in_files = sorted(in_files)

    items = []
    for file_path in in_files:
        page_info = read_file(file_path)
        items.append(page_info)
    return items

def main():
    infos = read_files()

if __name__ == "__main__":
    print("======== dump start ========")
    main()
    print("======== dump end ========")
