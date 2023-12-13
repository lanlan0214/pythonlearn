import requests
from bs4 import BeautifulSoup
import concurrent.futures
from datetime import datetime
import time

# 初始化前一次的股票資訊字典
previous_stock_info = {}

# 定義股票列表
stock_urls = {
    '0050': 'https://tw.stock.yahoo.com/quote/0050',
    '2376': 'https://tw.stock.yahoo.com/quote/2376',
    '2377': 'https://tw.stock.yahoo.com/quote/2377',
    '3443': 'https://tw.stock.yahoo.com/quote/3443',
    '8046': 'https://tw.stock.yahoo.com/quote/8046',
    # 添加更多股票的 URL
}

def get_stock_info(stock_code, url):
    global previous_stock_info

    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.find('h1', class_="C($c-link-text) Fw(b) Fz(24px) Mend(8px)")
    a = soup.select('.Fz\(32px\)')[0]
    b = soup.select('.Fz\(20px\)')[0]
    s = ''
    if soup.select("#main-0-QuoteHeader-Proxy")[0].find('div', class_="D(f) Ai(fe) Mb(4px)").find('span', class_="C($c-trend-down)"):
        s = '-'
    elif soup.select("#main-0-QuoteHeader-Proxy")[0].find('div', class_="D(f) Ai(fe) Mb(4px)").find('span', class_='C($c-trend-up)'):
        s = '+'
    else:
        s = ''

    # 使用 strip() 函數去掉 b 中的空白字符
    b_value = b.get_text().strip()

    current_stock_info = f'{title.get_text()} : {a.get_text()} ( {s}{b_value} )'

    # 如果 b 的值為 0，則跳過自動刷新的步驟
    if b_value == '0':
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {current_stock_info} (Skipping refresh, b is 0)')
    else:
        # 比較前一次和當前的股票資訊，如果有變動才顯示
        if current_stock_info != previous_stock_info.get(stock_code):
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {current_stock_info}')
            previous_stock_info[stock_code] = current_stock_info

# 設定自動刷新的間隔時間（秒）
refresh_interval = 10

with concurrent.futures.ThreadPoolExecutor() as executor:
    while True:
        # 使用 ThreadPoolExecutor 來同時爬取多支股票的資訊
        futures = {executor.submit(get_stock_info, stock_code, stock_url): stock_code for stock_code, stock_url in stock_urls.items()}
        concurrent.futures.wait(futures)

        time.sleep(refresh_interval)
