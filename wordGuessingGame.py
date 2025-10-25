import random
wordBank = ["cat", "cute", "meow", "cozy", "computer", "neko", "chocolate", "luck", "lust", "hair", "shark", "ubuntu", "chain", "paw", "moon", "candle", "pluto", "math"]

word = random.choice(wordBank)
guessWord = ["_"] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessWord))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print("\nGreat guess!")
    else:
        attempts -= 1
        print("\nWrong guess! Attempts left: " + str(attempts))

    if "_" not in guessWord:
        print("\nCongratulations!! you guessed the word: " + word)
        break

    if attempts == 0 and "_" not in guessWord:
        print("\nYou ran out of attempts! The word was: " + word)
        