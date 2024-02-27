import pytesseract
from PIL import ImageGrab
from flask import Flask, Response, render_template
import webbrowser
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # path to tesseract installation

app = Flask(__name__)

last_image = None

current_directory = os.getcwd()

@app.route('/', methods=['GET', 'POST'])

def update_page_with_ocr_text():
    ocr_image = ImageGrab.grabclipboard()

    if ocr_image:
        ocr_image.save(current_directory + '\\images\\clipboard.png') #path to temporary image
        text = pytesseract.image_to_pdf_or_hocr(ocr_image, extension='hocr', lang='eng+jpn+chi_sim+chi_tra+kor+spa+fra') # selected languages
        return Response(text, mimetype='text/html')
    else:
        return render_template('index.html', result='No image found in clipboard.')

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true': # Prevents the browser from opening twice
        webbrowser.open('http://www.localhost:5000')
    app.run(debug=True)