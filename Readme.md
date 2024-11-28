
# Image-to-Text Converter - OCR Tool

This project is a simple tool for extracting text from images using OCR (Optical Character Recognition). It is written in Python and works with Tesseract OCR.

---

## **Features**
- Fast and accurate text extraction from images
- Supports multiple languages (English and Persian)
- Adds a right-click context menu option in Windows for convenience
- Generates an executable file for Windows

---

## **Prerequisites**
1. Install Python (version 3.8 or newer)
2. Install Tesseract OCR:
   - Download from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
3. Install dependencies:
   ```bash
   pip install pytesseract pillow
   ```

---

## **Usage**
### **1. Run Directly with Python**
1. Run the script:
   ```bash
   python convert_to_txt.py "path_to_image_file"
   ```
2. The extracted text will be saved as a `.txt` file in the same directory as the image.

### **2. Build Executable (Optional)**
For easier usage, you can generate an executable file:
```bash
pyinstaller --onefile convert_to_txt.py
```
The executable file will be located in the `dist` folder.

### **3. Add to Windows Right-Click Menu**
1. Note the path to the executable file.
2. Add the following command to Windows Registry:
   ```
   "path_to_executable" "%1"
   ```

---

## **Releases**
Current Version: 1.0.0

---

## **License**
This project is licensed under the MIT License.
