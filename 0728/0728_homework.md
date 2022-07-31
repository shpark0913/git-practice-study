1. class Circle:
   
       pi = 3.14
   
       def __init__(self, r, x, y):
   
           self.r = r
   
           self.x = x
   
           self.y = y
   
       def area(self):
   
           return Circle.pi * self.r * self.rS
   
       def circumference(self):
   
           return 2 * Circle.pi * self.r
   
       def center(self):
   
           return (self.x, self.y)
   
   c1 = Circle(3, 2, 4)
   
   print(c1.area())
   
   print(c1.circumference())

2. class Animal:
   
       def __init__(self, name):
   
           self.name = name
   
       def walk(self):
   
           print(f'{self.name}! 걷는다!')
   
       def eat(self):
   
           print(f'{self.name}! 먹는다!')
   
   class Dog(Animal):
   
       def run(self):
   
           print(f'{self.name}! 달린다!')
   
       def bark(self):
   
           print(f'{self.name}! 짖는다!')
   
   class Bird(Animal):
   
       def fly(self):
   
           print(f'{self.name}! 푸드덕!')
   
   dog = Dog('꼽이')
   
   bird = Bird('구구')
   
   dog.run()   #꼽이! 달린다!
   
   dog.bark()   #꼽이! 짖는다!
   
   bird.walk()   #구구! 걷는다!
   
   bird.eat()   #구구! 먹는다!
   
   bird.fly()   #구구! 푸드덕!

3. from fibo import fibo_recursion as recursion
