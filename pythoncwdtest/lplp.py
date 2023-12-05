import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor

def download(url_and_name):
    url, name = url_and_name
    print(url)
    jpg = requests.get(url)
    file_path = os.path.join(folder_name, f'test_{name}.jpg')
    with open(file_path, 'wb') as f:
        f.write(jpg.content)

# 取得使用者輸入的目錄名稱和網址
folder_name = input("請輸入目錄名稱： ")
url = input("請輸入網址： ")

# 創建目錄
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

web = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0

img_urls = [(i['src'], name) for name, i in enumerate(imgs)]

# 使用 ThreadPoolExecutor 執行多執行緒下載
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls)
