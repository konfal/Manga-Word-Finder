import pytesseract
from PIL import Image
import os

# ---------------------------------------------------------
# 1️⃣ SETUP
# ---------------------------------------------------------

# change this if your tesseract is installed somewhere else
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# this is the folder that contains ALL your manga volumes
# example structure:
# C:\manga
#    ├── volume 45
#    ├── volume 46
#    └── volume 47
BASE_FOLDER = r"C:\manga"

# ---------------------------------------------------------
# 2️⃣ USER INPUT
# ---------------------------------------------------------

# ask the user which volumes they want to scan
# example input: volume 45,volume 46
volumes_input = input("Enter volumes (example: volume 45,volume 46): ")

# word we want to search inside the manga pages
SEARCH_WORD = input("Enter word to search: ").lower()

# turn the input string into a list
# "volume 45,volume 46" -> ["volume 45", "volume 46"]
volumes = [v.strip() for v in volumes_input.split(",")]

# ---------------------------------------------------------
# 3️⃣ SCAN EACH VOLUME
# ---------------------------------------------------------

for volume in volumes:

    # build the full path to the volume folder
    folder = os.path.join(BASE_FOLDER, volume)

    print(f"\nScanning {folder}...\n")

    # walk through every folder + subfolder
    for root, dirs, files in os.walk(folder):

        for file in files:

            # only check image files (manga pages)
            if file.lower().endswith((".jpg", ".png", ".jpeg")):

                path = os.path.join(root, file)

                try:
                    # use OCR to extract text from the manga page
                    text = pytesseract.image_to_string(
                        Image.open(path),
                        lang="eng"
                    )

                    # check if our word appears in the page
                    if SEARCH_WORD in text.lower():
                        print("Found in:", path)

                except:
                    # sometimes OCR crashes on weird images
                    # we just skip the page and keep going
                    pass