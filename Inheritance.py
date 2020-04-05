class A:
    def __init__(self):
        print ("Hello A")

    def feature1(self):
        print ("Feature 1")

class B(A):
    def __init__(self):
        super().__init__()
        print ("Hello B")

    def feature2(self):
        print("Feature 2")

a1=B()
a1.feature2()
