    #counting the number of letters,digits and space in the sentence
str_input=input("enter a sentence:")
num_spaces=0
letters_digits={"letters":0,"digits":0}
for i in str_input:
    if i.isalpha():
        letters_digits["letters"]+=1
    elif i.isdigit():
        letters_digits["digits"]+=1
    elif i.isspace():
        num_spaces=num_spaces+1
    else:
        pass

print("Letters:",letters_digits["letters"])
print("Digits:",letters_digits["digits"])
print("number of spaces:",num_spaces)
    