a = 1 # Integer
b = 1.1 # Float
c = "1" # String

print ("""
All of these values will be of different types.
""")
print(type(a))
print(type(b))
print(type(c))

print ("""
Original Values:
""")

print (a)
print (b)
print (c)

print ("""
Casting is when you can force a data type on a variable.
""")


a = str(a)  # This will cast a to an integer

b = str(b)  # This will cast b to an integer

c = str(c)  # This will cast c to an integer

print(type(a))
print(type(b))
print(type(c))

print ("""
Values after casting:
""")

print (a) # Integer
print (b) # Integer
print (c) # Integer