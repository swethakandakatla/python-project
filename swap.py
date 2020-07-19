def swap():
    list2=[1,2,3,4,5]
    val=list2[0]
    temp=list2[-1]
    print(temp)
    list2[0]=temp
    list2[-1]=val
    print(list2)
    return list2
  
list4=swap()