

import requests
from bs4 import BeautifulSoup
import os

# 取得使用者輸入的目錄名稱和網址
folder_name = input("請輸入目錄名稱： ")
url = input("請輸入網址： ")

# 創建目錄
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

web = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0    #  設定圖片編號

for i in imgs:
    print(i['src'])
    jpg = requests.get(i['src'])
    # 使用 os.path.join 來建立路徑
    file_path = os.path.join(folder_name, f'test_{name}.jpg')
    with open(file_path, 'wb') as f:
        f.write(jpg.content)
    name += 1

#https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html
#抓ptt圖