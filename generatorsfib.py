def genfib():
    a,b=0,1
    yield:a
    a,b=b,a+b

for n in genfib():
    if(n<20):
      print(n)