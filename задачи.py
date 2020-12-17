#1
'''num1 = int(input('enter anumber1: '))
num2 = int(input('enter anumber2: '))
print(num1-num2)

#2
print(36%5)
'''
#3
'''word = input('введите слово: ')
if word[::-1] == word:
    print('слово является палиндромом')
else:
    print('слово не является палиндромом')'''


#4
'''word = 'I love JAVA'
print(word.replace('JAVA', 'Python'))'''

#5
'''name = input('enter your name: ')
print(name*10)'''

#6
'''text = input('введите текст: ')
print(text[::-1])
'''


#7
'''text = (input('введите число: '))
if len(text) >= 10:
    print(text[9])
elif len(text) < 10:
    num = 10 % len(text)
    print(text[num-1])'''



#8
'''
text = input('введите текст: ')
if len(text) > 2:
    print(text[0:2] + text[-2:])
elif len(text) == 2:
    print(text)
elif len(text) < 2:
    print('Error')
'''

#9
'''num = int(input('enter number: '))
print(int(num-1), int(num + 1))'''

#10
'''num1 = input('enter number1: ')
num2 = input('enter number2: ')
if num1.isalpha() or num2.isalpha():
    print('вы ввкли не число!')
elif num1 > num2:
    print(num1 + ' > ' + num2)
elif num1 == num2:
    print(num1 + ' = ' + num2)
elif num1 < num2:
    print(num1 + ' < ' + num2)
else:
    print('Error')'''
#11
'''while True:
    chislo = int(input('введите число: '))
    if chislo > 0:
        print('положительное')
    elif chislo < 0:
        print('отрицательное')
    elif chislo == 'stop':
        print('цикл остановлен')
        break
    elif chislo == 0:
        print('0')
    else:
        print('Error')'''