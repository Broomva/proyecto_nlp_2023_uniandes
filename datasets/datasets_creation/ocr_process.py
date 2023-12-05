#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Convert the first 3 pages of the PDF into images
pdf_path = 'files/constitucion_5.pdf'
pages = convert_from_path(pdf_path, first_page=69, last_page=89)

text = [pytesseract.image_to_string(image=page, lang='spa') for page in pages]

with open('constitucion_nasa_yuwe_spanish.txt', 'w') as f:
    for item in text:
        f.write("%s\n" % item)
        
#%%

pages = convert_from_path(pdf_path, first_page=91, last_page=96)

text = [pytesseract.image_to_string(image=page, lang='spa') for page in pages]

with open('palabras_importantes_nasa_yuwe_spanish.txt', 'w') as f:
    for item in text:
        f.write("%s\n" % item)

# %%
