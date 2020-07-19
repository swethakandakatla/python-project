import re
str1=input("enter any string:")
pattern='[aeiouAEIOU]'
flags='I'
if(re.match(pattern,str1)):
    print("starts with vowel")
else:
    print("not vowel")
