import random


total_wins = 0  
total_losses = 0  

def hangman(word_list):
    global total_wins, total_losses  

    if not word_list:
        print("\n🎉 You have guessed all the words!! Game Over 🎉")
        print(f"Final Score: Wins: {total_wins} | Losses: {total_losses}")
        return

    word = random.choice(word_list)
    word_list.remove(word)
    guesses = "" 
    lives = 5

    print("\nNew Word Loaded! Try to guess it.")    

    while lives > 0:    
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')  
            else:
                print('_', end=' ')  
                failed += 1
        print()

        if failed == 0:
            print(f"🎉 You Win! The word was: {word}")
            total_wins += 1 
            break

        guess = input("Guess a character: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please input a single letter at a time.")
            continue

        if guess in guesses:
            print("⚠️ You already guessed that letter. Try another one.")
            continue

        guesses += guess  

        if guess not in word:
            lives -= 1
            print(f"❌ Wrong! The letter '{guess}' isn't in the word.")
            print(f"You have {lives} {'lives' if lives > 1 else 'life'} left.")

        if lives == 0:
            print(f"💀 Game Over! The word was '{word}'.")
            total_losses += 1  

    
    print(f"\nCurrent Score: {total_wins} Wins | {total_losses} Losses")

   
    choice = input("\nDo you want to play again? (Enter 'q' to quit, or any key to continue): ").lower()
    if choice == 'q' or choice == 'quit':
        print("\n🏆 Thanks for playing! Here is your final score:")
        print(f"✅ Total Wins: {total_wins} | ❌ Total Losses: {total_losses}")
        return

    hangman(word_list)

word_list = ["alpha", "beta", "gamma", "delta", "pi", "rho", "sigma", "omega"]

hangman(word_list) 


