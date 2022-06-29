import re
from select import select
from datetime import date

class Student: ## First litter in class name has to be capital litter
    ###### Objects attriburtes
    ## Must take self as a parameter
    ## if we initialize the parameter it will be the default if user didn't enter it
    
    def __init__(self,name,age=0): # Constructor function --To initialize attribute  
        self.name = name
        self.age = age
    
    ########   Methods    
    # 1-instant method  must take self as a parameter to take acess to object attribute

    def info(self):
        print(f"My name is {self.name}.")
        print("My age is {}.".format(self.age))

    
    # 2- Class method
    ##Decorator بيخليني أعرف اعدل على التصرف بتاع الوظيفة بدون الدخول في التفاصيل
    ##  Could be consider as Second Constructor method
    @classmethod 
    def initFromBrithYear(cls, name,brithYear):
        return cls(name,date.today().year-brithYear)

    


class Pizza: ## First litter in class name has to be capital litter

    #### increasw constructor increases the facilities
    ### First constructor method
    def __init__(self,ingredients):
        self.ingredients = ingredients
    
    ### Second constructor method 
    @classmethod
    def veg(cls):
        return cls(['mushromms','olives','onions'])
    
    ### Third constructor method
    @classmethod
    def margherita(cls):
        return cls(['mozzarella','olives','sauce'])

    ## It dunder method exist in class but I can't see it 
    ## I will override it to print ingredients we write print(object)
    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}."

# student1= Student("Ahmed",22)
# student2= Student.initFromBrithYear("mohamed",2000)
# student2.info()

### Use different constructors to define different types of pizza
pizza1 = Pizza(['Tomatoes','olivers'])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()
# print(pizza2,pizza3)
### dunder or magic function
### dunder double under scoll__funName__
### This print all dunder function related with this class
### we will override the __str__ dunder method as line 46
# print(dir(pizza2))  

### Now This will print all ingredients of pizza 2 
print(pizza1)  
print(pizza2)
print(pizza3)  

