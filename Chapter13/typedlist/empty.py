class TypedList(list):
    def __init__(self, example_element, initial_list):
        # 初始化 TypedList
        self.type = type(example_element)  # 記錄元素的類型
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)  # 檢查初始列表中的每個元素是否符合類型要求
        super().__init__(initial_list)

    def __check(self, element):
        # 私有方法，檢查單個元素是否符合類型要求
        if type(element) != self.type:
            raise TypeError(
                "Attempted to add an element of incorrect type to a TypedList.")

    def __setitem__(self, i, element):
        # 重寫 __setitem__ 方法，用於在設置元素時檢查類型
        self.__check(element)
        super().__setitem__(i, element)

    def __getitem__(self, i):
        # 重寫 __getitem__ 方法，用於取得元素
        return super().__getitem__(i)


# 使用 TypedList 創建兩個實例
x = TypedList('Hello', ['Some', 'original', 'stuff'])
print(x)

y = TypedList('', [''] * 5)
print(y)

# 將兩個實例相加
print(x + y)
