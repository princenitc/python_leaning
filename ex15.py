from sys import argv
script , read_file = argv

txt = open(read_file)

print(f"Here's is your file {read_file}")
print(txt.read())
txt.close()