first_input = input()
second_input = input()

indexes = []

for index, element in enumerate(first_input.split()):
    if element == second_input:
        indexes.append(str(index))

if len(indexes) == 0:
    print("not found")
else:
    print(" ".join(indexes))
