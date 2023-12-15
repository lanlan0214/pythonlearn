

unicode_string = '河'
utf_bytes = unicode_string.encode('utf-8')
print(utf_bytes)

result_string = utf_bytes.decode()
print(result_string)