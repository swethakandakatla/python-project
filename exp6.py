l1=[4, 6, 7, 8, 9, 4, 6, 7]
l2=[1, 2, 3, 5]
l3=[]
l4=[]
# l1[1]=10
# print(l1)
# l1.remove(l1[1])
# print(l1)

l4=[]
l3=l1+l2
print(l3)
print(l4*5)
print(len(l1))
print(max(l1))
print(min(l1))
# print(cmp(l1,l2))
l1.append(11)
print(l1)
l2.insert(3,11)
print(l2)
print(l1.count(4))
l1.sort()
print(l1)
l1.extend(l2)
print(l1)
l1.remove(9)
print(l1)
print(l2.pop(4))
# print(l2)
l1.reverse()
print(l1)
l4=l1.copy()
print(l4)
print(sum(l1))
print(l1.index(6))
del l1[4]
print(l1)
