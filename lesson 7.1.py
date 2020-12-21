'''file = open('text.txt', 'w')
file.write('hello world')
file.close()'''
'''
with open('text.txt', 'a') as f:
    text = f.read(11)
    print(f)
    f.write('\npython')'''

'''with open('new_file.txt', 'w') as file:
    for i in range(20):
        file.write('pthon\n')

with open('new_file.txt', 'r') as file:
    for line in file:
        line = file.readline()
        print(line.replace('\n', ''))'''

'''try:
    x = 100 / 0
    print(x)
except Exception as ex:
    print(ex)
print("а код работает")'''

'''x = 10 / 0
print(x)'''


'''def add_lines_to_file():
    file = open('1.txt', 'w')
    nums1 = [i for i in range(25)]
    for i in nums1:
        file.write(str(i) + '\n')
file = open('1.txt', 'r')
nums = []
try:
    for line in file:
        nums.append(int(line))
except ValueError:
    print('это не число!')
else:
    print('все хорошо')
finally:
    file.close()
    print('я закрыл файл')
print(nums)'''


import random
'''a = [random.randint(1, 1000) for i in range(1000)]
#a.sort()
#print(a)
print(sorted(a))
print(a)

x = random.randint(1, 100)
print(x)'''

'''x = random.randrange(999, 1000)
print(x)

y = random.random()
print(y)'''

list_ = ['орел', 'решка']
print(random.choice(list_))
