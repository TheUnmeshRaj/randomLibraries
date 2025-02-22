import requests
from bs4 import BeautifulSoup


def fetchToFile(url,path):
  r = requests.get(url)
  with open(path,'w') as f:
    f.write(r.text)

url = "https://www.amazon.in/s?k=bacca+bucci+shoes"
fetchToFile(url,'data.html')
