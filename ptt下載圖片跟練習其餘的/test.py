import os

# print(os.pardir)
# print(os.listdir(os.pardir))
# 這樣會因為不同作業系統 而改變

import datetime

x = datetime.datetime.now()

print(x.strftime("%H:%M:%S"))