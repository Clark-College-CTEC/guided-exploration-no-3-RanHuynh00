# Guided Exploration No. 3
# Randy Huynh

# import the random library (snippet 1)
import random

# create an empty list to store possible names (snippet 2)
possible_names = []

# create and open a new file in write (snippet 3)
outputFile = open('rap-names-output.txt', 'w')

# open the rap-names.txt as a datafile (snippet 4)
with open('rap-names.txt', 'r') as dataFile:
    # for each name in the file
    for name in dataFile:
        # append the name to the possible_names list
        possible_names.append(name.rstrip())

# ask the user for the amount of rap names they want to create (snippet 5)
count = int(input('How many rap names would you like to create? '))
# ask for how many parts the name should have
parts = int(input('How many parts should the name contain? '))

# for each name, loop that many times (snippet 6)
for i in range(count):
    # create an empty list for the name_parts each time it loops
    name_parts = []
    # loop for each part
    for j in range(parts):
        # add a random name to the parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# write to the output file (snippet 7)
outputFile.write(f"{' '.join(name_parts)}\n")
# format the name parts with spaces in between
print(f"{' '.join(name_parts)}")

# close the file (snippet 8)
outputFile.close()
