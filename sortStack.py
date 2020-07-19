def createStack():
    stack1=[]
    return stack1

def ifStackisEmpty(stack1):
    return len(stack1)==0

def Push(stack1,item):   
    stack1.append(item)
    # print("item:",item)

def PoP(stack1):
    
    return stack1.pop()

def sortStack (stack1): 
    tmpStack = createStack() 
    while(ifStackisEmpty(stack1) == False): 
          
        # pop out the first element 
        tmp = Top(stack1) 
        
        PoP(stack1)
  
        # while temporary stack is not 
        # empty and top of stack is 
        # greater than temp 
        while(ifStackisEmpty(tmpStack) == False and
             int(Top(tmpStack)) > int(tmp)): 
              
            # pop from temporary stack and 
            # push it to the input stack 
            Push(stack1,Top(tmpStack)) 
            PoP(tmpStack) 
  
        # push temp in tempory of stack 
        Push(tmpStack,tmp) 
       
    return tmpStack 






def Top(stack1):

    return stack1[len(stack1)-1]

obj=createStack()
Push(obj,20)
Push(obj,30)
Push(obj,10)
Push(obj,50)
Push(obj,40)
print("Sorted numbers are: ") 
sortedst = sortStack(obj) 
print(sortedst) 

