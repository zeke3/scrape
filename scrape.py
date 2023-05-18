import requests
from bs4 import BeautifulSoup

def redirect_link(url):
    response = requests.get(url, allow_redirects=False)

    if response.status_code in (300, 301, 302, 303, 307):
        redirect_location = response.headers['Location']
        redirected_response = requests.get(redirect_location)
        print(redirected_response.url)
        return redirected_response.url
    else:
        print("Passed")
    return url


# data = open('tra-receipt.html', 'r')
data = requests.get(redirect_link('https://verify.tra.go.tz/E215B4207332_093108'))
# data = requests.get(redirect_link('https://verify.tra.go.tz/Verify/Verified?Secret=09:31:08'))
# print(data.text)
# print(data.read())
# soup = BeautifulSoup(data.read(), 'html.parser')
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)


# data_dict = {}
# for tr in soup.find_all('tr'):
#     for th in tr.find_all('th'):
#         for td in tr.find_all('td'):
#             data_dict[th.text] = td.text

# print(data_dict)            