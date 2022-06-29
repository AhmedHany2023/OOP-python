############################################################################
######## Link of Video :https://www.youtube.com/watch?v=A9kSngn7254     ####
############################################################################

# x= 5
# print(type(x))


class Student:  ## First litter in class name has to be capital litter
    ###### Class attriburtes must be intialize
    ###### Common between all objects
    numOfStudent = 0

    ###### Objects attriburtes
    ## Must take self as a parameter
    ## if we initialize the parameter it will be the default if user didn't enter it
    def __init__(self,name,age=0,courses='none'):
        self.name = name
        self.age = age
        self.courses = courses
        Student.numOfStudent+=1

    #self can replace with any name
    #like
    # def __init__(ff,name,age=0,courses='none'):
    #     ff.name = name
    #     ff.age = age
    #     ff.courses = courses
    #     Student.numOfStudent+=1

    ########   Methods
    
    # 1-instant method  must take self as a parameter to take acess to object attribute

    def info(self):
        ##  f  to use  {}
        print(f"my name is {self.name}.")
        ## it equivlant to above
        print("my age is {}.".format(self.age))
        print(f"my courses are {self.courses}.")
    
    def is_old(self,num):
        if self.age <=  num:
            print(f"{self.name} is not an old")
        else:
            print(f"{self.name} is an old")

    # 2-instant method  must take self as a parameter to take acess to object attribute




### must enter all parameter
# student1= Student("Ahmed",23,['C','python'])
# student2= Student("Ahmed",23,['C','python'])

### Although  they have same values but they are in different palces in a memory
# print(student1,student2) #print address in memory of 2 objects
# print(id(student1),id(student2))  #print an id address in a memory of 2 objects



## If we put default value, doesnot matter if not enter value
student1= Student("Ahmed")
student1.name="mohamed" ##acsess attribute, this is bad for encapsulation

student2= Student("Ahmed",23,['C','python'])

print(student1.name,student1.age,student1.courses)
print(student2.name,student2.age,student2.courses)

##class attrubites are common for all objects
print(Student.numOfStudent,student2.numOfStudent,student1.numOfStudent)

student2.info()
student2.is_old(40)


###############   Encapsulation
print(student1.name) ##This is bad for encapsulation

### Encapsulation will be in OOP1_Encapsulation file