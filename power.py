t1=(10,4,5,6)
t2=(5,6,7,5)
t3=()
l1=[]
n=len(t1)
for i in range(0,n):
    n=t2[i]
    t3=t1[i]**n
    l1.append(t3)
print(tuple(l1))     
      