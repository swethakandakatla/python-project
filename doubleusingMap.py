def doublenum(list_num):
    return list_num+list_num

num=[1, 5, 4, 6, 8, 11, 3, 12]   
double_num=map(doublenum,num)
print(list(double_num))
