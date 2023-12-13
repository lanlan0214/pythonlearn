import buildexception

try:
    num = "test"
    buildexception.enter_age(num)
except buildexception.NegaviteNumberException as error:
    print(error)
except:
    print("Something we don't know went wrong!")