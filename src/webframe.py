import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
nyt_html = r.text

soup = BeautifulSoup(nyt_html,"html.parser")
for h2 in soup.findAll("h2", class_="esl82me2"):
    print(h2.text)