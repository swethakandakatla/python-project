class Generator_divison():
    def gen_div(nums):
    # n=len(l1)
        my_num=[]
        for i in range(0,nums+1):
            if(i%7==0):
                my_num.append(i)
    #  print(my_num)
        yield my_num

 
result=Generator_divison.gen_div(int(input("enter the number:")))  
for res in result:
    if(res!=0):
        print(res) 
    else:
        pass
# print(next(result))
# print(next(result))
# print(next(result))
