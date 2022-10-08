user_input = str(input("Enter a phrase:"))
#string input user then adding the split function to split the sentence

text = user_input.split()
a = ""
#a variable to store the acronym phrase

for i in text:
    a = a+str(i[0]).upper()
#a for loop over the variable while running it is get stored in the index[0] for every word after the split then making it upper.

print(a)



