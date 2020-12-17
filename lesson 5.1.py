# циклы
'''x = 0
for i in range(20):
    x += 1
    print('Python', x)'''

'''import time
numbers = []
for number in range( 0,45, 2):
    numbers.append(number)
    print(number)
    time.sleep(0.2)
print(numbers)'''

# range (начало, конец, шаг)
'''import time
text = 'i love python'
for i in text:

    print(i.upper())
    time.sleep(0.3)'''

'''for i in range(50)
    if i % 2 == 0:
        print(i)'''
# while
'''b = 0
while i  in range :

    print(b)
    b += 2'''

'''total = 100
i = 0
while i < 5:
    n = int(input('input number: '))
    total -= n
    i +=1
print('Осталось:', total)'''


'''i = 0
while i < 20:
    print('тестовая строка')
    i += 1
    if i == 10:
        continue
    print('continue не сработало')
    if i == 18:
        print("break")
        break'''

# функция def
#функция без параметров
'''def hello():
    print('hello')

hello()'''

# def
"""name = input('input your name: ')
def hello(name):
    print(f"hello, {name}")
hello(name)"""

'''def add (x, y):
    return  x + y
print(add(100, 43))'''

'''name = 'siymyk'
def my_func()
    print(name)
my_func()'''

'''def my_func():
    name = 'Siymyk'
    print('print in func ' + name)
my_func()
print(name)'''

'''def my_func(x, y):
    z = x**y
    return  z
var = my_func(2, 3)
print(var)'''

'''num = 2222
def my_func():
    num = 111
    print(num)
num = my_func()
print(num)
my_func()
my_func()'''

'''def add2(*args):
    result = 0
    for i in args:
        result +=1
    return result

nums = [1,2,3,4,5,6,7,8,9]
print(add2(nums))'''

'''def my_func(x, y, z =10):
    return  x + y+ z
print(my_func(1,2,123))
var = 'hello'
print(var, var, sep = '______')'''

'''def my_func(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} is {value}")


my_func(
    firstname = 'John',
    lastname = 'Wood',
    age = 19)'''

# рекурсия
'''import time
def fun():
    print("у попа была собака, он ее любил")
    print('она сьела кусок мяса, он ее убил')
    print("в землю закопал и надпись написал")
    time.sleep(0.3)
    fun()
fun()'''