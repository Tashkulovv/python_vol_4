#1
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
'''

#2
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a.extend(b)
a.sort()
print(a)'''
#3
'''dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}
new_dict = {'бежал': 'бежать в прошедшем времени',
                   'туфли': 'туфля во множественном числе'}
dictionary.update(new_dict)
print(dictionary)
'''
#4
'''numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 
           237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
for i in numbers:
    if i == 237:
        print('stop')
        break
        elif i % 2 == 0:
        print(i)
'''

#5
'''a = int(input('нижний диапозон: '))
b = int(input('верхний диапазон: '))
for i in range(a, b+1):

    i <= b
    print(i)
'''

#6
import math
'''a = int(input('нижний диапозон: '))
b = int(input('верхний диапазон: '))
for (i) in range(a, b):
    print()'''
#7
'''a = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
chet = 0
nechet = 0
for i in a:
    if i % 2 == 0:
        chet+=1
    elif i % 2 == 1:
        nechet += 1
print(f'количество четных: {chet}')
print(f'колтчество нечетных: {nechet}')'''


#8
'''
a = 10
b = 0
while b < a:
    print(str(b) * b)
    b+=1'''

#9
'''a = int(input('таблица умножения для числа: '))
b=1
while b <= 10:
    print(f'{a} * {b} = {a*b}')
    b+=1'''

#10
'''
a = int(input('минимум: '))
b = int(input('максимум: '))
c = int(input('шаг: '))
x = a
while x <= b:
    print(x)
    x +=c'''
#11
'''a = int(input('число: '))
i = 1
z = 1
f = 0
while f < a:
    sum = i + z
    i = z
    z = sum
    f+=1
    print(sum)'''

#12
'''num = int(input())
a = 1
b = 1
while b < num:
    b +=1
    a = a * b
print(a)'''