class Point:

    def __init__(self, x, y):

        self.x = x

        self.y = y

class Rectangle:

    def __init__(self, p1, p2):

        self.p1 = p1

        self.p2 = p2

    def get_area(self):

        return abs(self.p1.x - self.p2.x)*abs(self.p1.y-self.p2.y)

    def get_perimeter(self):

        return 2 * abs(self.p1.x - self.p2.x) + 2 * abs(self.p1.y-self.p2.y)

    def is_square(self):

        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):

            return True

        else:

            return False

p1 = Point(1, 3)

p2 = Point(3, 1)

r1 = Rectangle(p1, p2)

print(r1.get_area())                    #4

print(r1.get_perimeter())          #8

print(r1.is_square())                   #True

p3 = Point(3, 7)

p4 = Point(6, 4)

r2 = Rectangle(p3, p4)

print(r2.get_area())                     #9

print(r2.get_perimeter())           #12

print(r2.is_square())                    #True


































