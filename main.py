import pyperclip
import time
import pytesseract
import selenium
import webdriver_manager
from PIL import ImageGrab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def display_text_in_browser(text):
    driver = webdriver.Chrome()
    driver.get("data:text/html,<h1 id=\"text\" style=\"text-align: center; margin-top: 50vh;\">"+text+"</h1>")
    driver.quit()

def main():
    while True:
        print("Press 'q' to quit")
        if input() == 'q':
            break
        else:
            screenshot = ImageGrab.grabclipboard()
            if screenshot:
                text = pytesseract.image_to_string(screenshot)
                print(text)
                display_text_in_browser(text)
                print("Text displayed in browser")
                time.sleep(2)
            else:
                print("No image found in clipboard")
                time.sleep(2)

if __name__ == "__main__":
    main()