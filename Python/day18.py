# 第19课：面向对象编程应用


# 案例1：扑克游戏

from enum import Enum

class Suite (Enum):
    SPADE,HEART,CLUB,DIAMOND=range(4)

for suite in Suite:
    print(f'{suite}:{suite.value}')

class Card:

     def __init__(self,suite,face):
         self.suite=suite
         self.face=face

     def __repr__(self):
         suites = '♠♥♣♦'
         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
         return f'{suites[self.suite.value]}{faces[self.face]}'

     def __lt__(self,other):
         if self.suite==other.suite:
            return self.face<other.face
         return self.suite.value<other.suite.value
     


card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)  

import random

class Poker:
    def __init__(self):
        self.cards=[Card(suite,face) for suite in Suite for face in range (1,14)]
        self.current=0

    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)

poker = Poker()
poker.shuffle()
print(poker.cards)   


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()



poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)


# 案例2：工资结算系统

#抽象类


from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass




class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

emps = [
    Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), 
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽'),
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')

