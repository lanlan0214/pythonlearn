import datetime

now = datetime.datetime.now()
oneday = datetime.datetime(2020,1,1)
gap = datetime.timedelta(1)
diff = now - oneday
tomorrow = now + gap

print(diff)
print(type(diff))
print(diff.days)
print(diff.total_seconds())
print(tomorrow)