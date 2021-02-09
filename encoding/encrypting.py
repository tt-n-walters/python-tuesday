message = input("Enter the message to be encoded: ")
print("Encoding:", message)
print("Length of message:", len(message))

secret_numbers = []
for character in message:
    number = ord(character)
    # print(character, number)
    secret_numbers.append(number)

print(secret_numbers)