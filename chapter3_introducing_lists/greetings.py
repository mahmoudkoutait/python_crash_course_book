# Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each mes
# sage should be the same, but each message should be personalized with the 
# person’s name.

friends_names = ["mahmoud", "mohamed", "ali", "ahmed"]

for name in friends_names:
    print(f"how are you {name.capitalize()}?")