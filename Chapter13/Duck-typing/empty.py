# # type () 以下這些通常只會用在debug

# print(type("Goodbye"))
# print(type("Hello") == type("Goodbye"))
# print(type("Hello") == type(5))

############################################################################################

# # isintance(obj, class) 這在需要檢查物件是否屬於多個可能類型之一的情況下很有用。 內建函數

# class C:
#     pass

# class B(C):
#     pass

# class A(B):
#     pass

# a = A()
# b = B()
# c = C()

# print(isinstance(a, A)) # True
# print(isinstance(a, B)) # True
# print(isinstance(c, A)) # False

############################################################################################

# # issubclass 子集合

# class C:
#     pass

# class B(C):
#     pass

# class A(B):
#     pass

# print(issubclass(C, A)) # False
# print(issubclass(A, B)) # True
# print(issubclass(A, C)) # True

############################################################################################

# The sorted function is using the principle of DuckTyping
# This is the duck typing style design

# print(sorted(['for', 'box', 'head']))
# print(sorted({'for', 'box', 'head'}))
# print(sorted({'key1':'for', 'key2':'box', 'key3':'head'}))
# print(sorted('forboxhead'))

# try:
#     print(sorted(999966464646))
# except:
#     print("Error happened while using sorted function.")

# 數字是可以跟字串相*的

def calculate(x, y, z):
    return(x + y) * z

print(calculate('3', 'bar', 3))
print(calculate([5,3], [9,2], 3))
try:
    print(calculate([5,3], 9, 3))
except:
    print('we got error')