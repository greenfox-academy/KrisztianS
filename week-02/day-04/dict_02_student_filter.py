
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def candy_counter():

    for i in range(len(students)):
        if (students[i]["candies"]) > 4:
                print(students[i]["name"])

candy_counter()