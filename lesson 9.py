'''class User:
    def __init__(self, name):
        self.name = name
        print(f'появился новый пользователь с именем {self.name}')


first_user = User('Siymyk')
second_user = User('Bermet')'''

'''class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        print('Появился новый питомец ')
    def __str__(self):
        text = f"объект класса Pet с именем {self.name}, {self.type}"
        return text

    def talk(self, sound):
        print(sound)

bobik = Pet('Bobik', 'dog')
bobik.talk('gav gav')
barsik = Pet('barsik', 'Cat')
barsik.talk('meow')
print(barsik)
bobik.type = 'Cat'
print(bobik)'''

#И Н К А П С У Л Я Ц И Я
'''class A:
    def _private(self):
        print('это закрытый метод')

a = A()
a._private()
class B:
    def __private(self):
        print('это защищенный метод')
    def __str__(self):
        return f'chfewf{self.__private}'
b = B()
print(b)'''

# Н А С Л Е Д О В А Н И Е
'''class Dog:
    def __init__(self, name):
        self.name = name
        print('сработал констуктор в классе Dog')


class Doberman(Dog):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('сработал констуктор в классе Doberman')

    def talk(self, sound='wow'):
        print(sound)

dog1 = Doberman('Doggg', 2)
dog1.talk()'''


class Table:
    def __init__(self, l=1, w=2, h=1):
        self.l = l
        self.w = w
        self.h = h


class KitchenTable(Table):
    def set_place(self, p):
        Table.__init__(self, l=1, w=2, h=1)
        self.places = p


class DeskTable(Table):
    def square(self):
        return self.w * self.l


t1 = KitchenTable(1, 1, 1.5)
t2 = DeskTable(1.5, 0.8, 0.75)
t3 = KitchenTable(1, 1.2, 0.8)
t4 = Table(1, 1, 0.5)
print(t2.square())


class ComputerTable(DeskTable):
    def square(self, e):
        # return  self.w * self.l - e
        return DeskTable.square(self) - e


ct = ComputerTable(2, 1, 1)
print(ct.square(0.3))
