string = input()

characters = [',', '.', '!', '?']

processed_string = string

for character in characters:
    processed_string = processed_string.replace(character, '')

print(processed_string.lower())
