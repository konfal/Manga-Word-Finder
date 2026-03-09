# Manga Word Finder

A small Python script that scans manga pages and tells you exactly where a specific word appears.

Instead of manually flipping through hundreds of pages, this script scans the pages using OCR and tells you which images contain the word you're looking for.

It works with any manga

---

## What This Tool Does

This script goes through manga volumes stored on your computer and searches every page for a word you choose.

Under the hood it:

- walks through your manga folders
- opens each page image
- extracts the text using Tesseract OCR
- checks if the word appears
- prints the page path if it does

---

## Example output

```
Scanning C:\manga\volume 45...

Found in: C:\manga\volume 45\page_012.jpg
Found in: C:\manga\volume 45\page_103.jpg
```

So if you're looking for something like:

Naruto  
Luffy  
Sasuke  

the script will tell you exactly which pages contain that word.

---

## Requirements

Before running the script you'll need a few things installed.

### Python libraries

Install them with pip:

```bash
pip install pytesseract pillow
```

Libraries used:

- pytesseract – Python wrapper for the Tesseract OCR engine
- Pillow – used to open and process image files

### Tesseract OCR

This project relies on Tesseract, which is the OCR engine that actually reads the text inside images.

You can install it from the official repository:

https://github.com/tesseract-ocr/tesseract

Once installed, make sure the script knows where Tesseract is located.

If your installation path is different, just update that line.

---

## Folder Structure

The script expects your manga to be organized in folders.

Example:

```
manga/
volume 45/
page1.jpg
page2.jpg
page3.jpg

volume 46/
page1.jpg
page2.jpg
```

Each volume folder should contain the page images.

Supported formats:

- jpg
- jpeg
- png

---

## Running the Script

Run the script normally with Python:

```bash
python manga_word_finder.py
```

The program will ask you two things.

First, which volumes you want to scan.

Example input:

```
volume 45,volume 46
```

(it depends on how the folder containing the volume is named)

Then it will ask for the word you want to search.

The script will then scan every page and print the locations where the word appears.

---

## How It Works

Since manga pages are images, normal text search doesn't work.

So the script uses OCR (Optical Character Recognition).

For every page it:

- Opens the image
- Extracts the text using Tesseract
- Converts everything to lowercase
- Checks if the search word appears
- Prints the page path if it does

It's basically a simple automated search engine for manga pages.

---

## Things To Keep In Mind

OCR works surprisingly well, but it's not perfect.

Results depend a lot on the scan quality.

Things that may affect accuracy:

- low resolution pages
- unusual fonts
- stylized speech bubbles
- distorted text

For most English manga scans though, it works pretty well.

---

## Why I Made This

I mainly built this for fun and because I wanted a quick way to search through manga volumes without manually checking every page.

It's a simple script, but it solves a very annoying problem if you have large manga collections.

If you want to experiment with it or improve it, feel free to do so.

---

## License

MIT License.

Use it however you want.
