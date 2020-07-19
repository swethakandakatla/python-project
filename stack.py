def createStack():
    stack1=[]
    return stack1

def ifStackisEmpty(stack1):
    return len(stack1)==0

def Push(stack1,item):   
    stack1.append(item)
    print("item:",item)

def PoP(stack1):
    
    return stack1.pop()




def Top(stack1):

    return stack1[len(stack1)-1]

obj=createStack()
Push(obj,10)
Push(obj,20)
Push(obj,30)
Push(obj,40)
Push(obj,50)


    
    
    

    

    