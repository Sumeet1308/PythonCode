class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.lap=self.Laptop("HP","6GB")

    def show(self):
        print(self.name,self.id)
        self.lap.show()

    class Laptop:
        def __init__(self,make,ram):
            self.make=make
            self.ram=ram
        def show(self):
            print (self.make,self.ram)

s1=Student("Naveen",34)
s1.show()
s1.lap.show()

