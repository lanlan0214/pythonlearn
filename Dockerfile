# 使用官方的 Python 基本映像
FROM python:3.8

# 設定工作目錄
WORKDIR /app

# 將本地的應用程式代碼複製到容器中
COPY . /app

# 安裝應用程式依賴
RUN pip install --no-cache-dir -r requirements.txt

# 定義啟動指令
CMD ["python", "app.py"]
