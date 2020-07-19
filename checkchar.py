import re

pattern = '[a*a]'
test_string = 'abba'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	