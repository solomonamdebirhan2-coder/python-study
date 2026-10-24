#oop in python 
class student:
    def __init__(self, name , age, gpa, sex):
        self.name=name
        self.age=age
        self.gpa=gpa
        self.sex=sex
    def great(self):
        print('hello  my name si ' , + self.name)

student1 = student('solomon' , 21 , 3.9 ,"male")
student2= student("samson", 22 ,3.4 ,"male")
student3 =student(input('enter your name: ') ,float(input("enter your age: ")),float(input('enter your gpa: ')), input('enter yor sex: '))
print(student3.name)
print(student3.age)
print(student3.gpa)
print(student3.sex)
print(student1.name)
print(student1.age)
print(student1.gpa)
print(student1.sex)
print(student2.name)
print(student2.age)
print(student2.gpa)
print(student2.sex)
#
class bankaccaunt:
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance

    def dposit(self , amount):
        self.balance += amount
        print(f'dposited amount is {amount} and the curent balance is {self.balance} ')

    def wathdraw(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'the wathdraw amout is {amount} and the curent balance is {self.balance}')
        else:
            print("you have no seficent balance")

acc1=bankaccaunt('solomon amdebirhan' ,250000)
acc2=bankaccaunt("selamawiat" , 20000)

acc1.dposit(300000)
acc1.wathdraw(400000)
acc2.dposit(20000)
acc2.wathdraw(60000000)
#
class car:
    def __init__(self , model , calor , man_date, speed ):
        self.model = model
        self.calor = calor
        self.man_date = man_date
        self.speed = speed

    
    def move (self):
        return f'the {self.model} a {self.calor} and {self.man_date} is moving in speed of{self.speed}'
    
    
    def stop(self):
         return f'the {self.model} a {self.car} and {self.man_date} is stoppd'


car1=car('tyoota', 'red', 1998, '45 m/s')
car1.move()
# claas variable
class Student:

    class_year=2018
    gc_year=2021
    num_student = 0
    def __init__(self, name , age , GPA, sex):
        self.name = name
        self.age = age 
        self.GPA =GPA
        self.sex = sex
        Student.num_student += 1

student1 = Student('solomon' , 21 , 3.7 , ' male')
student2 = Student(' selam' , 20 , 3.5 , ' female')
student3 = Student('seti' , 22 , 3 , 'male')
print(student1.name)
print(student1.age)
print(student1.GPA)
print(student1.sex)
print(student1.class_year)
print(student1.gc_year)
print(student2.name)
print(student2.age)
print(student2.GPA)
print(student2.sex)
print(student2.class_year)
print(student2.gc_year)
print(student3.name)
print(student3.age)
print(student3.GPA)
print(student3.sex)
print(student3.class_year)
print(student3.gc_year)


print(f' the total number of student is {Student.num_student} ')

class Animal:
    def __init__(self ,name ):
        self.name = name
        self.is_aleave=True
    def eat(self):
        return f'{self.name} is eating'
    def slep(self):
        return f' {self.name} is sleeping'
    def move(self):
        return f'{self.name} is moving '
class cat(Animal):
    pass

class dog(Animal):
    pass

class musse(Animal):
    pass

dog = dog('shasho')
cat = cat('wuro')
musse=  musse('korach')
print(dog.name)
dog.eat()
dog.slep()
dog.move()
print(cat.name)
cat.slep()
 
class Car:
      def __init__(self, brand, model):
          self.brand = brand
          self.model = model

      def move(self):
          print(f"{self.brand} is Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(f"{self.brand} is Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(f"{self.brand} is Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
   
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

#
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
x.move()
