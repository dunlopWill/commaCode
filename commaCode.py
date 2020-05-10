#commaCode function takes a list values as an argument.
#It returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item.

#Example Lists
food = ['apples', 'bananas', 'tofu', 'rice']
animals = ['lions', 'tigers', 'bears', 'zebras', 'leopards', 'frogs']
names = ['John Smith']
empty = []

#Define commaCode function
def commaCode(list):
    if len(list) == 0:
        print("Please enter a list with values inside of it.")
        return 0
    elif len(list) > 1:
        string = ""
        for i in range(len(list)-2):
            string = string + list[i] + ", "
        string = string + list[len(list)-2] + " and " + list[len(list)-1]
        print(string)
    else:
        print(list[0])

#Call function commaCode
commaCode(animals)