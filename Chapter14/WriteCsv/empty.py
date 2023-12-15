import csv

with open("new.csv",mode="w", newline="", encoding="cp950") as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerow(['a', 'b', 'c'])
    csv_writer.writerows([['a', 'b', 'c'],['h', 's', 't']])