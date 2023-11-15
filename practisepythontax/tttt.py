def calculate_import_duty(package_value, import_tax_rate, sales_tax_rate):
    # 計算進口稅額
    import_tax = package_value * (import_tax_rate / 100)

    # 計算營業稅額
    sales_tax = (package_value + import_tax) * (sales_tax_rate / 100)

    # 計算關稅總額
    total_duty = import_tax + sales_tax

    return import_tax, sales_tax, total_duty

# 讓使用者輸入包裹總金額
package_value = float(input("請輸入包裹總金額（NTD）: "))

import_tax_rate = float(input("請輸入進口稅率（%）: "))
sales_tax_rate = 5  # 營業稅率（%）

# 計算關稅
import_tax, sales_tax, total_duty = calculate_import_duty(package_value, import_tax_rate, sales_tax_rate)

# 顯示結果
print(f"進口稅額：NT${import_tax:.2f}")
print(f"營業稅額：NT${sales_tax:.2f}")
print(f"關稅總額：NT${total_duty:.2f}")

input("按下 Enter 鍵以結束程式...")