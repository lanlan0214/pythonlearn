import random

# for i in range(10):
#     print(random.randrange(10,20,3))

random.seed(6) # 有用seed的話 就會鎖住 種子

for i in range(5):
    print(random.randint(1,500))