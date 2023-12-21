# # 如果有出現 250之後的就代表已經有連上了
# # getpass這是要隱藏輸入的帳密
# # (235, b'2.7.0 Accepted') 這是成功後會顯示的
# # 在google應用程式密碼 然後設置密碼 到時候也是可以刪除
# # 用python寄email

import smtplib
import getpass

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = input("Enter your email:")
password = getpass.getpass("Enter your password:")
smtp_obj.login(email, password)

from_address = email
to_address = email
subject = input("Enter subject:")
message = input("Enter message:")
full_message = "Subject: " + subject + "\n" + message

print(smtp_obj.sendmail(from_address, to_address, full_message))
smtp_obj.quit()