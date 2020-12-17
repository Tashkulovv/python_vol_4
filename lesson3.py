# method range  v list
'''new_list =[]
empty_list=list()
list_ = [1,2,3,4,5,6,7,8,9]
print(list_[5])
print(len(list_))
dip = range(5, 30)
print(list(dip))
print(list_[2:6])'''
#append элементы в конец списка

 '''list_2 = [1,2,3,4,5]
list_2.append("gorilla")
print(list_2)
new_list=[4444, 888]
list_2.append(new_list)
print(list_2)
print(len(list_2))'''

# метод extend расширяет спиисоск другим списком
'''
list1 = ['u1', 'u2', 'u3']
list2 = ['der', 'qwerty', 'qwerty']
list3 = list1 + list2
list1.extend(list2)
print(list3)
print(list1)'''

# method insert получает 2 арг и добавляет в список поиндексно
'''cars = [ 'MB', 'BMW', "porshe"]
cars.insert(0, 'toyota')
print(cars)'''

# method remove удаляет элементы по значению
'''laptops = ['yghjk', 'ccccv', 'vccvm']
laptops.remove('vccvm')
print(laptops)
'''
# method pop вырезает последнии элемент, но можно передать индекс
'''laptops = ['acer', 'bin', 'hp', 'lenovo', 'mac']

abc = laptops.pop()
abc1 = laptops.pop(0)

print(laptops)
print(abc)

print(abc1)
abc3 = laptops.pop(0)
print(abc3)'''
#method index возвращает индекс элемента

'''laptops = ['a', 'b', 'c', 'd']


print(laptops.index('d'))'''

'''# method count
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 1, 2, 1, 1]
print(numbers.count(1))
'''

#method revers разворачивает список
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 1, 2, 1, 1]
numbers.reverse()
print(numbers)'''

#method sort сортирует по ключу
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 1, 2, 1, 1]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
laptops = ['acer', 'bin', 'hp', 'lenovo']
laptops.sort(key=len, reverse=True)
print(laptops)'''


# method copy копирует какой-то список
'''laptops = ['acer', 'bin', 'hp', 'lenovo']
print(laptops)
new_laptops = laptops.copy()
new_laptops [3] = "BMW"
print(new_laptops)

numbers = [1, 2, 3, 4, 5, [6, 7, 8, 9]]
numbers_2 = numbers.copy()
numbers_2[2] = 'six'
print(numbers)
print(numbers_2)'''

#method deepcopy
'''import copy
laptops = ['acer', 'bin', 'hp', 'lenovo']
print('Original', laptops)
new_laptops = copy.deepcopy(laptops)
print('copy', new_laptops)
new_laptops[2]= 'ERLAN'
print('Original', laptops)
print('copy', new_laptops)'''



#method clear очищает список


#method del удвлякт элемент по индексу
'''laptops = ['acer', 'bin', 'hp', 'lenovo', 'mac']
#laptops.clear()
del laptops[2]
print(laptops)
del laptops[3]
print(laptops)
'''

'''from datetime import datetime

print(datetime.now())'''
# срезы
'''list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_[0:5]) #срез
print(list_[1::2]) #четные
print(list_[::-1]) #обр порядок
print(list_[0 :: 2]) #нечтеные'''

#method tuples кортеж
'''
new_turple =('abc',)
print(type(new_turple))
print(dir(new_turple))
'''

'''list_ = [1, 2, 3, 4, 5, 6, 7, 8, 2,9]
print(list_.index(3))
print(list_.count(9))

nums = list(list_)
print(nums)
nums.clear()
nums= tuple(nums)
print(nums)'''