print("Welcome to the Word Guessing Game!")
print("-----------------------------------")
print("Category is farm animals.")

secret_word = "Cow" 


guessing_letters = []
tries = 6

while tries > 0:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that!")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        tries -= 1
        print("Wrong! You have", tries, "tries left.")

    if all(letter in guessed_letters for letter in secret_word):
        print("You win! The word was", secret_word)
        break
else:
    print("Game over! The word was", secret_word)