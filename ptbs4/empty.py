#pip install bs4
#pip install lxml
from bs4 import BeautifulSoup

# 如果要貼比較多string 就要用三個"""符號
text = """
    <html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p class="title hello item">123</p>
    <a target="_blank" href="https://www.google.com" >123</a>
    <p class="test">321</p>
</body>
</html>
"""

soup = BeautifulSoup(text, 'lxml')
# print(soup.find("p"))
# # 這邊尋找如果要找class要加個底線
# print(soup.find(class_="title"))
# # 想找p tag然後class是title
# print(soup.find("p" , class_="title"))
# # 找全部
# print(len(soup.find_all("p" )))
# tag的
first_p_tag = soup.find("p")
print(first_p_tag.get("class"))
# 這是看這裡面內容
print(first_p_tag.getText())
print(first_p_tag["class"])