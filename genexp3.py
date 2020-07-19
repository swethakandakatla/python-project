def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(next(x)) # In Python 3, _next_() 
print(next(x)) 
print(next(x)) 