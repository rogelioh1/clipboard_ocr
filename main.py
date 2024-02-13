import pyperclip
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def display_text_in_browser(text, driver=None):
    driver.get("")

def display_hocr_in_browser(driver=None):
    driver.get('file:///output.hocr')

def main():
    s = Service('C:\\tools\\geckodriver.exe')
    option = Options()
    option.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(option, s)

    while True:
        print("Press 'q' to quit")
        if input() == 'q':
            if driver != None:
                driver.quit()
            break
        else:
            screenshot = ImageGrab.grabclipboard()
            if screenshot:
                hocr_text = pytesseract.image_to_pdf_or_hocr(screenshot, extension='hocr')
                with open('output.hocr', 'w+b') as f:
                    f.write(hocr_text)
                
                ##text = pytesseract.image_to_string(screenshot)
                ##print(text)
                ##display_text_in_browser(text, driver)
                display_hocr_in_browser(driver)
                print("Text displayed in browser")
                time.sleep(2)
            else:
                print("No image found in clipboard")

if __name__ == "__main__":
    main()