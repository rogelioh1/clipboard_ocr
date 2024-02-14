import pytesseract
from PIL import ImageGrab
from PIL import Image
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def update_page_with_ocr_text():
    
    ocr_image = ImageGrab.grabclipboard()

    if ocr_image:
        ocr_image.save('images/clipboard.png')
        text = pytesseract.image_to_pdf_or_hocr(ocr_image, extension='hocr', lang='eng+jpn')
        return Response(text, mimetype='text/html')
    
    else:
        return render_template('index.html', result='No image found in clipboard.')
    
if __name__ == '__main__':
    app.run(debug=True)