import requests
from bs4 import BeautifulSoup

def find_company_phone(company_name):
    # 构建搜索的URL，这里以Google为例
    search_url = f"https://www.google.com/search?q={company_name}+phone"
    
    # 发送HTTP请求并获取响应
    response = requests.get(search_url)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 在Google搜索结果中找到电话号码
        # 这里假设电话号码在class为 "phone" 的元素中
        phone_element = soup.find(class_='phone')
        
        # 提取电话号码文本
        if phone_element:
            phone_number = phone_element.text
            return phone_number.strip()  # 去除首尾空白字符
        else:
            return "未找到电话号码"
    else:
        return "无法连接到网页"

# 测试
company_name = input("请输入公司名称：")
phone_number = find_company_phone(company_name)
print(f"{company_name} 的电话号码是：{phone_number}")
