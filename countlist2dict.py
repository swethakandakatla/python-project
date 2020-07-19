l1=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
n=len(l1)

m=1
dict={}
for i in range(0,n-1):
    if(l1[i]==l1[i+1]):
        
        h=l1.count(l1[i])        
        val=l1[i]
        
        dict[val]=h
   
    else:
        pass
  
print(sorted(dict.items()))