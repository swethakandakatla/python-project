import re
txt = "The rain in Spain\n98098:45"
x = re.findall("[+]", txt)
y=re.split('\s',txt,2)
z=re.sub('\d','ten',txt,2)
print(z)
print(y)
# x = re.search("^The.*Spain$", txt)
print(x)
# if(x):
#     print("true")
# else:
#     print("false")
