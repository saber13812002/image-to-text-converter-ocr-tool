import pytesseract
import os
from PIL import Image

def convert_image_to_text(image_path):
    # مسیر نصب Tesseract و پوشه tessdata
    pytesseract_path = r"C:\Program Files\Tesseract-OCR"
    os.environ["TESSDATA_PREFIX"] = os.path.join(pytesseract_path, "tessdata")
    pytesseract.pytesseract.tesseract_cmd = os.path.join(pytesseract_path, "tesseract.exe")
    
    try:
        # باز کردن تصویر
        image = Image.open(image_path)
        
        # استخراج متن
        text = pytesseract.image_to_string(image, lang="eng")  # "fas" برای فارسی
        output_file = f"{os.path.splitext(image_path)[0]}.txt"
        
        # ذخیره متن در فایل متنی
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        
        print(f"متن استخراج‌شده در فایل ذخیره شد: {output_file}")
    except Exception as e:
        print(f"خطا در پردازش تصویر: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("لطفاً مسیر فایل تصویری را وارد کنید.")
    else:
        image_path = sys.argv[1]
        convert_image_to_text(image_path)
