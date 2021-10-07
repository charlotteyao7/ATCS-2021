#Create a dictionary to hold information about pets. Each key is an animal's name, and each value is
# the kind of animal.
#For example, 'ziggy': 'canary'
#Put at least 3 key-value pairs in your dictionary.
#Use a for loop to print out a series of statements such as "Willie is a dog."

pets = {'Cookie': 'dog', 'Snowflake': 'cat', 'Stephie': 'bunny'}
for name, kind in pets.items():
    print(name + " is a " + kind)