str1="python"
str2=[]

val=len(str1)
for i in range(0,val):
     
     if str1[i]!='y':
       str2+=str1[i]
      
     else: 
      pass
print(''.join(str2))

str3="python"
str4=[]
val=len(str3)
for i in range(0,val):
      if str3[i]=='y':
        str4+=''
      else:
        str4+=str3[i]  
print(','.join(str4))