###########3
#### 4-Abstruction 
### Python doesnot support abstraction by it self so I will import a library

from abc import ABC, abstractmethod

class Shape(ABC): ##from abc library
    @abstractmethod ##abstract method from abc library
    def area(Self):
        pass

    @abstractmethod
    def perimeter(Self):
        pass
    
class Square(Shape):  ## Child class for the parent class Shape
    def __init__(self,side):
        self.__side= side
    
    ### It is an abstracte but I redefine it for each child
    def area(self):  ##polymorphism overriding
        return self.__side**2

    def perimeter(self):
        return self.__side*4

class Rect(Shape):  ## Child class for the parent class Shape
    def __init__(self,lenght,width):
        self.__lenght= lenght
        self.__width= width

    def area(self):  ##polymorphism overriding
        return self.__lenght*self.__width

    def perimeter(self):
        return (self.__lenght+self.__width)*2

squre =Square(10)
print(f"- Square area is {squre.area()} and perimeter is {squre.perimeter()}.")
rect =Rect(5,3)
print(f"- Rectangular area is {rect.area()} and perimeter is {rect.perimeter()}.")
