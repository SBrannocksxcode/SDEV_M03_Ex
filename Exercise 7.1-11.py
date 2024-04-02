# Exercise 7.4
things = ["mozzarella", "cinderella", "salmonella"]

# Exercise 7.5
things[1] = things[1].capitalize()

# Exercise 7.6
things[0] = things[0].upper()

# Exercise 7.7
things.remove("salmonella")

# Exercise 7.8
surprise = ["Groucho", "Chico", "Harpo"]

# Exercise 7.9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()

# Exercise 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

# Exercise 9.2
def get_odds():
    for num in range(1, 10, 2):
        yield num

# Use a for loop to find and print the third value returned by the generator function
for index, num in enumerate(get_odds()):
    if index == 2:
        print("Third odd number:", num)
        break
