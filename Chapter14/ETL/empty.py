import csv

with open("14-1file.csv", newline="", encoding="utf8") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row[1].title())