import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import cv2
import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

img_file= "/content/img_file.png"
img= Image.open(img_file)

image = cv2.imread('/content/img_file.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply image enhancement techniques (e.g., brightness, contrast, sharpness adjustments)
enhanced_image = cv2.convertScaleAbs(gray_image, alpha=1.2, beta=10)

# Apply thresholding to convert the image to binary
_, thresholded_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Apply noise removal techniques (e.g., blurring)
denoised_image = cv2.GaussianBlur(thresholded_image, (3, 3), 0)
custom_config = r'--psm 3 --oem 1 -l eng'

ocr_result = pytesseract.image_to_string(denoised_image, config= custom_config)
doc = nlp(ocr_result)
print(ocr_result)
print(doc)

#1. Printing the GST number


import re
gst_pattern = r'\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}\ \d{1}[A-Z]{2}\b'
gst_numbers = re.findall(gst_pattern, ocr_result)
for match in gst_numbers:
  match = match.replace(' ', '')
print(match)

#2. Printing the total

import re

# Define a pattern or regular expression to match the total amount
pattern = r'Total\s*\=\s*\₹?(\d+(?:\.\d{2})?)'

# Search for the pattern in the extracted text
match_total = re.findall(pattern, ocr_result)

print(match_total)

