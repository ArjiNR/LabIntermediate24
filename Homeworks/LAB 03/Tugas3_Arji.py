def hangman(word):
    guesses = '_'
    lives = 5
    while True:    
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        print()

        if failed == 0:
            print("You Win!")
            break

        guess = input("Guess a character: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please input a single letter at a time")
            continue

        if guess in guesses:
            print("You already guessed that letter. Try another one")
            continue

        guesses += guess

        if guess not in word:
            lives -= 1
            print("Wrong the letter isn't in the word. Try Agains")
            print("You have", lives, "more guesses")

        if lives == 0:
            print("You Lose")
            break

word = "sigma"
hangman(word)