'''
#Python3 函数
函数是对功能相对独立且会重复使用的代码的封装*

1.定义一个函数
def max(a, b):
    if a > b:
        return a
    else:
        return b
 
a = 4
b = 5
print(max(a, b))

2.参数传递
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

3.参数
必需参数
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：
#可写函数说明
def printme( str )
:
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
printme()

关键字参数
用关键字参数允许函数调用时参数的顺序与声明时不一致
#可写函数说明
def printinfo( name, age )
:
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )

默认参数
调用函数时，如果没有传递参数，则会使用默认参数。带默认值的参数必须放在不带默认值的参数之后
#可写函数说明
def printinfo( name, age = 35 )
:
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )

不定长参数
函数能处理比当初声明时更多的参数。

 可写函数说明
def printinfo( arg1, *vartuple )
:
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
以上实例输出结果：
输出: 
70
(60, 50)

如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
def printinfo( arg1, *vartuple )
:
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple
:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
以上实例输出结果：
输出:
10
输出:
70
60
50

加了两个星号 ** 的参数会以字典的形式导入。
实例(Python 3.0+)
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, **vardict )
:
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
以上实例输出结果：
输出: 
1
{'a': 2, 'b': 3}
声明函数时，参数中星号 * 可以单独出现，例如:
def f(a,b,*,c):
    return a+b+c

`*args`并不能处理带参数名的参数
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10

4.匿名函数
Python 使用 lambda 来创建匿名函数。
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))



def myfunc(n)
:
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))


5.强制位置参数
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
以下使用方法是正确的:

f(10, 20, 30, d=40, e=50, f=60)
以下使用方法会发生错误:

f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式

如果函数中没有`return`语句，那么函数默认返回代表空值的`None`。

6.用模块管理函数

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

    
foo()    # 大家猜猜调用foo函数会输出什么
```

当然上面的这种情况我们很容易就能避免
`module1.py`

```Python
def foo():
    print('hello, world!')
```



`module2.py`

```Python
def foo():
    print('goodbye, world!')
```

`test.py`

```Python
import module1
import module2

# 用“模块名.函数名”的方式（完全限定名）调用函数，
module1.foo()    # hello, world!
module2.foo()    # goodbye, world!
```

在导入模块时，还可以使用`as`关键字对模块进行别名，这样我们可以使用更为简短的完全限定名。

`test.py`

```Python
import module1 as m1
import module2 as m2

m1.foo()    # hello, world!
m2.foo()    # goodbye, world!
```

上面的代码我们导入了定义函数的模块，我们也可以使用`from...import...`语法从模块中直接导入需要使用的函数，代码如下所示。

`test.py`

```Python
from module1 import foo

foo()    # hello, world!

from module2 import foo

foo()    # goodbye, world!
```

但是，如果我们如果从两个不同的模块中导入了同名的函数，后导入的函数会覆盖掉先前的导入
```Python
from module2 import foo
from module1 import foo

foo()    # hello, world!
```

如果想在上面的代码中同时使用来自两个模块中的`foo`函数也是有办法的，大家可能已经猜到了，还是用`as`关键字对导入的函数进行别名，代码如下所示。

`test.py`

```Python
from module1 import foo as f1
from module2 import foo as f2

f1()    # hello, world!
f2()    # goodbye, world!


| 函数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| `abs`   | 返回一个数的绝对值，例如：`abs(-1.3)`会返回`1.3`。           |
| `bin`   | 把一个整数转换成以`'0b'`开头的二进制字符串，例如：`bin(123)`会返回`'0b1111011'`。 |
| `chr`   | 将Unicode编码转换成对应的字符，例如：`chr(8364)`会返回`'€'`。 |
| `hex`   | 将一个整数转换成以`'0x'`开头的十六进制字符串，例如：`hex(123)`会返回`'0x7b'`。 |
| `input` | 从输入中读取一行，返回读到的字符串。                         |
| `len`   | 获取字符串、列表等的长度。                                   |
| `max`   | 返回多个参数或一个可迭代对象中的最大值，例如：`max(12, 95, 37)`会返回`95`。 |
| `min`   | 返回多个参数或一个可迭代对象中的最小值，例如：`min(12, 95, 37)`会返回`12`。 |
| `oct`   | 把一个整数转换成以`'0o'`开头的八进制字符串，例如：`oct(123)`会返回`'0o173'`。 |
| `open`  | 打开一个文件并返回文件对象。                                 |
| `ord`   | 将字符转换成对应的Unicode编码，例如：`ord('€')`会返回`8364`。 |
| `pow`   | 求幂运算，例如：`pow(2, 3)`会返回`8`；`pow(2, 0.5)`会返回`1.4142135623730951`。 |
| `print` | 打印输出。                                                   |
| `range` | 构造一个范围序列，例如：`range(100)`会产生`0`到`99`的整数序列。 |
| `round` | 按照指定的精度对数值进行四舍五入，例如：`round(1.23456, 4)`会返回`1.2346`。 |
| `sum`   | 对一个序列中的项从左到右进行求和运算，例如：`sum(range(1, 101))`会返回`5050`。 |
| `type`  | 返回对象的类型，例如：`type(10)`会返回`int`；而` type('hello')`会返回`str`。 |
'''


def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    # 返回num的阶乘（因变量）
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))