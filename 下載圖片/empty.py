import bs4
import requests

result = requests.get("https://zh.wikipedia.org/zh-tw/Wikipedia:%E9%A6%96%E9%A1%B5")
soup = bs4.BeautifulSoup(result.text, 'lxml')
image = soup.select("img.mw-file-element")[2]

print(image["src"])
print(image["class"])
print(image["width"])