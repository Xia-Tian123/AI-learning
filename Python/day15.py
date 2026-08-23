'''
#Python3 模块

import 语句
#!/usr/bin/python3
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return

#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")


以使用模块名称来访问函数：
实例
>>>fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> 
fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> 
fibo.__name__
'fibo'
如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
>>> fib = fibo.
fib
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377


给模块起别名
使用 as 关键字为模块或函数起别名：

import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root









__name__ 是一个内置变量，表示当前模块的名称。

当模块作为主程序运行时，__name__ 的值是 "__main__"。

当模块被导入时，__name__ 的值是模块的文件名。

使用 if __name__ == "__main__": 可以控制模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。


def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")


































'''