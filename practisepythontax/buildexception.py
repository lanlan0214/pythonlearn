class NegaviteNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if (age < 0):
            print("This is not a vaild age")


def enter_age(age):
    if age < 0:
        raise NegaviteNumberException(age)
    if age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age is odd.")


# 自訂一個error function 然後再buildexceptionmain 裡面用到 可以測試 ~ nice!!
# 自訂的function 可以用在沒有內建的error function 這樣可以更快的test