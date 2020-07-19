t1=[(),(),('',),('a','b'),('a','b','c'),('d')]
n=t1.count(())
print(n)
for i in range(0,n):
  if () in t1:
    t1.remove(())
    
    
print(t1)