name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
dict1={}
l1=[]
n=len(name)
dict1=zip(name, roll_no, marks)

dict1=set(dict1)
print(dict1)

# for x,y,z 

name,roll_no,marks=zip(*dict1)
print(name)
print(roll_no)
print(marks)



