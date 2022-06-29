import re
from select import select

class Student: ## First litter in class name has to be capital litter
    ###### Class attriburtes must be intialize
    ###### Common between all objects
    __numOfStudent = 0

    ###### Objects attriburtes
    ## Must take self as a parameter
    ## if we initialize the parameter it will be the default if user didn't enter it
    
    ##  For Encapsulation we will make all attributes as private-- by replace
    ##     self.name    with   self.__name
    def __init__(self,name,age=0,courses='none'):
        # self.name = name
        # self.age = age
        # self.courses = courses
        ###  Private attributes
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.__numOfStudent+=1
    
    ########   Methods    
    # 1-instant method  must take self as a parameter to take acess to object attribute

    def info(self):
        ##  f  to use  {}
        print(f"my name is {self.__name}.")
        ## it equivlant to above
        print("my age is {}.".format(self.__age))
        print(f"my courses are {self.__courses}.")
    
    def is_old(self,num):
        if self.__age <=  num:
            print(f"{self.__name} is not an old")
        else:
            print(f"{self.__name} is an old")

    # 1.1-Getter and setter methods for encapsulation
    # Also it must take self as a parameter to take acess to object attribute
    def getName(self):
        return self.__name
    
    def setName(self,newName):
        self.__name = newName
    
    # 2- Class method
    ##Decorator بيخليني أعرف اعدل على التصرف بتاع الوظيفة بدون الدخول في التفاصيل
    ## it will be in OOP1_classmethod file
    # @classmethod  

    # 3- Static method
    ## it will be in OOP1_Staticmethod file
    # @staticmethod  

    




student1= Student("Ahmed")
## after edit for encaps this will add a new attrubite called name so it doesn't give error
student1.name="mohamed" ##acsess attribute, this is bad for encapsulation

student1.GPA = 3.73   ## This add attribute called GPA

student2= Student("said",23,['C','python'])

###############   Encapsulation
print(student1.GPA) ##This is bad for encapsulation
####### after put attributes as private it print a new attribute called for the above line
student1.info() ## name dosenot channge 

student2.setName("Sona")
print(student2.getName())
