def count():
    a = 1
    def cal(val):
        nonlocal a    # 宣告 a 為自由變數
        a = a + val
        return a
    return cal

test = count()
test(10)
test(11)
print(test(12))    # 34 ( 1 + 10 + 11 + 12 )

a = [[1,2],[4,3],[5,1],[9,2],[3,7]]
b = sorted(a, key = lambda x: x[1])
print(list(b))    # [[5, 1], [1, 2], [9, 2], [4, 3], [3, 7]]