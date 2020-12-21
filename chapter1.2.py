#1
'''a = [1, 2, 2, 4, 11, 2, 3, 1]

print(set(a))'''
#2

'''a = ['John', 'Anna',  'Raychel' , 'Katarina', 'Marko', 'Tom']
b = a.pop(5)
b= a.pop(1)
b = a.pop(0)
print(a)
'''
#3

'''list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_.reverse()
print(list_)'''

#4

'''a = [ 'John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom' ]

a.insert(1, 'Siymyk')
print(a)'''

#5

'''word = input('введите слова: ').split()
word.sort(key = len)
print(word)
'''
#6

'''b = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
key = input('введите ключ: ')
if key in b:
    print('ключ существует')
else:
    print('такого ключа нет')'''

#7
'''a = dict(UA = 'Kiev', BY = 'Minsk', UZ = 'Tashkent' )
b = dict(RUS = 'Moscow', KG = 'Bishkek', GB = 'London')
z = {**a, **b}
print(z)
print(len(z))'''

#8

'''a = dict(UA = 'Kiev',RUS = 'Moscow', KG = 'Bishkek', GB = 'London', BY = 'Minsk', UZ = 'Tashkent' )
print(a.keys())'''

#9
'''dict_ = { 'key1': 123}
a = len(dict_)
if len(dict_) == 0:
    print('словарь пуст')
else:
    print('словарь не пуст, в словаре ' + str( a ) + ' keys')'''

#10

'''a = [ 'John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom' ]
a.append('Siymyk')
a.append('Beka')
a.append('Tashkulov')
a = tuple(a)
print(a)'''

#11
'''try:
    login_ = dict(abc = '996')  # логин и пароль
    a = input('введите логин: ')
    b = input('введите пароль: ')
    if login_[a]:
        if login_.setdefault(a) == b:
            print('логин и пароль введены верно')
        else:
            print('error')
except Exception as ex:
    print('неверный логин или пароль')'''

#12
'''
sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word = input('введите букву: ')
if word in sogl:
    print(f'{word} согласная')
elif word in glas:
    print(f'{word} гласная')
else: 
    print("это звук")'''

#13
'''
apple = int(input('количкство яблок: '))
stud = int(input('количество студентов: '))
a = apple//stud
b = apple%stud
if stud > apple:
    print('яблоки остались в корзине')
else:
    print(f'каждый получит по {a} яблок, а в корзине останется {b} яблок')'''

#14
'''
import math
pupil = int(input('количество учеников: '))
part = math.ceil(pupil/2)
print(f'{part} парт нужно купить')'''

#15
'''
age = int(input('введите возраст собаки: '))
size = int(input('размер: 1 - маленькая, 2 - средняя, 3 - большая: '))
if size == 1:
    print(f'возраст вашей собаки {age*9} лет')
elif size == 2:
    print(f'возраст вашей собаки {age*10.5} лет')
elif size == 3:
    print(f'возраст вашей собаки {age*12.5} лет')
'''
#16

'''a, b, c = input().split()
if int(a) > 10 and int(b) > 10 and int(c) > 10:
    print('YES')
else:
    print('NO')
    '''
# 17
'''
a1 = int(input('enter 1: '))
a2 = int(input('enter 2: '))
a3 = int(input('enter 3: '))
print('количество положительных чисел: ', (a1 > 0) + (a2 > 0) + (a3 > 0))'''

#18
'''num = int(input('введите число: '))
step = int(input('введите степень: '))
if num < 100:
    rezult = num ** step
    print(rezult)
else:
    print('Введенное вами число > 100')'''

#19
a = int(input())
b = int(input())
c = int(input())
m = a
if m < b:
    m = b
    if m < c:
        m = c
print(m)

#20

'''a = int(input())
b = int(input())
c = int(input())
if b < a < c or b > a > c:
    print(a)
elif a < b < c or a > b > c:
    print(b)
else:
    print(c)
'''