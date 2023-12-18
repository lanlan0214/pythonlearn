from openpyxl import load_workbook
import os

# 取得程式檔案的目錄
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "Dodgers.xlsx")

wb = load_workbook(file_path)
result = []

wb = wb.worksheets[0]

for row in wb.iter_rows():
  # list comprehension
  result.append([cell.value for cell in row])
sum = 0
for r in result[1:]:
  sum += int(r[11])
     
print(f"Homeruns {sum}")
