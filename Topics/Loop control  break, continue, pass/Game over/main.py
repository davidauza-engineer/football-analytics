scores = input().split()

failures = 0
total_score = 0

for score in scores:
    if score == 'C':
        total_score += 1
    else:
        failures += 1
        if failures == 3:
            print("Game over")
            break

if failures < 3:
    print("You won")

print(total_score)