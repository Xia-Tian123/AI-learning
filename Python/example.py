"""print('两数相加之和是%.1f'%(float(input('第一个数为'))+float(input('第二个数为'))))

import cmath
num=int(input('输入'))
sq=cmath.sqrt(num)
print('{0}的平方根为{1:3f}+{2:3f}'.format(num,sq.real,sq.imag))

import math
import cmath
def solve(a,b,c):
    if a==0:
        if b==0:
            return "无解"if c!=0 else "方程有多个解"
        return f"解为x={-c/b}"
    d=b**2-4*a*c
    if d>0:
        r1=(-b-math.sqrt(d))/2*a
        r2=(-b+math.sqrt(d))/2*a
        return f"方程有两个实数解{r1},{r2}"
    elif d==0:
        root=-b/(2*a)
        return f"一个{root}"
    else:
        r1 = (-b + cmath.sqrt(d)) / (2 * a)
        r2 = (-b - cmath.sqrt(d)) / (2 * a)
        return f"两个复数根x1 = {r1}, x2 = {r2}"

a, b, c = 1, -3, 2
result = solve(a, b, c)
print(result)

num=int(input("shuru"))
if num%2 ==0:
    print('{0}是偶数'.format(num))
else:
    print('{0}是奇数'.format(num))"""


a, b = 0, 1
for _ in range(20):
     print(a)
     a, b = b, a + b