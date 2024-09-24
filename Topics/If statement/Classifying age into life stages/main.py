# Read the user's age
age = int(input())

# Check the age and print the corresponding category
# TODO: Write your if statement here
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
