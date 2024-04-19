import random

with open ('words.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1] # The word of the round is randomly selected and then all but the last character (/n) is selected.

allowed_errors = 7
guesses = []
past_guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed errors remaining: {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -=1
        past_guesses.append(guess.lower())
        if allowed_errors == 0:
            break

    # if (past_guesses != []) and (guess.lower() not in word):
    #     for letter in past_guesses:
    #         if guess.lower() == letter:
    #             print(f"You have already guessed that letter, {letter}!")
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"Correct! You have successfully guessed the word: {word}.")
else:
    print(f"Game over! The word was {word}.")