import bs4
import requests

# result = requests.get("https://zh.wikipedia.org/zh-tw/Wikipedia:%E9%A6%96%E9%A1%B5")
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# image = soup.select("img.mw-file-element")[2]

# print(image["src"])
# print(image["class"])
# print(image["width"])

## 抓到圖片 並且下載
# 發送 HTTP GET 請求到指定的 URL，並將伺服器的回應存儲在 result1 中
result1 = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Gate_of_AHNU_of_the_Old_Campus.jpg/120px-Gate_of_AHNU_of_the_Old_Campus.jpg")

# 使用 open 函數以二進制寫入模式打開名為 "Frank.jpg" 的檔案
# "wb" 參數表示以二進制寫入模式打開檔案
with open("Frank.jpg", "wb") as f:
    # 將 result1 中的二進制內容寫入到 "Frank.jpg" 檔案中
    f.write(result1.content)