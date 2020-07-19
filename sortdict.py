def Sortdictkey():
    key_value={2:'64',1:'69',4:'23',5:'65',6:'34',3:'76'}
    sortedkeyvalue={}
    for key in sorted(key_value.keys()):
        sortedkeyvalue=key,key_value[key]
    
        print(tuple(sortedkeyvalue),end='')

Sortdictkey()