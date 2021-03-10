'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet_me(self):
        greeting = f'Hello! My name is {self.name}! I\'m {self.age} years old'
        print(greeting)

person = Person(input('name: '), input('age: '))

person2 = Person('Alice', 20)
person2.greet_me()
person.greet_me()
'''

class Vehicle:
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed

    def accelerate(self, x):
        self.speed += x
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self, x):
        self.speed -=x
        if self.speed < 0:
            self.speed = 0
    def print_status(self):
        print(f'скорость ТС равна {self.speed} км/ч')


class Motorcycle(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        self._front_tire_width = 95
        self._rear_tire_width = 95

    def set_tires_width(self, front, rear):
        self._rear_tire_width = rear
        self._front_tire_width = front
        print('на мотике была установлена новая резина')

    def tire_info(self):
        print(f'размер передней шины {self._front_tire_width}')
        print(f'размер задней шины { self._rear_tire_width}')


class Auto(Vehicle):
    def __init__(self, speed, max_speed):
        Vehicle.__init__(self, speed, max_speed)
        self._gear = 0
        self._color = 'серебро'

    def set_gear(self, gear):
        self._gear = gear
        Vehicle.print_status(self)
        print(f'авто переключен на скорость №{self._gear}')
        print(f'авто перекрашен в {self._color}')


    def set_color(self, color):
        self._color = color

    def print_status(self):

        Vehicle.print_status(self)
        print(f'авто переключен на скорость №{self._gear}')
        print(f'авто перекрашен в {self._color}')

    def get_color(self):
        return self._color



m = Motorcycle(40, 120)
m.print_status()
m.set_tires_width(90,100)
m.tire_info()

a = Auto(0,150)
a.accelerate(40)
a.set_gear(2)
a.print_status()
a.set_color('black')
color = a.get_color()
print(color)
