#函数的应用
'''
#### 案例1 设计一个生成验证码的函数。

验证码由数字和英文大小写字母构成，长度可以用参数指定。

import random
import string
ALL_CHARS = string.digits + string.ascii_letters
def generate_code(code_len=4):
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
```

可以用下面的代码生成10组随机验证码来测试上面的函数。

```Python
for _ in range(10):
    print(generate_code()) //如果这里面没有括号就会打印函数本身
```

> **说明**：`random`模块的`sample`和`choices`函数都可以实现随机抽样，`sample`实现无放回抽样，这意味着抽样取出的字符是不重复的；
`choices`实现有放回抽样，这意味着可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，而参数`k`代表抽样的数量。



案例3：写一个判断给定的正整数是不是质数的函数。

```Python
def is_prime(num: int) -> bool:
    """判断一个正整数是不是质数

    :param num: 正整数
    :return: 如果是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num != 1

案例4：写出计算两个正整数最大公约数和最小公倍数的函数。

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)

案例5：写出计算一组样本数据描述性统计信息的函数。

```Python
import math


def ptp(data):
    """求极差（全距）"""
    return max(data) - min(data)


def average(data):
    """求均值"""
    return sum(data) / len(data)


def variance(data):
    """求方差"""
    x_bar = average(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - 1)


def standard_deviation(data):
    """求标准差"""
    return math.sqrt(variance(data))


def median(data):
    """找中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return average(temp[size // 2 - 1:size // 2 + 1])


'''


'''
调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            result = op(result, arg)
    for value in kwargs.values():
        if type(value) in (int, float):
            result = op(result, value)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))    # 120


def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]
```

当然，要完成上面代码的功能，也可以使用列表生成式，列表生成式的做法更为简单优雅。

```Python
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)    # [144, 64, 3600, 2704]
'''

### Lambda函数
'''
import operator, functools

# 一行代码定义求阶乘的函数
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(10))        # 3628800
print(is_prime(9))    # False
```

> **提示1**：上面使用的`reduce`函数是Python标准库`functools`模块中的函数，它可以实现对数据的归约操作，
通常情况下，**过滤**（filter）、**映射**（map）和**归约**（reduce）是处理数据中非常关键的三个步骤，而Python的标准库也提供了对这三个操作的支持。
>
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

from functools import reduce
 
numbers = [1, 2, 3, 4, 5]
 
# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)
 
print(product)  # 输出：120


> **提示2**：上面使用的`all`函数是Python内置函数，如果传入的序列中所有布尔值都是`True`，`all`函数就返回`True`，否则`all`函数就返回`False`。
'''
