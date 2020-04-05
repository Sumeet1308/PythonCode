class A:
    def process(self):
        print ("This is class A statement")

class B(A):
    def process(self):
        print("This is class B statement")

a=B()
a.process()