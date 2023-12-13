try:
    lst = [1,2,3]
    print(lst[4])

except LookupError:
    print("This is LookupError")


except IndexError:
    print("This is IndexError")


