import os  # 處理檔案路徑
from PyPDF2 import PdfReader, PdfWriter  # PDF 讀寫工具

# 固定輸出資料夾
OUTPUT_DIR = r"C:\Users\apuser\Desktop\PDF處理\output"

def split_pdf_pages(input_pdf_path, page_input):
    """
    按照使用者輸入的頁碼範圍拆出 PDF
    :param input_pdf_path: PDF 檔案路徑
    :param page_input: 頁碼字串，例如 "2-5" 或 "3"
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # 確保輸出資料夾存在
    reader = PdfReader(input_pdf_path)  # 讀取 PDF
    total_pages = len(reader.pages)  # 總頁數

    # 解析使用者輸入的頁碼範圍
    if "-" in page_input:
        start, end = map(int, page_input.split("-"))  # 拆解成起始與結束頁
    else:
        start = end = int(page_input)  # 單一頁情況

    # 檢查頁碼合法性
    if start < 1 or end > total_pages or start > end:
        print("頁碼範圍錯誤！請確認輸入。")
        return

    # 建立 PDF 寫入器
    writer = PdfWriter()
    for i in range(start - 1, end):
        writer.add_page(reader.pages[i])  # 加入指定頁

    # 設定輸出檔名
    if start == end:
        output_path = os.path.join(OUTPUT_DIR, f"page_{start}.pdf")
    else:
        output_path = os.path.join(OUTPUT_DIR, f"pages_{start}_to_{end}.pdf")

    # 寫出 PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"已輸出檔案：{output_path}")

def merge_pdfs(pdf1_path, pdf2_path):
    """
    合併兩個 PDF 檔案
    :param pdf1_path: 第一個 PDF 路徑
    :param pdf2_path: 第二個 PDF 路徑
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # 確保輸出資料夾存在
    merger = PdfWriter()

    # 加入第一個 PDF
    reader1 = PdfReader(pdf1_path)
    for page in reader1.pages:
        merger.add_page(page)

    # 加入第二個 PDF
    reader2 = PdfReader(pdf2_path)
    for page in reader2.pages:
        merger.add_page(page)

    # 輸出合併檔案
    output_path = os.path.join(OUTPUT_DIR, "merged.pdf")
    with open(output_path, "wb") as output_file:
        merger.write(output_file)

    print(f"已輸出合併檔案：{output_path}")

if __name__ == "__main__":
    print("=== PDF 處理工具 ===")
    print("1. 拆分 PDF")
    print("2. 合併 PDF")
    choice = input("請選擇功能（1 或 2）：").strip()

    if choice == "1":
        input_pdf = input("請輸入 PDF 檔案路徑：").strip()
        page_range = input("請輸入要拆分的頁碼（例如 2-5 或 3）：").strip()
        split_pdf_pages(input_pdf, page_range)
    elif choice == "2":
        pdf1 = input("請輸入第一個 PDF 檔案路徑：").strip()
        pdf2 = input("請輸入第二個 PDF 檔案路徑：").strip()
        merge_pdfs(pdf1, pdf2)
    else:
        print("輸入錯誤，請重新執行。")
