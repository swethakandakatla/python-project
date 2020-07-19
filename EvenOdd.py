def evenodd():
    l1=[3, 6, 7, 9, 11]
    l2=[4, 5, 12, 13, 15]
    l3=[]
    l4=[]

    for i in l1:
        if i%2==0:
            l3.append(i)              
        else:
             l4.append(i)
         
    for j in l2:
        if j%2==0:
            l3.append(j)   
        else:
            l4.append(j) 
    return print(l3,l4)

evenodd()
