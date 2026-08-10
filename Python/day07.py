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


#### 添加和删除元素

```Python
items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)    # ['Python', 'Java', 'Go', 'Kotlin', 'Swift']
# 使用insert方法在列表指定索引位置插入元素
items.insert(2, 'SQL')
print(items)    # ['Python', 'Java', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定的元素
items.remove('Java')
print(items)    # ['Python', 'SQL', 'Go', 'Kotlin', 'Swift']
# 删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)
print(items)    # ['SQL', 'Go', 'Kotlin']

# 清空列表中的元素
items.clear()
print(items)    # []


#### 元素位置和次数

列表类型的`index`方法可以查找某个元素在列表中的索引位置；因为列表中允许有重复的元素，所以列表类型提供了`count`方法来统计一个元素在列表中出现的次数。请看下面的代码。

```Python
items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素的索引位置
print(items.index('Python'))       # 0
print(items.index('Python', 2))    # 5
# 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的
print(items.index('Java', 3))      # ValueError: 'Java' is not in list
```

再来看看下面这段代码。

```Python
items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素出现的次数
print(items.count('Python'))    # 2
print(items.count('Go'))        # 1
print(items.count('Swfit'))     # 0
```

#### 元素排序和反转

列表的`sort`操作可以实现列表元素的排序，而`reverse`操作可以实现元素的反转，代码如下所示。

```Python
items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']

# 排序
items.sort()
print(items)    # ['Go', 'Java', 'Kotlin', 'Python', 'Python']
# 反转
items.reverse()
print(items)    # ['Python', 'Python', 'Kotlin', 'Java', 'Go']
```

### 列表的生成式

在Python中，列表还可以通过一种特殊的字面量语法来创建，这种语法叫做生成式。我们给出两段代码，大家可以做一个对比，看看哪一种方式更加简单优雅。

通过`for`循环为空列表添加元素。

```Python
# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)
```

通过生成式创建列表。

```Python
# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']



### 嵌套的列表
scores = [[0] * 3] * 5
print(scores)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

看上去我们好像创建了一个`5 * 3`的嵌套列表，但实际上当我们录入第一个学生的第一门成绩后，你就会发现问题来了，我们看看下面代码的输出。

```Python
# 嵌套的列表需要多次索引操作才能获取元素
scores[0][0] = 95
print(scores)
# [[95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0]]
```

scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)
# [[95, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''
