
dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
    
translation={keys.translate({32:None}):values for keys, values in dict.items()}
print(translation)