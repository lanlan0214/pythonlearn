# import yfinance as yf
# import datetime

# def get_tsmc_stock_data():
#     start_date = datetime.datetime(2024, 2, 1)
#     end_date = datetime.datetime(2024, 2, 29)
#     # 這裡的"2330.TW"代表台積電在Yahoo Finance的代碼
#     df = yf.download("2330.TW", start=start_date, end=end_date)
#     return df

# def save_to_csv(data_frame, file_path):
#     data_frame.to_csv(file_path)

# def main():
#     stock_data = get_tsmc_stock_data()
#     save_to_csv(stock_data, 'tsmc_stock_data.csv')

# if __name__ == "__main__":
#     main()

import yfinance as yf
import datetime

def get_tsmc_stock_data():
    start_date = datetime.datetime(2016, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)
    # 這裡的"2330.TW"代表台積電在Yahoo Finance的代碼
    df = yf.download("2330.TW", start=start_date, end=end_date)
    return df

def save_to_csv(data_frame, file_path):
    # 將日期格式調整成 "1/3/2017" 的形式
    data_frame.index = data_frame.index.strftime('%m/%d/%Y')
    # 將 Volume 欄位中的數字格式調整成有逗號分隔的形式
    data_frame['Volume'] = data_frame['Volume'].apply(lambda x: '{:,}'.format(x))
    # 將 Open、High、Low、Close 欄位保留兩位小數
    data_frame[['Open', 'High', 'Low', 'Close']] = data_frame[['Open', 'High', 'Low', 'Close']].round(2)
    data_frame.to_csv(file_path)

def main():
    stock_data = get_tsmc_stock_data()
    save_to_csv(stock_data, 'tsmc_stock_data1.csv')

if __name__ == "__main__":
    main()
