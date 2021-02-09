
filename = "day1_inputs"
file = open(filename, "r")
contents = file.read()
file.close()

# print(type(contents))
# print(len(contents))

lines = contents.splitlines()

# print(type(lines))
# print(len(lines))

print("Checking all 8,000,000 combinations...")
for number_a in lines:
    for number_b in lines:
        for number_c in lines:
            # Here will be all 8,000,000 combinations
            number_a = int(number_a)
            number_b = int(number_b)
            number_c = int(number_c)
            if number_a + number_b + number_c == 2020:
                print("Found the combination:", number_a, number_b, number_c)
                print("Product:", number_a * number_b * number_c)
                exit()