def reverseWords(string):
    st=[]
   
    for i in range(len(string)):
        if(string[i]!=" "):
            st.append(string[i])
             
        else:
            
            while(len(st)!=0):
                print(st[-1],end=" ")
                st.pop()
    while len(st) > 0: 
        
        print(st[-1], end = " ") 
        st.pop() 

string="hello world"
reverseWords(string)

