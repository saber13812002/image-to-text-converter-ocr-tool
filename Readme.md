
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


## **Adding to Windows Right-Click Context Menu**
To make the tool easier to use, you can add an option to the Windows right-click context menu. This allows you to execute the tool directly from the menu for files or folders.

---

### **Registry Settings for Files**
1. Create a new text file and name it `add_to_context_menu_files.reg`.
2. Copy the following content into the file:
   ```reg
   Windows Registry Editor Version 5.00

   [HKEY_CLASSES_ROOT\*\shell\ConvertToText]
   @="Convert to Text"

   [HKEY_CLASSES_ROOT\*\shell\ConvertToText\command]
   @="\"E:\\saberprojects\\kasra\\image-to-text-windows-python\\dist\\convert_to_txt.exe\" \"%1\""
   ```
3. Replace `E:\\saberprojects\\kasra\\image-to-text-windows-python\\dist\\convert_to_txt.exe` with the path to your executable file.
4. Save the file.
5. Right-click on the file and select **Merge**.

---

### **Registry Settings for Folders**
1. Create another text file and name it `add_to_context_menu_folders.reg`.
2. Copy the following content into the file:
   ```reg
   Windows Registry Editor Version 5.00

   [HKEY_CLASSES_ROOT\Directory\shell\ConvertToText]
   @="Convert to Text"

   [HKEY_CLASSES_ROOT\Directory\shell\ConvertToText\command]
   @="\"E:\\saberprojects\\kasra\\image-to-text-windows-python\\dist\\convert_to_txt.exe\" \"%1\""
   ```
3. Replace the executable path with your own.
4. Save and run the file.

---

### **Important Notes**
- Make sure the path to the executable (`convert_to_txt.exe`) is correct.
- To remove the options, delete the following registry keys:
  - For files: `HKEY_CLASSES_ROOT\*\shell\ConvertToText`
  - For folders: `HKEY_CLASSES_ROOT\Directory\shell\ConvertToText`

