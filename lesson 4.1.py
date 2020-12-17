 # set - множества
'''new_set = {1,2,4,5,1,9, 9,4,3,2,3,4,5,6,6,4,1,2,2,3,4,5}
print(new_set)
new_list = [1,2,4,5,1,1,2,2,3,4,5]
print(new_list)
new_list = set(new_list)
print(new_list)'''

# method addпринимает один аргкмент, который может
 # method apdate принимает один арг - множество, и добавляет все его элементы к исходному множесвту
'''a_set = {1,2}
a_set.add(4)
a_set.add('4')
print(a_set)

b_set = {5,6,7,8}
a_set.update(b_set)
print(a_set)
#method remove
a_set.remove(1)
print(a_set)

#methpd discerd
a_set.discard(2)
print(a_set)'''

#method pop, method clear()



'''a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76}
b_set ={ 1, 2, 195, 8, 4, 12, 76, 54, 34, 32, 23,77 , 99}
a_set.union(b_set) #union возвращает однаковые значения

print(a_set.union(b_set))
'''

# method intersection() (пересечение ) возвращает новне иножество, содержащее все эдементы, которые есть и в первом и во втором
'''
set_1 = {1,2,3,4,5,6,7,8,9}
set_2 = {2,4,6,8,222,333,444}
#set_3 = set_1.intersection(set_2)
#print(set_3)
print(set_1.union(set_2))        # сложение только один жезнмпляр
print(set_1.intersection(set_2))   #пересечение
print(set_1.difference(set_2))     #разность множества (вычитает одно из другого)
print(set_1.symmetric_difference(set_2))    #симметричная разность
# method symmetric_difference() (симметрическая разность ) возвращает новое множнство,
# которое содержит только уникальные элементы обоих множеств

'''



# boolean
'''x = True
y = False

if 1>0:
    print(True)
elif 2<0:
    print(False)        
else:
    print('сработал блок else')
   
== сравнение  
 != отрицание
 >  меньще
 < большк
 =>  больше или равно
 <=  ментше или равно
 and    и
 or    или
 not    не'''
'''point = input('enter your point: ')
if point == '5':
    print('molodec')
elif point == '4':
    print('ty molodec no ne do konca')
elif point == '3':
    print('staraysa')
else:
    print(' Ty lox')'''

'''
list_ = [1, 2, 3, 4, 5]
num = int(input('enter a number: '))
if num not in list_:

    print('такого числа нет')
else:
    print("есть такое число")'''

'''
import math
while True:

    num1 = int(input('введите первое число: '))
    num2 = int(input('введите второе число: '))
    oper = input('Ввкдите + - * / ')
    if oper == '+':
        print(num1+num2)
    elif oper == '-':
        print(num1-num2)
    elif oper == '*':
        print(num1*num2)
    elif oper == '/':
        print(num1/num2)
    elif oper == 'stop':
        print('цикл остановлен')
        break
    else:
        print('ошибка оператора')
'''
