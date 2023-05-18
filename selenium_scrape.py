import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from PIL import Image
import io
import base64

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://verify.tra.go.tz/E215B4207332_093108"
result = re.search(r'_(.*)$', link)

if result:
    extracted_text = result.group(1)
    # Add colons to separate hours, minutes, and seconds
    formatted_text = re.sub(r'(\d{2})(\d{2})(\d{2})', r'\1:\2:\3', extracted_text)
    # print(formatted_text)

# Path to the ChromeDriver executable
chromedriver_path = '/Users/Eze/Downloads/chromedriver_mac64/chromedriver'  # Replace with the actual path to chromedriver

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a new instance of the Chrome driver with the configured options
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to the current webpage
driver.get(link)

# Execute JavaScript code to update the URL
new_url = f'https://verify.tra.go.tz/Verify/Verified?Secret={formatted_text}'
driver.execute_script(f'window.history.pushState(null, "", "{new_url}")')

# Get the updated URL
current_url = driver.current_url
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')

#Getting receipt data
data_dict = {}
for tr in soup.find_all('tr'):
    for th in tr.find_all('th'):
        for td in tr.find_all('td'):
            data_dict[th.text] = td.text.replace(',', '')

print(data_dict)   

# Wait for page to fully load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get page dimensions
page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')

# Set window size to match the entire page
driver.set_window_size(page_width, page_height)

# Capture full-page screenshot
screenshot_path = 'screenshot.png'
driver.save_screenshot(screenshot_path)

# Close the browser
driver.quit()
