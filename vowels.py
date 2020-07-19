def Vowels():
    s=input("enter the word:")
    w=set(s)
    v={'a','e','i','o','u'}
    d=w.intersection(v)
    print(d)

Vowels()
