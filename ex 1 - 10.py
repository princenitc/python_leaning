# Exercise - 01 

print("This is the first exercise of python the hard way.")
print("this is the second print statement of the file.")
# Octothorpe or hash can be used to comment the codes for single lines comment.


        #Exercise - 02
print("I could have code like this.") #this part of the code will be ignored.


        # Exercise - 03

print("Hens", 25 + 30 / 6)

print("Roosters", 100 - 25 * 3 % 4)
print("Is it greater? ", 5 > -1)



                        # Exercise - 04

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ",cars,"cars available.")
print("There are only ",drivers," drivers available.")
print("There will be ",carpool_capacity, " people today.")

                                # Exercise - 05


my_name = "Prince Chauhan"
my_age = 21
my_height = 170 #cms
my_weight = 62 #kilograms
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cms tall.")
print(f"He's {my_weight} kilograms heavy.")
print("Actually that's not too heavy.")

print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky , try to get it exactly right

total = my_age + my_height + my_weight
print(f"If I {my_age}, {my_height}, and {my_weight} I get {total}.")



                # Exercise - 05 

type_of_people = 10 
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and who {do_not}."

print(x)
print(y)

print(f"The above could be also written as {x}.")

hilarious = False
joke_evaluation  = "Isn't that a joke so funny ?! {}."
print(joke_evaluation.format(hilarious))

w = "This is the left side ......."
e = "a string with right side."
print(w+e)


                        # Exercise - 07
        
print("Continuation of the print statements --- >")
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('Snow'))
print("."*50)


                        # Exercise - 08

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
        "Pta nhi kis roop mein aakar","Narayan mil jaega",
        "nirmal man ke darpan ko","darshan de jaega."
))


                        # Exercise - 09 

days = "Mon Tue Wed Thur Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here's are the days: ", days)
print("Here are the months: ", months)

print("""This Kind of three double quotes could 
be used to print the statement in the multi line printing.""")


                        # Exercise - 10

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list :
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)