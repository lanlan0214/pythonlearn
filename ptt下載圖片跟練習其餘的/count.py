from collections import Counter;
from collections import defaultdict

my_list = [1,2,3,1,2,3,4,5,6,1,2,3,4]
####################################################
letters = "aaaaaaaaaaabbbbbbbbbbbbbccccccccccaaaaaabdcdcccdddd"
####################################################
Harry = {
    "age" : 28,
    "name" : "FK"
}
#################################################### 這個類似下面這個方法很多人也是用lambda
Borther = defaultdict(lambda: "Wrong Key!!")
Borther["name"] = "test"
Borther["age"] = 20
print(Borther["pice"])
####################################################
def defaut_factory(): # 這是定義如果沒有這個值就輸入哪個東西 也可以是3或是字串
    return [1,2,3]
d = defaultdict(defaut_factory)
d["a"] = 1
d["b"] = 2
####################################################
f = Counter(letters)
####################################################
result = Counter(my_list)
####################################################
print(result) # 1出現3次 2出現3次 3出現3次 4出現2次 5出現1次 6出現1次
print(f.most_common()) #排順序了 most_common(2)這樣是要最常見的2個
print(d["a"], d["b"], d["c"])