phone_number = input()

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for digit in phone_number:
    print(digits[int(digit)])