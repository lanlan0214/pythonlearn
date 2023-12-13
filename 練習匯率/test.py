def calculate_tax(price, tax_rate):
    tax_amount = price * tax_rate
    return tax_amount

def get_tax_rate(product_type, custom_rates):
    if product_type in custom_rates:
        return custom_rates[product_type]
    else:
        return float(input(f"請輸入商品 '{product_type}' 的稅率或匯率: "))

total_amount = 0  # 初始化總金額
selected_products = set()  # 用於記錄選擇的商品

# 定義 custom_rates 字典
custom_rates = {
    "巧克力": 0.03,
    "衣服": 0.12,
    "塑膠": 0.08
    # 可以在這裡新增其他商品類型及其默認稅率
}

while True:
    # 使用者輸入價格和商品種類
    user_price = float(input("請輸入價格 (輸入0表示結束): "))
    
    if user_price == 0:
        break  # 如果使用者輸入0，則結束循環
    
    user_product_type = input("請輸入商品種類 (巧克力, 衣服, 塑膠 或其他): ")
    
    # 將商品添加到已選擇的商品集合中
    selected_products.add(user_product_type)

    # 取得商品的稅率或匯率
    user_tax_rate = get_tax_rate(user_product_type, custom_rates)

    # 如果金額低於2000，不計算稅金
    if user_price <= 2000:
        total_amount += user_price
        print("金額低於等於2000則沒有稅率")
    else:
        # 計算稅金
        tax_result = calculate_tax(user_price, user_tax_rate)

        # 將金額和稅金加到總金額
        total_amount += user_price + tax_result

# 印出最終結果
print(f"總金額（包括稅金）為: {total_amount}")

# 印出已選擇的商品及其對應的默認稅率
print("已選擇的商品及其對應的默認稅率:")
for product in selected_products:
    print(f"{product}: {custom_rates.get(product, user_tax_rate)}")

input("按下 Enter 鍵以結束程式...")
