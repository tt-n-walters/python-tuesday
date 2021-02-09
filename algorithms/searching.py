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
def linear_search():
    amount_of = len(names_1000000)
    range_of_names = range(amount_of)
    for i in range_of_names:
        if names_1000000[i] == target:
            print("Yay found at position " + str(i) + "!")
            break
        # else:
        #     print("Not at position " + str(i) + ".")


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
def binary_search():
    left = 0
    right = len(names_1000000) - 1

    searches = 0
    searching = True
    while searching:
        midpoint = int((right - left) / 2) + left
        middle_name = names_1000000[midpoint]
        searches += 1

        if middle_name == target:
            print("Found at position " + str(midpoint) + ". Took " + str(searches) + " searches.")
            searching = False
        elif middle_name < target:
            left = midpoint + 1
        elif middle_name > target:
            right = midpoint - 1


binary_search()
binary_search()
binary_search()
binary_search()
binary_search()