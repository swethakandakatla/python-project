l1=[-1, 2, -3, 5, 7, 8, 9, -10]

res = list(filter(lambda a:a<0,l1))
res_val=list(filter(lambda a:a>0,l1))
print(res+res_val)