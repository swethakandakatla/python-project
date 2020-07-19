list_a = [1, 2, 3]
list_b = [2, 7]
list_res=[(i,j) for i in list_a for j in list_b if i!=j]
print(list_res)