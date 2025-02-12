def hangman(word):
    guesses = '_'
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
        guesses += guess

        if guess not in word:
            print("Wrong the letter isn't in the word. Try Agains")
word = "sigma"

hangman(word)