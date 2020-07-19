def fibonacci():
    num1=0
    num2=1
    n=int(input("enter the number:"))
    for i in range(0,n):
         if i<n:
            num3=num1+num2
            num1=num2
            num2=num3
            print(num1,num2)   
         else:
            pass

fibonacci()