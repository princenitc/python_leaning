from sys import argv
script,filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that the press CTRL-C (^C).")
print("If you want then hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename,'w')
print("Truncating the file....")
target.truncate()

print("Now, I will ask you for three new lines :)")

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("I'm going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1,line2,line3))
print("Now I will close the file.")
target.close()
