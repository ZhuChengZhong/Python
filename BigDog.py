from Dog import Dog

class BigDog(Dog):
    def __init__(self,name,age,size):
        super().__init__(name,age)
        self.size=4

    def info(self):
        super().introduce();
        print("size "+str(self.size))


bigDog=BigDog("xiao zhuang",18,600)
bigDog.info()
