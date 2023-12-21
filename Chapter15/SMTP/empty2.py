# # receiving email
import imaplib
import email as em

M = imaplib.IMAP4_SSL("imap.gmail.com")
email = "123@gmail.com"
password = "123"
M.login(email, password)
# 這會顯示全部裡面的信
# M.list()
# 收件夾
M.select("inbox")
result, ids = M.search(None, "FROM 123@gmail.com")
result2, content = M.fetch(ids[0], "(RFC822)")

raw_content = content[0][1]
email_content = raw_content.decode("utf-8")
email_message = em.message_from_string(email_content)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        with open("email_content.txt", mode="wb") as f:
            f.write(body)
            
            
# 額外補充資料
# 在print(ids[0])時，如果有較多寄件給自己的內容，ids[0]的值可能會是

# b'688 690 694 716 717 1783 1808 3416 5464 5465 9327 10223 11100 11102 11237 11240 12708 12709 12710 12711 12712 12713 12714 12715 12716 12717 12718 12719 12720 12721 13340 13473 13475 13902 13903 13904 15598 15605'

# 像這樣的結果。我們可以看出，ids[0]是個binary string，內部有多個email的id。如果直接執行下面步驟：

# rest,content = M.fetch(ids[0], "(RFC822)")
# print(content)
# 會出現

# imaplib.IMAP4.error: FETCH command error: BAD [b'Could not parse command']

# 解決辦法是，ids[0]內部如果有多個數字的話，只需要先將ids[0]先做decode，再用split(" ")根據空格做分隔。最後在fetch的階段，可以針對要獲得的email做選擇。例如：

# result, ids = M.search(None, "FROM yourOwnEmail@gmail.com")
 
# myString = ids[0].decode("utf-8") # 先將ids[0]做decode，從bytes變成string
# myEmailList = myString.split(" ") # 將string內部的數字分開
# rest, content = M.fetch(myEmailList[0], "(RFC822)") #這裡的index是可以改的
# c = content[0][1]
# e = c.decode("utf-8")
# print(e)
# 更改index的部分，就可以取得不同的email的內容。