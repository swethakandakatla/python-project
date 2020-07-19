import array as arr;
def createStack():
    stack1=[]
    # tmpstack=[]
    arr=[]
    return stack1


def ifstackisempty(stack1):
    return len(stack1)==0

def Pushstack(stack1,item):
    stack1.append(item)

def Popstack(stack1):
    return stack1.pop()

def TopofStack(stack1):
    return stack1[len(stack1)-1]


def sortStack(stack1):
    tmpstack=createStack()
    while(ifstackisempty(stack1)==False):
        tmp=TopofStack(stack1)
        Popstack(stack1)
        while(ifstackisempty(tmpstack)==False and TopofStack(tmpstack)>tmp):
            Pushstack(stack1,TopofStack(tmpstack))
            Popstack(tmpstack)
        Pushstack(tmpstack,tmp)
       
    return tmpstack

def sortArrayUsingStack(arr,n):
    input=[]
    i=0
    #inserting the array elements into stack
    while(i<n):
        input.append(arr[i])
        i=i+1
        
    
    # tmpstack=createStack()
    tmpstack=sortStack(input)
   
    #after sorting the elements move into array arr

    i=n-1
    while(i>=0):
        tmp=TopofStack(tmpstack)
        arr[i]=tmp
        tmpstack.pop()
        i=i-1
       
    return arr

    #carray values
arr=[8,5,7,1,9,12,10]
n=len(arr)
sortarr=sortArrayUsingStack(arr,n)
i=0
while(i<n):
    print(sortarr[i], end=" ")
    i=i+1



stack=createStack()

sortArray=sortStack(stack)



