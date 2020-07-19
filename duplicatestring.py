def Finddupchar():
    str_char='hello'
    strlen=len(str_char)
    countchar=0
    for i in range(0,strlen-1):
        if(str_char[i]==(str_char[i+1])):
           countchar+=1
      
        else:
            pass 
    return print(countchar)     

Finddupchar()