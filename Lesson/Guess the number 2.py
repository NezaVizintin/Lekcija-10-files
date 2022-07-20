import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Your top score is: " + str(best_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    attempts += 1

    if guess == secret:
        if best_score > attempts:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("You've guessed it!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        print("Not quite there, try going a bit higher!")
    elif guess > secret:
        print("Not quite there, try going a bit lower!")
