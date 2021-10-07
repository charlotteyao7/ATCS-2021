#Wikipedia has a list of the tallest mountains in the world, with each mountain's elevation.
#Pick five mountains from this list.
#Create a dictionary with the mountain names as keys, and the elevations as values.
#Print out just the mountains' names, by looping through the keys of your dictionary.
#Print out just the mountains' elevations, by looping through the values of your dictionary.
#Print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall."

#Revise your output, if necessary.
#Make sure there is an introductory sentence describing the output for each loop you write.
#Make sure there is a blank line between each group of statements.

mtn = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, 'Lhotse': 8516, 'Makalu': 8485}
print('Mountain Names:')
for name, elevation in mtn.items():
    print(name)
print('')
print('Mountain Elevations:')
for mame, elevation in mtn.items():
    print(elevation)
print('')
print('Summary:')
for name, elevation in mtn.items():
    print(name + ' is ' + str(elevation) + ' meters tall.')

