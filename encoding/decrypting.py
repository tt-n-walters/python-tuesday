secret_numbers = [102, 111, 100, 112, 101, 102, 101, 32, 106, 111, 32, 98, 111, 32, 98, 111, 100, 106, 102, 111, 117, 32, 115, 112, 110, 98, 111, 32, 100, 106, 113, 105, 102, 115]

print("Decoding", len(secret_numbers), "values.")
offset = 0

for i in range(26):
    characters = []
    for number in secret_numbers:
        # If the number is 32 (the character is a space)
        # Just decode normally and add to the list
        if number == 32:
            character = chr(number)
            characters.append(character)
        else:
            # If we have an actual letter, add the offset
            offset_number = number + offset
            # If the letter would now be past the end of the alphabet
            # subtract 26 to reset back to the beginning
            if offset_number > 122:
                offset_number -= 26
            character = chr(offset_number)
            characters.append(character)



    whole_string = "".join(characters)
    print("Result with offset of", offset, ":", whole_string)
    offset += 1