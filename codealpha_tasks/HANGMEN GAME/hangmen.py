import random #we use it bcz we have 5 words, and we want Python to randomly select one.

words=["window","python","internet","programming","software"] #a list of words to choose from

word = random.choice(words) #randomly select a word from the list

hidden_word = ["_"]*len(word) #create a hidden word with underscores

max_incorrect_guesses = 6
incorrect_guesses = 0

guessed_letters = []

print("="*50)
print("HANGMAN GAME")
print("="*50)


while incorrect_guesses < max_incorrect_guesses : #everythig inside the loop will keep running while the player still has guesses remainging

    print("\nWord:"," ".join(hidden_word)) #display the hidden word with spaces between the underscores/ join puts spaces between the elements
    print("Incorrect guesses left:",max_incorrect_guesses - incorrect_guesses) #display the number of incorrect guesses left
    print("Guessed letters :",guessed_letters)


    guess = input("Guess a letter: ").lower() #ask the player to guess a letter and convert it to lowercas
    if guess in guessed_letters:
        print("You already guessed that letter before. Try again.")
        continue #if the player has already guessed that letter, skip the rest of the loop and start over
    
    guessed_letters.append(guess) # add the guessed letter to the list of guessed letters

    if guess in word:  #if the guessed letter is in the word, reveal it in the hidden word
        print("Good guess!")

        for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess #reveal the guessed letter in the hidden word
        

    else:
        print("Wrong guess!")
        incorrect_guesses += 1 #if the guessed letter is not in the word, increment the incorrect guesses counter

    
    if "_" not in hidden_word: # no underscores left in the hidden word, the player has guessed the word
        print("\nCongaratulations! You guessed the word!")
        print("The word was:", word)
        break #exit the loop if the player has guessed the word


if incorrect_guesses == max_incorrect_guesses:
        print("\nGame Over!")
        print("The word was:", word)


