from datetime import date

#### Inheritance and Polymorphism 
class Person: ### parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self): ## instant method
        return f"My name is {self.name} and my age is {self.age}"


    ### second constructor
    @classmethod
    def initFromBirthYear(cls,name,brithYear,extra="None"):
        return cls(name,date.today().year-brithYear,extra) ## extra in man is voice&&in woman is hair

## Now I want to do another class called man 
## and this class inherites from person
class Man(Person): ### Child class 
    ## class attributes
    gender ="Male"
    noOfMen = 0

    ## init function must take parameter of parent init
    def __init__(self,name, age, voice): 
        super().__init__(name,age)   ###كده بقوله إن دي الحاجات الي أنا هرثها
        self.voice = voice 
        Man.noOfMen+=1  ############# Must say  Man.class name because noOfMen is a class attribute
    
    ### This is polymorphism (overriding) because I have the same method 
    ### in the parent class person
    def info(self):  ## Same name but different behavior == overriding
        string = super().info()  ### To inherit this method from parent class
        return string + f" and voise is {self.voice} and genger is {self.gender}."


class Woman(Person): ### Child class for a parent class (Person)
    ## class attributes
    gender ="Female"
    noOfWomen = 0

    ## init function must take parameter of parent init
    def __init__(self,name, age, hair): 
        super().__init__(name,age)   ###كده بقوله إن دي الحاجات الي أنا هرثها
        self.hair = hair 
        Woman.noOfWomen+=1  ############# Must say  Man.class name because noOfMen is a class attribute
    
    ### This is polymorphism (overriding) because I have the same method 
    ### in the parent class person
    def info(self):  ## Same name but different behavior == overriding
        string = super().info()  ### To inherit this method from parent class
        return string + f" and her hair is {self.hair} and genger is {self.gender}."


###########   Using first Constructor
# man = Man("ahmed",25,"hard")
# print(man.info())
# print(Man.noOfMen)
# woman = Woman("fofa",48,"curly")
# print(woman.info())
# print(Woman.noOfWomen)

#############    Using Second Constructor
man = Man.initFromBirthYear("ahmed",1997,"hard")
print(man.info())
woman = Woman.initFromBirthYear("fofa",1974,"curly")
print(woman.info())

######################### To know if this object from this class or not   isinstant(obj,class)
### gives true or false
print(isinstance(woman,Woman))  ## This gives True
print(isinstance(woman,Man))    ## This gives False
print(isinstance(woman,Person)) ## This gives True cause the woman object from Woman class which inherites the Person class
print(isinstance(man,Person))   ## This gives True cause the man object from Man class which inherites the Person class