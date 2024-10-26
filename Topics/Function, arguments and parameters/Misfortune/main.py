# the function is fine, you do not need to change it
def square_odds(a, b):
    start = a
    if a % 2 == 0:
        start += 1
    end = b + 1
    for odd in range(start, end, 2):
        print(odd ** 2)


# from 22 to 42
square_odds(a=22, b=42)

# from 15 to 31
square_odds(b=31, a=15)

# from 42 to 49
square_odds(42, b=49)
