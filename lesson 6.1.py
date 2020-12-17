        ### генераторы списков

'''
from datetime import datetime
start = datetime.now()
nums = [num for  num in range(2000000)]

finish = datetime.now()
start2 = datetime.now()

nums2 = []
for i in range(2000000):
    nums2.append(i)

finish2 = datetime.now()
print(finish - start)
print(finish2 - start2)'''

'''even = [num for num in range(50) if num % 2 == 1]
print(even)'''

'''my_f = lambda x, y: x+y

print(my_f(10, 10))
def add (x, y):
    return x +y
print(add(10, 10))'''

# map

'''list_ = [1,2,3,4,5,6,7,8,9]
def my_f(x):
    return  x**x

new_list = list(map(my_f, list_))
print(new_list)'''

'''text = 'i love python'
def myf(x):
    return x.upper()
text2 = list(map(myf, text))
print(text2)
text3 = ''.join(text2)
print(text3)'''

# функция filter() фильтрует

'''mixed = ['mak', 'mak', 'proso', 'mak', 'proso', 'mak', 'mak', 'mak']
my_filter = lambda x: x == 'mak'
zolushka = list(filter(my_filter, mixed))
print(zolushka)
print(len(zolushka))'''


# функция reduce()
'''from functools import reduce
nums = [x for x in range(2)]
lambda_f = lambda x, y: x**y
sum_all = reduce(lambda_f, nums)
print(sum_all)'''
# функция  zip
'''a = 'hello world'
b = [x for x in range(20)]
tuple_ = ('a', 'b', 'c', 'd', 'e')
izp_f = list(zip(a, b, tuple_))
print(izp_f)
tuple_ = tuple(zip(a, b))
print(tuple_)'''

