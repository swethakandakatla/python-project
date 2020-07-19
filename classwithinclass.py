class Student:

   def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno
       

   def getSchool(self):
      print(self.name, self.rollno)

   class Laptop:
      
       def __init__(self):
           self.brand='HP'
           self.cpu='i8'
           self.ram=8
       def show(self):
           print(self.brand, self.cpu, self.ram)
          

s1=Student('Samanvitha', 9)
s2=Student('Sriansha', 3)    

s1.getSchool()

lap1=Student.Laptop()
lap1.show()

print(id(lap1))