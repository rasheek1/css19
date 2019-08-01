def character_counter():
    response = raw_input('Enter a Word : ')
    characters = {}
    for char in response:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
            
    return characters

print(character_counter())
