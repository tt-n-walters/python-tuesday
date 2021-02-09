
#   Reusability - Functions can be run on command and as many times as we like
#   Dynamic     - Functions can be run in custom ways, ie. we can change their inputs


names = [
    "Arthur",
    "Bill",
    "Charlie",
    "Fred",
    "George",
    "Ginny",
    "Harry",
    "Hermione",
    "Molly",
    "Percy",
    "Ron"
]


filename = "names.txt"
file = open(filename, "r", encoding="utf-8")
names_1000000 = file.read().splitlines()
names_1000000.sort()

target = input("Enter name: ")

# linear search algorithm
def linear_search(data, needle):
    amount_of = len(data)
    range_of_names = range(amount_of)
    for i in range_of_names:
        if data[i] == needle:
            print("Yay found at position " + str(i) + "!")
            break
        # else:
        #     print("Not at position " + str(i) + ".")
    
    return i


x = linear_search(names, target)
print(x)




names = [
    "Arthur",
    "Bill",
    "Charlie",
    "Fred",
    "George",
    "Ginny",
    "Harry",
    "Hermione",
    "Molly",
    "Percy",
    "Ron"
]

# binary search algorithm


def binary_search(list, target):
    left = 0
    right = len(list) - 1

    return "Hi from the function"
    searches = 0
    searching = True
    while searching:
        midpoint = int((right - left) / 2) + left
        middle_name = list[midpoint]
        searches += 1

        if middle_name == target:
            print("Found at position " + str(midpoint) +
                  ". Took " + str(searches) + " searches.")
            searching = False
        elif middle_name < target:
            left = midpoint + 1
        elif middle_name > target:
            right = midpoint - 1
    
    return midpoint


index = binary_search(names_1000000, target)
print(index)
print("Program finished.")
