from sys import argv

script, first, second  = argv

print("The script is called as ",script)
print("My first variable is ",first)
print("My second variable is ",second)
# print("My third variable is ",third

# normal input method 
variable = input("enter the variable ")
print("Variable from normal input method",variable)

print("Variable from argv is : ",first,second)
