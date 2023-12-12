
import time
from concurrent.futures import ThreadPoolExecutor

def test(n):
    for i in range(n):
        print(i, end=' ')
        time.sleep(0.2)

with ThreadPoolExecutor() as executor:    # 改用 with...as
    executor.map(test, [1,2,3,4])