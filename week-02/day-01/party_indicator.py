# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people\

girls = int(input("Girls: "))
boys = int(input("Boys: "))
if girls == boys and girls + boys == 20:
    print("The party is excellent!")
if girls + boys > 20 and girls / boys != 1:
    print("Quite cool party!")
if girls + boys < 20:
    print("Average pary...")
if girls == 0:
    print("Sausage party")