names=['swetha','sriansha','samanvitha','kartik']
colors=['blue','yellow','orange','green']
dict1={}
# for names,colors in zip(names,colors):
#     dict1[names]=colors
# print(dict1)
dict1={names:colors for names,colors in zip(names,colors)}
print(dict1)