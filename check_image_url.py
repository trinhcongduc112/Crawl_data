import requests
from bs4 import BeautifulSoup

r = requests.get('https://docs.abivin.com/changelog/mar-09-2023-release-note')
soup = BeautifulSoup(r.text, 'html.parser')
imgs = soup.find_all('img')

print("Images on page:")
for img in imgs:
    src = img.get('src', '')
    print(f"  {src}")




