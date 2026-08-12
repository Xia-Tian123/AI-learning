'''
#元组tuple
# Python 的元组与列表类似，不同之处在于元组的元素不能修改

组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
实例(Python 3.0+)
>>> tup1 = (50)
>>> type(tup1)     # 不加逗号，类型为整型
<class 'int'>

>>> tup1 = (50,)
>>> type(tup1)     # 加上逗号，类型为元组
<class 'tuple'>

修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup3 = tup1 + tup2

组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup

重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象

len((1, 2, 3))
3	计算元素个数

print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>变量类型

>>> a = (1, 2, 3)
>>> b = (4, 5, 6)
>>> c = a+b
>>> c
(1, 2, 3, 4, 5, 6)
连接，c 就是一个新的元组，它包含了 a 和 b 中的所有元素。

>>> a = (1, 2, 3)
>>> b = (4, 5, 6)
>>> a += b
>>> a
(1, 2, 3, 4, 5, 6)
连接，a 就变成了一个新的元组，它包含了 a 和 b 中的所有元素。

('Hi!',) * 4
('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制

3 in (1, 2, 3)
True	
元素是否存在


# 循环遍历元组中的元素
for member in t2:
    print(member)


#### 例子1：打包和解包操作
# 打包
a = 1, 10, 100
print(type(a), a)    # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k = a
print(i, j, k)       # 1 10 100
星号表达式
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)          # 1 10 [100, 1000]
用range也可以
a, b, *c = range(1, 10)
print(a, b, c)

#### 例子2：交换两个变量的值
a, b = b, a

Python中的元组和列表是可以相互转换的，我们可以通过下面的代码来做到。

 ```Python
# 将元组转换成列表
 info = ('骆昊', 175, True, '四川成都')
 print(list(info))       # ['骆昊', 175, True, '四川成都']
# 将列表转换成元组
fruits = ['apple', 'banana', 'orange']
print(tuple(fruits))    # ('apple', 'banana', 'orange')
'''






'''
print`函数中的`end=''`表示输出后不换行














































'''