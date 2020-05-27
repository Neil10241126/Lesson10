import sys
import traceback

x = 10
y = int(input('請輸入數字:'))
try:
    z = x / y
except Exception as e: # Exception 抓出錯誤內容
    print('有錯誤發生', e)  # 列印 e 表示得到什麼錯誤內容
    print(e.__class__.__name__)  # 得到錯誤的型態
    print(e.args)
    cl, exc, tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]
    print(lastCallStack)
else:
    print(z)