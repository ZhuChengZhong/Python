class Dog():

    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("my name is "+self.name+" and my age is " + str(self.age))


dog=Dog("xiao huang",13)
dog.introduce()

#print(dog.name.title())
#print(dog.age)
