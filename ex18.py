def print_two(*args):
    arg1,arg2 = args
    print(f"arg1 : {arg1}, arg2 : {arg2}.")

def print_two_again(arg1,arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}.")

def print_one(one):
    print("one: {}".format(one))

def print_none():
    print("Function without argument.")

print_two("prince","chauhan")
print_two_again("Vimal","chauhan")
print_one("Anubhav")
print_none()