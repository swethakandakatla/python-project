class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person('samanvitha','9')

sentence='my name is {0.name} and iam {0.age} years old.'.format(p1)
print(sentence)