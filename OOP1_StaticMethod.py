
##  3- Static method   called utility method or helper method
##     doesnot take self or class(cls) as a parameter
##    بتجمع الكود بشكل أفضل

#####   Example 1
#########################################################

class Math:  ## First litter in class name has to be capital litter
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    @staticmethod
    def PI():
        return 3.14

# x = Math.add(5,10)
# y = Math.add5(x)
# z = Math.add10(y)
# print(x,y,z)
#####*****************************************



#####   Example 2
#########################################################
class Pizza: ## First litter in class name has to be capital litter
    def __init__(self,radius,ingredients):
        self.ingredients = ingredients
        self.radius = radius

    ## It is adunder method exist in class but I can't see it 
    ## I will override it to print ingredients we write print(object)
    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}."
    
    def area(self): # instant method
        return Pizza.circleArea(self.radius)

    @staticmethod
    def circleArea(r):
        return r**2 *Math.PI()
    

# pizza1 = Pizza(6,['Mozzarella','Tomatoes'])
# print(pizza1.area())  ## instant method
# ## static mathed Using function regardelss class
# print(Pizza.circleArea(4)) ## doesn't effect by attribute and method of class
 
#####*****************************************


#####   Example 3
#########################################################

class Dates:  ## First litter in class name has to be capital litter
    def __init__(self,date):
        self.__date =date   ## __data is a private attribute
    
    def getDate(self):
        return self.__date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)  ##static method called by class name

if(date.getDate()==dateWithDash):
    print("Equal")
else:
    print("unequal")

     
#####*****************************************
