def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} cheese of crackers!")
    print(f"Man that's enough for a party.")
    print(f"Get a blanket.\n")

print("We can give the function arguments numbers directly:")
cheese_and_crackers(20,30)

print("Or, we can use variables from our own script.")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can do the math also inside the parameters:")
cheese_and_crackers(10 + 20, 5 + 5)

print("OR else we can also combine the two variables and math them:")
cheese_and_crackers(10 + amount_of_cheese, 20 + amount_of_crackers)