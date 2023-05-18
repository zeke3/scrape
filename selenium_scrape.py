import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Path to the ChromeDriver executable
chromedriver_path = '/Users/Eze/Downloads/chromedriver_mac64/chromedriver'  # Replace with the actual path to chromedriver

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a new instance of the Chrome driver with the configured options
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=chromedriver_path)

# Navigate to the current webpage
driver.get('https://verify.tra.go.tz/E215B4207332_093108')

# Execute JavaScript code to update the URL
new_url = 'https://verify.tra.go.tz/Verify/Verified?Secret=09:31:08'
driver.execute_script(f'window.history.pushState(null, "", "{new_url}")')

# Alternatively, you can use the following code to redirect to a new URL:
# driver.execute_script(f'window.location.href = "{new_url}"')

# Get the updated URL
current_url = driver.current_url
# print(driver.page_source)
data = driver.page_source
# data = requests.get(current_url)
# print(data.text)
soup = BeautifulSoup(data, 'html.parser')
# print(soup)
data_dict = {}
for tr in soup.find_all('tr'):
    for th in tr.find_all('th'):
        for td in tr.find_all('td'):
            data_dict[th.text] = td.text.replace(',', '')

print(data_dict)     
# print('Updated URL:', current_url)

# Close the browser
driver.quit()
