import os
from fastapi import FastAPI, Query
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import PyPDF2
from typing import List

PDF_DIR = "pdfs"
INDEX_DIR = "indexdir"

app = FastAPI(title="PDF Searcher API", description="جستجوگر PDF با FastAPI", version="1.0")

# تعریف اسکیما
schema = Schema(title=ID(stored=True), content=TEXT)


def get_or_create_index():
    """اگر ایندکس وجود نداشت یا خراب بود، یه ایندکس جدید بساز"""
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)

    try:
        return index.open_dir(INDEX_DIR)
    except index.EmptyIndexError:
        return index.create_in(INDEX_DIR, schema)


def create_index():
    """ایندکس‌سازی فایل‌های PDF"""
    ix = get_or_create_index()
    writer = ix.writer()

    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            filepath = os.path.join(PDF_DIR, file)
            text = extract_text_from_pdf(filepath)
            writer.add_document(title=file, content=text)
            print(f"[+] Indexed: {file}")

    writer.commit()


def extract_text_from_pdf(filepath):
    """استخراج متن از PDF"""
    text = ""
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


@app.on_event("startup")
def startup_event():
    """وقتی سرور بالا میاد، ایندکس ساخته بشه"""
    print("[*] در حال ایندکس کردن PDF ها ...")
    create_index()


@app.get("/search", response_model=List[str])
def search(query: str = Query(..., description="عبارت جستجو")):
    """جستجو در متن PDF ها"""
    ix = get_or_create_index()
    parser = QueryParser("content", ix.schema)
    q = parser.parse(query)

    results_list = []
    with ix.searcher() as searcher:
        results = searcher.search(q)
        for r in results:
            results_list.append(r["title"])

    return results_list