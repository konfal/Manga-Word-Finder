import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

volumes_input = input("Enter volumes (example: volume 45,volume 46): ")
SEARCH_WORD = input("Enter word to search: ").lower()

BASE_FOLDER = r"C:\naruto manga"

volumes = [v.strip() for v in volumes_input.split(",")]

for volume in volumes:
    folder = os.path.join(BASE_FOLDER, volume)

    print(f"\nScanning {folder}...\n")

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".jpg", ".png", ".jpeg")):
                path = os.path.join(root, file)

                try:
                    text = pytesseract.image_to_string(Image.open(path), lang="eng")

                    if SEARCH_WORD in text.lower():
                        print("Found in:", path)

                except:
                    pass