#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
student=Student("Vasia", 23)
student.info()

#2
class Cirkle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * (self.radius ** 2)
cirkle=Cirkle(123)
print(cirkle.area())

#3
class Animals:
    pass
class Dog(Animals):
    def sound(self):
        print("Собака каже: Гав")
dogi = Dog()
dogi.sound()


#4
class BancAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self):
        if self.balance<0:
            print("Баланс від'ємний! Введіть баланс заново!!!")
        else:
            print(f"Баланс : {self.balance}, Власник: {self.owner}")
            a=float(input("Введіть річну ставку в відсотках: "))
            b=self.balance + (a / 100 * self.balance)
            if b < 0:
                print("Баланс став від'ємним!!!")
            else:
                print(f"Баланс : {b}")
                g=float(input("Введіть суму яку потрібно вилучити: "))
                j=b-g
                if j<0:
                    print("Занадто велика сума!!!")
                    return g
                else:
                    print(f"Баланс: {j}")
bancaccount=BancAccount(1000, 'Vitaliy')
bancaccount.deposit()

