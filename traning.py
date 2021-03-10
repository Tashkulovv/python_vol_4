'''bambuk = 50
gus = 20
day = float(input('введите количество полных дней и часть неполного: '))
print(100 + day * bambuk - gus * int(day))
'''

from OOP.new1 import Rectangle

new = Rectangle(2, 3)
print(new.perimtr())

new1 = Rectangle(2, 5)
print(new1.perimtr())

x = new.perimtr() - new1.perimtr()
print(x)


