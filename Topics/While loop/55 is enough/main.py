count = 0
sum = 0

number = int(input())
while number != 55:
    count += 1
    sum += number
    number = int(input())

print(count)
print(sum)
print(round(sum / count))