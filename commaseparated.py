str=input("enter the sentence").split(',')
items=[i for i in str]
items.sort()
print(','.join(items))
