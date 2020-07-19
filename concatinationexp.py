t1=('ABC','IS','BEST','FOR','ALL','PERSONS')
# print(t1)
n=len(t1)

t2=tuple(i+j for i, j in zip(t1,t1[1:]))

print(t2)



   