#!/usr/bin/python3

class Square:
        
    def init(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Calculate the area of the square"""
        return self.width * self.width

    def perimeter(self):
        """Calculate the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def str(self):
        return "{}/{}".format(self.width, self.height)

if name == "main":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())i
