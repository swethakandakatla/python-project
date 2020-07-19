def gen_divison(nums):
   res=[]
   for i in range(0,nums+1):
      
       if(i%5==0 and i%7==0):
    
           res.append(i)
    #    elif i%7==0:
     
    #        res.append(i)
       else:
            pass
   yield res
       

result=gen_divison(int(input("enter the number:")))  
for n in result:     
    print(n)