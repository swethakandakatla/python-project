class A:
    def __init__(self):
        print("init A class")
    def feature1(self):
        print("feature1 is here")
    def feature2(self):
        print("feature2 is here")
class B():
    def __init__(self):
        
        print("init B class")
    def feature3(self):
        print("feature3 is here")
    def feature4(self):
        print("feature4 is here")
class C(A, B):
    def __init__(self):
        print("init c class")
a1=C()
