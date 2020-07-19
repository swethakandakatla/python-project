
t1=(11,22)
l1=['swetha','swetha', t1, 23, 23, 23]
n=len(l1)
for i in range(0,n):
    # print(i)
    if type(i)==tuple:
        break
    else:
        var=l1.count(l1[i])
        
print(var)
   