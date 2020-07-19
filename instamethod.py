class Student:
    school="warangal public school"

    def __init__(self, m1, m2, m3):
          self.m1=m1
          self.m2=m2
          self.m3=m3

    def avg(self): 
      
       return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1   
    @classmethod
    def info(cls):
        return cls.school    

s1=Student(86,75,90)
s2=Student(55,66,77)   

print(Student.school)
print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(Student.info())
