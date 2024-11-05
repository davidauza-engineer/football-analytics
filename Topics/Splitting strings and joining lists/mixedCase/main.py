phrase = input()
words = phrase.split()
mixed_case_words = []
for index, word in enumerate(words):
    if index == 0:
        mixed_case_words.append(word.lower())
    else:
        mixed_case_words.append(word.capitalize())
print("".join(mixed_case_words))
