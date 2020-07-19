l1=[2,3,4,3,5,2,6,7,8,7,9]
n=len(l1)
for i in range(0,n-1):
  if(l1.count(l1[i]))>1:
     l1.remove(l1[i])
     print(l1[i])
  else:
    print(l1[i])