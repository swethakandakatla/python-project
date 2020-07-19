def Palindrom():
        str1= input("enter the value:")
        val=len(str1)/2
        print(str1[::-1])
        if str1==str1[::-1]:
            print("palindrom:"+str1)
        else:
            print("not palindrom")

    
        
str2=Palindrom()
