import string
def letters_file_line(n):
    f1=open("alpha.txt",'r+')
    alphabet = string.ascii_uppercase
    letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
    f1.writelines(letters)
letters_file_line(3)
# list=['ABC','DEF','GHI','JKL','MNO','PQR','STU','VWX','YZ']
# f1.writelines(list)
# n=len(list)d
# str=""
# i=int(input("enter number:"))
# if i!=0:
#     str=f1.read(i)
#     print(str,end='')
#     # print(f1.tell())


# else:
#     f1.close()

# f1=open("alphabets.txt",'r+')
# # f1.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# # with open('alphabets.txt','r')as f:
# #     for line in f:
# #         print(line,end='')
# # n=int(input("enter the number:"))
# i=int(input("enter how many letters to get:"))

# str=f1.read()
# n=len(str)
# for i in range(3,n):
#   str1=str[i::]

#   print(str1)
# # n=len(str)
# # for i in range(n):

#     print(str.split(i))
# # n=len(str.split(3))
# print(str,end='')
# n=len(str)

