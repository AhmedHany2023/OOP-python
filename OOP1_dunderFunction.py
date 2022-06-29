 ###Dunnder

class Man: 
    def __init__(self,name, age): 
        self.name =name
        self.age =age
    
    ## first dunnder excute when object + object
    def __add__(self,other): ### other or any parameter
        names = self.name+" and "+other.name
        ages = self.age+other.age
        return f"names combined are {names} and sum of ages is {ages} "
    
    ## first dunnder excute when object < object this is lessthan dunnder 
    def __lt__(self,other):
        return self.age <other.age  ### true false
        
    def info(self):  ## Same name but different behavior == overriding
        return f"Name is {self.name} and age is {self.age}."



man=Man("Islam",20)
man1=Man("Ahmed",25)

############### To regonize dunnder of the class
# print(dir(man)) 

##  This will give error if __add__ is not existed
##     Now this will excute the dunnder method of add 
print(man+man1) 

##  This will give error if __add__ is not existed
##     Now this will excute the dunnder method of add 
print(man<man1) 