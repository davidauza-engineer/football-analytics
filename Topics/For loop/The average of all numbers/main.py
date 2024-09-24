first_number = int(input())
second_number = int(input())

divisible_by_3 = []

for number in range(first_number, second_number +1):
    if number % 3 == 0:
        divisible_by_3.append(number)

average = sum(divisible_by_3) / len(divisible_by_3)

print(average)