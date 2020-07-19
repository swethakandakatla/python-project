import re
regex = '[+-]?[0-9]+\.[0-9]+'
def check(floatnum):  
   if(re.search(regex, floatnum)):  
        print("Floating point number")            
   else:        
          print("Not a Floating point number")  
floatnum="1.23"
check(floatnum)
      