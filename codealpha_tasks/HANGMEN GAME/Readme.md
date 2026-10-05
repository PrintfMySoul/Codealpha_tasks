# Hangman Game

## Description

This is a simple Hangman game developed using Python. The game runs in the console and allows the player to guess a randomly selected word one letter at a time.

The game uses a small list of 5 predefined words, and the player has a maximum of 6 incorrect guesses.

## Features

* Uses 5 predefined words.
* Randomly selects one word at the beginning of each game.
* Hides the letters of the word using underscores (`_`).
* Allows the player to guess one letter at a time.
* Keeps track of previously guessed letters.
* Reveals correctly guessed letters.
* Allows a maximum of 6 incorrect guesses.
* Displays a win message when the word is completely guessed.
* Displays a game-over message when the player reaches 6 incorrect guesses.
* Runs entirely in the console with no graphics or audio.

## How to Run

### Requirements

* Python 3
* No external libraries are required.

### Steps

1. Make sure Python is installed on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code or another Python editor.
4. Open the terminal in the project folder.
5. Run the following command:

```bash
python hangman.py
```

6. Follow the instructions shown in the console.

## How the Game Works

1. The program creates a list containing 5 predefined words.
2. `random.choice()` randomly selects one word from the list.
3. The selected word is hidden using underscores.
4. The player is asked to guess one letter.
5. If the letter is in the word, it is revealed in its correct position.
6. If the letter is not in the word, the number of incorrect guesses increases by one.
7. The player can make up to 6 incorrect guesses.
8. The game ends when:

   * The player correctly guesses the entire word, or
   * The player reaches 6 incorrect guesses.

## Python Concepts Used

This project uses the following basic Python concepts:

* **Random:** `random.choice()` is used to select a random word.
* **Lists:** Used to store the predefined words, hidden letters, and guessed letters.
* **Strings:** Used for the words and console messages.
* **While loop:** Keeps the game running while the player has incorrect guesses remaining.
* **If-else statements:** Used to check whether a guessed letter is correct, already guessed, or incorrect.
* **For loop:** Used to check each position of the selected word and reveal correctly guessed letters.
* **User input:** `input()` is used to receive guesses from the player.
* **Output:** `print()` is used to display the game information and results.

## Word List

The game currently uses these 5 predefined words:

* window
* python
* internet
* programming
* software

## Example

```text
==================================================
HANGMAN GAME
==================================================

Word: _ _ _ _ _ _
Incorrect guesses left: 6
Guessed letters : []
Guess a letter: p
Good guess!

Word: p _ _ _ _ _
Incorrect guesses left: 6
Guessed letters : ['p']
Guess a letter: 
```

## Author

Created as a beginner Python programming project to practice basic Python concepts and game logic.
