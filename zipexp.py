players=["sachin","abc", "def","ghi"]
scores=[100,20,30,40]

d1=zip(players,scores)
print(d1)
for x,y in d1:
    print("players:{} scores:{}".format(x,y))
