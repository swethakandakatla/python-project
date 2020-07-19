pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    
    while l<=u:
        mid = int(l + u)/2
        print(mid)
    if(list[mid]==n):
         globals()['pos']=mid
         return true
    else:
            if(list[mid]<n):
                l = mid
            else:
                u = mid  
     
list = [3,6,9,11,15]
n = 6
    
if search(list,n):
    print("found")
else:
    print("not found")