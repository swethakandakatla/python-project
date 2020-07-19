class Pycharm:
    def excute(self):
     print("compile")
     print("running")

class Laptop:
   def code(self, ide):
     ide.excute()

class visual:
     def excute(self):
      print("in this class")    
      print("compile")
      print("running")


ide=visual()   
l1=Laptop()
l1.code(ide)