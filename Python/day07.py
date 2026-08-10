'''
#列表

访问数值
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])

更新列表
list = ['Google', 'Runoob', 1997, 2000]
list[2] = 2001
list1.append('Baidu')

删除列表
del list[2]

len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代

函数
len(list)
列表元素个数

max(list)
返回列表元素最大值

min(list)
返回列表元素最小值

list(seq)
将元组转换为列表

list.append(obj)
在列表末尾添加新的对象

list.count(obj)
统计某个元素在列表中出现的次数

list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

list.index(obj)
从列表中找出某个值第一个匹配项的索引位置

list.insert(index, obj)
将对象插入列表

list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

list.remove(obj)
移除列表中某个值的第一个匹配项

list.reverse()
反向列表中元素

list.sort( key=None, reverse=False)
对原列表进行排序

list.clear()
清空列表

list.copy()
复制列表


items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
items3 = items1 + items2
print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]

# 列表的重复
items4 = ['hello'] * 3
print(items4)    # ['hello', 'hello', 'hello']

# 列表的成员运算
print(100 in items3)        # False
print('hello' in items4)    # True

# 获取列表的长度(元素个数)
size = len(items3)
print(size)                 # 9

# 列表的索引
print(items3[0], items3[-size])        # 35 35
items3[-1] = 100
print(items3[size - 1], items3[-1])    # 100 100

# 列表的切片
print(items3[:5])          # [35, 12, 99, 68, 55]
print(items3[4:])          # [55, 87, 45, 8, 100]
print(items3[-5:-7:-1])    # [55, 68]
print(items3[::-2])        # [100, 45, 55, 99, 35]

# 列表的比较运算
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)    # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)    # True

#### 列表元素的遍历

如果想逐个取出列表中的元素，可以使用`for`循环的，有以下两种做法。

方法一：
items = ['Python', 'Java', 'Go', 'Kotlin']

for index in range(len(items)):
    print(items[index])
```

方法二：
items = ['Python', 'Java', 'Go', 'Kotlin']

for item in items:
    print(item)
```

#计算扔的骰子点数
import random
counters = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

'''

import random
counter = [0]*6
for _ in range(6000):
    face = random.randint(1,6)
    counter[face-1]+=1
for face in range(1,7):
    print(f'{face}点出现了{counter[face - 1]}次')