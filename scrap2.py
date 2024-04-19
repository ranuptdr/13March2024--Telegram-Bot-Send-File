from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import os
import pytesseract
from PIL import Image
import requests


# File path
file_path = 'captcha2.png'

# Check if the file exists
if os.path.exists(file_path):
    # Remove the file
    os.remove(file_path)
    print(f"File '{file_path}' has been removed.")
else:
    print(f"File '{file_path}' does not exist.")
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome in maximized mode
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# Path to tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


# Provide path to the chromedriver executable
webdriver_service = Service('./chromedriver.exe') 
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the webpage
driver.get('https://mphc.gov.in/case-status')

# Wait for the captcha to load
captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cp_img')))

# Save screenshot of the captcha
captcha_img.screenshot("./captcha2.png")

# Read captcha using pytesseract
captcha_text = pytesseract.image_to_string(Image.open("./captcha2.png")).strip()

# Assuming you have already extracted the captcha text
#captcha_text = "B13"

# Replace 'B' with '8' in captcha_text
captcha_text = captcha_text.replace('B', '8')

# Print the modified captcha text
print('Modified Captcha Text >>>', captcha_text)
# Find the input field for captcha and fill it
captcha_input = driver.find_element(By.ID, 'code')
captcha_input.send_keys(captcha_text)

# Find the input element with id "txtnos" and fill it
input_element = driver.find_element(By.ID, "txtnoS")
input_element.send_keys("123")

# Find the select element by its ID for case type
select_element = driver.find_element(By.ID, "lst_caseS")
select = Select(select_element)
select.select_by_visible_text("WP - WRIT PETITION")

# Find the select element by its ID for year
select_element = driver.find_element(By.ID, "txtyear")
select = Select(select_element)
select.select_by_visible_text("2010")

# Find the button element by its ID and click it
button_element = driver.find_element(By.ID, "bt1")
button_element.click()

# Find the first <td> within the <thead>
first_td = driver.find_element(By.XPATH,"//table[@class='mphc_first']/thead/tr/th[1]/label")
# Extract the inner text of the first <td>
if first_td:
    stage = first_td.text
    print("Inner text of the first <td>:", stage)
    
    url = f'https://api.telegram.org/bot6382859668:AAFI5niH0r-L0bFyjvW6-wL75W1OK5lSv6A/sendMessage?chat_id=5656784248&text={stage}'
    hdrs= {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Connection":"keep-alive"
    }
    response = requests.get(url,headers=hdrs)

    if response.status_code == 200:
        print('Sent Successfully :) ')
        pass
    else:
        print('Unable to Send :( ')
        pass
    
else:
    print("No <td> found within <thead>")
  
print(select_element)
print(select)

time.sleep(20)

# Close the browser
driver.quit()