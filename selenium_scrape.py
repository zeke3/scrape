import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Path to the ChromeDriver executable
chromedriver_path = '/Users/Eze/Downloads/chromedriver_mac64/chromedriver'  # Replace with the actual path to chromedriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Navigate to the current webpage
driver.get('https://verify.tra.go.tz/E215B4207332_093108')

# Execute JavaScript code to update the URL
new_url = 'https://verify.tra.go.tz/Verify/Verified?Secret=09:31:08'
driver.execute_script(f'window.history.pushState(null, "", "{new_url}")')

# Alternatively, you can use the following code to redirect to a new URL:
# driver.execute_script(f'window.location.href = "{new_url}"')

# Get the updated URL
current_url = driver.current_url
data = requests.get(current_url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)
print('Updated URL:', current_url)

# Close the browser
driver.quit()
