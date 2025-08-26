# 🔍 PDF Searcher API (with FastAPI)

## 📖 معرفی پروژه
جستجو در فایل‌های PDF همیشه یکی از نیازهای مهم در پروژه‌های تحقیقاتی، دانشگاهی و حتی سازمانی است.  
این پروژه یک **موتور جستجوی ساده و سریع برای فایل‌های PDF** است که با زبان **Python** و فریم‌ورک **FastAPI** پیاده‌سازی شده.  

### ✨ ویژگی‌ها و جذابیت‌ها
- استخراج متن از فایل‌های PDF و ذخیره آن در یک ایندکس جستجو.
- قابلیت جستجوی سریع در تمام PDFها با استفاده از [Whoosh](https://whoosh.readthedocs.io/en/latest/).
- رابط **API مدرن** با مستندات خودکار (Swagger و ReDoc).
- امکان گسترش آسان به سمت **رابط وب کاربرپسند** یا **اتصال به فرانت‌اند** (React/Vue/Angular).
- پایه‌ای برای توسعه پروژه‌های بزرگ‌تر مثل:
  - کتابخانه دیجیتال
  - سیستم‌های مدیریت اسناد (DMS)
  - موتورهای جستجوی داخلی سازمانی
  - ابزارهای پژوهشی دانشگاهی

---

## 🏗️ معماری پروژه
این پروژه از معماری ساده اما ماژولار استفاده می‌کند:

pdf_searcher/
│── pdfs/ # پوشه‌ای برای ذخیره فایل‌های PDF
│── indexdir/ # پوشه‌ی ایندکس (خودکار ساخته می‌شود)
│── app.py # کد اصلی FastAPI (API جستجو)
│── requirements.txt # لیست کتابخانه‌های موردنیاز
│── README.md # مستندات پروژه


### 📌 اجزای اصلی
1. **FastAPI** → پیاده‌سازی API و مدیریت درخواست‌ها.  
2. **Whoosh** → موتور جستجو برای ایندکس‌سازی و جستجوی متون.  
3. **PyPDF2** → استخراج متن از PDFها.  
4. **Uvicorn** → سرور ASGI برای اجرای FastAPI.  

---

## ⚙️ ابزارها و تکنولوژی‌ها
- **زبان برنامه‌نویسی**: Python 3.8+  
- **فریم‌ورک وب**: [FastAPI](https://fastapi.tiangolo.com/)  
- **موتور جستجو**: [Whoosh](https://whoosh.readthedocs.io/en/latest/)  
- **کتابخانه پردازش PDF**: [PyPDF2](https://pypi.org/project/PyPDF2/)  
- **وب‌سرور**: [Uvicorn](https://www.uvicorn.org/)  

---

## 🚀 نصب و اجرا

### 1. کلون یا دانلود پروژه
```bash
git clone https://github.com/oneasshkan/pdf-searcher.git
cd pdf-searcher
```

### 2. ساخت محیط مجازی (اختیاری ولی پیشنهاد می‌شود)
```bash
python -m venv venv
source venv/bin/activate   # در ویندوز: venv\Scripts\activate
```
### 3. نصب وابستگی ها
‍‍
pip install -r requirements.txt

### 4. اجرای سرور

```bash 
uvicorn app:app --reload
```
### 5. دسترسی به مستندات

مستندات Swagger → http://127.0.0.1:8000/docs
مستندات ReDoc → http://127.0.0.1:8000/redoc

### 6.برای جستجو 
http://127.0.0.1:8000/search?query= query text

عبارت مورد نظر را جایگزین query textکنید
مثلا
http://127.0.0.1:8000/search?query=security
