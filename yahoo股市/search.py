import requests
import pandas as pd

# 定義 API 網址
api_url = 'https://data.gcis.nat.gov.tw/od/data/api/F0E8FB8D-E2FD-472E-886C-91C673641F31'

# 定義參數
params = {
    '$format': 'json',
    '$filter': 'Company_Status eq 01 and Capital_Stock_Amount eq E',
    '$skip': '0',
    '$top': '1000',  # 每次最多撈取的資料筆數
}

def parse_json_data_to_excel(api_url, params):
    try:
        all_data = []  # 用於存儲所有資料的列表
        data_count = 0  # 計數器，記錄已獲取的資料筆數

        while data_count < 50000:  # 當已獲取的資料筆數小於 5000 時繼續迴圈
            # 發送 GET 請求並獲取網頁內容
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # 如果請求失敗，則引發異常
            # 解析 JSON 格式的響應
            data = response.json()

            # 如果資料為空，表示已經取得所有資料，退出迴圈
            if not data:
                break

            # 計算本次獲取的資料筆數
            num_data = len(data)
            # 更新計數器
            data_count += num_data

            # 如果已獲取的資料筆數超過 5000，只取其中前 5000 筆資料
            if data_count > 50000:
                data = data[:50000 - (data_count - num_data)]

            all_data.extend(data)  # 將本次獲取的資料添加到 all_data 列表中
            params['$skip'] = str(int(params['$skip']) + 1000)  # 更新 $skip 參數的值

        # 將所有資料轉換為 DataFrame
        df = pd.DataFrame(all_data)
        
        # 在 Company_Location 中篩選包含新北市和台北市的資料
        df_filtered = df[df['Company_Location'].str.contains('新北市|臺北市')]

        # 將 DataFrame 寫入 Excel 文件，並指定中文標題
        excel_file = 'company_data.xlsx'
        df_filtered.to_excel(excel_file, index=False, columns=[
            'Business_Accounting_NO',
            'Company_Name',
            'Company_Status',
            'Company_Status_Desc',
            'Capital_Stock_Amount',
            'Paid_In_Capital_Amount',
            'Responsible_Name',
            'Register_Organization',
            'Register_Organization_Desc',
            'Company_Location',
            'Company_Setup_Date',
            'Change_Of_Approval_Data'
        ], header=[
            '統一編號',
            '公司名稱',
            '公司狀態',
            '公司狀態說明',
            '資本額',
            '實收資本額',
            '負責人姓名',
            '登記機關',
            '登記機關說明',
            '公司地址',
            '公司設立日期',
            '核准變更日期'
        ])

        print(f'Data saved to {excel_file} successfully.')
    except Exception as e:
        print(f'Error: {str(e)}')

# 解析並處理 JSON 數據，並保存為 Excel 文件
parse_json_data_to_excel(api_url, params)
