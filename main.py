print("Welcome to GC mini golf!")
name = input("What is your name? ")
print("Hi " + name + "!")

while True:
    choice = input("Would you like to play 3 or 6 holes today? "). strip()
    if choice == '3':
        num_holes = 3
        par_score = 9
        break
    elif choice == '6':
        num_holes = 6
        par_score = 18
        break
    else:
        print("Please enter 3 or 6.")

putts = []

for hole in range(1, num_holes + 1):
    while True:
        try:
            num_putts = int(input(f"How many putts for hole {hole}?) (par is 3) ").strip())
            putts.append(num_putts)
            running_total = sum(putts)
            print(f"Current running total: {running_total}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

total_putts = sum(putts)

score_difference = total_putts - par_score

if total_putts > par_score:
    over_par = total_putts - par_score
    print(f"Nice try, {name}! Your total par was +{score_difference}.")
elif total_putts < par_score:
    under_par = par_score - total_putts
    print(f"Great job, {name}! Your total par was {score_difference}.")
else:
    print(f"Good game, {name}! Your total par was: 0.")












