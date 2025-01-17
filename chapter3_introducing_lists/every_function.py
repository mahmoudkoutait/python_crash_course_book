# Think of things you could store in a list. For example, you 
# could make a list of mountains, rivers, countries, cities, languages, or anything 
# else you’d like. Write a program that creates a list containing these items and 
# then uses each function introduced in this chapter at least once.


elements = ["car", "bike", "train", "ship"]

print(elements[1].capitalize())
del elements[0]
elements.pop(2)
print(elements)
elements.append("car")
elements.insert(0,"ship")
