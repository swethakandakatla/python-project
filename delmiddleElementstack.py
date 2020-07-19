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

def removemiddleElemen(stack1):
    m=0
    val=0
    m=int(len(stack1)/2)    
    val=stack1[m]   
    stack1.remove(val)
    print(stack1)

def Top(stack1):

    return stack1[len(stack1)-1]

obj=createStack()
Push(obj,1)
Push(obj,2)
Push(obj,3)
Push(obj,4)
Push(obj,5)
# Push(obj,6)
removemiddleElemen(obj)
