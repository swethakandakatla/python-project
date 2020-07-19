# str='php'
# str1='php'
# rever_str=str1[::-1]
l2=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# n=len(l1)
palin=list(filter(lambda a: a==a[::-1],l2))
# result=palin(l2)

print(palin)
