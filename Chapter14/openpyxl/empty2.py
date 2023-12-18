from openpyxl import Workbook
import os
import csv

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "file.csv")

data_rows = [fields for fields in csv.reader(open(file_path, newline=""))]

wb = Workbook()
ws = wb.active
ws.title = "MyFile"
ws.sheet_properties.tabColor = "1072BA"
for row in data_rows:
    ws.append(row)

wb.save("Myfile.xlsx")
