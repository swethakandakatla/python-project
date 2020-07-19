l1=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

newlist=list(filter(lambda a:(a%19==0),l1))
newlist1=list(filter(lambda b:(b%13==0),l1))
newlist+=newlist1
newlist.sort()
print(newlist)