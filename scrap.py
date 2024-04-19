import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import requests
from PIL import Image
import pytesseract

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# Path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
webdriver_service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get('https://mphc.gov.in/case-status')

# Locate the CAPTCHA image element
captcha_td_element = driver.find_element(By.XPATH, "//table//tr//td[2]//img")

# Take a screenshot of the 2nd td
captcha_td_element.screenshot("captcha_td_screenshot.png")

# Read image using OpenCV
captcha_image = cv2.imread("captcha_td_screenshot.png")

# Convert image to grayscale
captcha_image_gray = cv2.cvtColor(captcha_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, captcha_image_thresh = cv2.threshold(captcha_image_gray, 150, 255, cv2.THRESH_BINARY)

# Save the preprocessed image
cv2.imwrite("captcha_preprocessed.png", captcha_image_thresh)

# Open the preprocessed image
captcha_image_preprocessed = Image.open("captcha_preprocessed.png")

# Use pytesseract to extract text from the preprocessed image
captcha_text = pytesseract.image_to_string(captcha_image_preprocessed).strip()

# Close the image
captcha_image_preprocessed.close()

# Print the extracted text
print("Extracted text from the CAPTCHA image:", captcha_text)

# Find the input element by its ID
input_element = driver.find_element(By.ID, "code")
input_element.clear()

# Find the input element with id "txtnoS"
input_element = driver.find_element(By.ID, "txtnoS")
input_element.send_keys("123")

dropdown_element = driver.find_element(By.ID, "lst_caseS")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("WP - WRIT PETITION")

dropdown_element = driver.find_element(By.ID, "txtyear")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("2015")

button_element = driver.find_element(By.ID, "bt1")
#button_element.click()

time.sleep(7)
driver.quit()