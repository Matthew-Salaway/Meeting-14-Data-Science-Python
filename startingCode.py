# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will be discussing ways to improve the club/club membership, as well as learn data structures.

# First lets vote on the t-shirt designs and decide who wants one!

# T-shirts is a way to advertise and improve the club. Another could be a domain for the website.
# I made a website a while back for the club, but it has no domain. If we bought a domain, we would redo the website

# I will ask chapts for funding for these things. Is there anything else you can think of that would improve the club?


# Now lets go over Data Structures!

# Think of a data structure as anything that can hold multiple data values(ex: int or string)... such as tuples or arrays!
# Different structures have different benefits: Tuples, Sets, Arrays(lists), Dictionary

# Tuples: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Ordered, Unchangeable, Duplicates allowed ---- round brackets

student1 = ("Fernando", 3.67, True)  # Name, GPA, isOnlineSchool
print(student1)
print(student1[0])  # Prints the element at index 0
print(len(student1))  # returns the number of elements in tuple.

# Sets: collection which is both unordered and unindexed. store multiple items in a single variable.
# Unordered, Unchangeable, Duplicates not allowed ---- curley brackets

set = {1, 2, 3, 5, 6, 7, 7, 7}
print(set)
set.add(4)
print(set)
#print(set[2])

# Arrays/Lists: An array is a special variable, which can hold more than one value at a time. These values are elements.
# An array can hold many values under a single name, and you can access the values by referring to an index number.

cars = ["Tesla Model S", 911, "Honda", True]
print(cars)
print(cars[2])
cars.append("Ford")     #adds to list
print(cars)

# The above example is a one-D array. We can also make a two-D array, 3-D and so on. think about locker storage.
vehicles = [["car", "truck", "SUV"], ["boat", "yacht", "vessle"], ["train", "high-speed", "Inner city"]]
print(vehicles)
print(vehicles[1])
print(vehicles[0][1])

# Lastly we have dictionaries. We most likely won't be using them, so I will go over it quickly
# https://www.w3schools.com/python/python_dictionaries.asp
# Key-value. Emoji Lookup.

# Now try making a 2D array that contains all of the data structures
