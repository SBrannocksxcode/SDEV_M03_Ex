# Exercise 7.1
years_list = list(range(1990, 1996))

# Exercise 7.2
third_birthday_year = years_list[3]

# Exercise 7.3
oldest_year = years_list[-1]

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

# Exercise 7.10
even = [num for num in range(10) if num % 2 == 0]

# Exercise 7.11
rhymes = [
    ("Jack", "snack"),
    ("Jill", "hill"),
    ("Humpty", "dumpty"),
    ("Hickory", "dickory"),
    ("Little", "piddle"),
    ("Hey", "day"),
]

for first_word, second_word in rhymes:
    print(f"{first_word.capitalize()} {first_word.capitalize()} a {second_word},")
    print(f"But {first_word.lower()} doesn't care.")