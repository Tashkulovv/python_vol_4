#1
'''i = 0
while i < 10:
    i+=1
    print(i)'''

#2
'''i = 0
while i < 20:
    i += 2
    print(i)'''
#3
'''
num = 7
i = 0
while num != i:
    i = int(input('введите число: '))
    if num == i:
        print('сим сим, откройся!')'''

#4
'''password = '000'
i = 0
while i < 3:
    i +=1
    user = input('Enter your password: ')
    if password != user:
        print('No')
    else:
        print('YES')
        break
    if i == 3:
        print('game over')
'''

#5
'''star = ' * '
chislo = int(input('введите число: '))
while chislo > 0:
    print(star*chislo)
    chislo -=1'''


#6
'''a =int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
kol = 0
for i in range(a, b):
    if i % c == 0:
        kol +=1
print(kol)'''

#7
'''spisok = []

while True:
    student = input('Your name: ')
    spisok.append(student)
    if student == 'exit':
        break
print(spisok)'''

#8
'''
age = int(input('input age: '))
i =0
x = 1
if age % 2 == 0:
    while i < age+1:
        i +=2
        print(i)
elif age % 2 == 1:
    while x < age+1:
        print(x)
        x +=2'''


#9
'''from math import pow
N = int(input('input N: '))
i = 0
while 2**i < N:
    i +=1
if 2**i > N:
    i -=1
    print(i)
else:
    print(i)'''

#10
'''
popytka =3
word = 'словарь'
print(f'у вас есть {popytka} попытки')
while popytka > 0:
    i = input('введите букву или слово: ')
    if i == word:
        print('ураа!!! WIN!!!')
        break

    if i in word:
        print(word.index(i))
    else:
        popytka -= 1
        print(f'у вас осталось {popytka} попытки')
'''


