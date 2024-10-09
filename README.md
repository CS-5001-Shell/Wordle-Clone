# Wordle Clone

This project requires the following concepts:

- Iteration
- Functions
- Complex Logic

## Project Setup

The repository for this assignment includes the following:

1. A skeleton Python file named *word_guesser.py*. This file includes a function that will be used to randomly generate a secret word. In order for this function to work correctly you must ensure that the *words.txt* file is also in the same directory.
2. A text file named *words.txt* that is a list of five-letter words downloaded from here: [https://www-cs-faculty.stanford.edu/~knuth/sgb.html](https://www-cs-faculty.stanford.edu/~knuth/sgb.html).
3. A text file called *sample_output.txt* that is one example of how the program may operate. Your output does not need to look exactly like the sample as long as you meet all of the requirements described below.
4. An image file called *sample_output_color.png* that shows how you may use
   colored letters in your output. **This is not required**.

## Overview

For this assignment, you will write a Python program that plays a word guessing game with the user. The requirements are as follows:

1. The user will have six tries to guess a five-letter secret word.
2. Each time the user makes a guess the program will provide feedback about the following:
  1. "Green" letters are those that appear in the same location in the guess and the secret word.
  2. "Yellow" letters are those that appear in both the guess and secret word, but in a different location.
  3. Other letters are those that are only in the guess.
3. If the user gets the secret word within six guesses the program will declare a winner, otherwise the program will tell the user what the word was.
4. The program will allow the user to continue to play until they decide to quit.
5. Before exiting, the program will report the total number of wins and losses.

## Requirements and Assumptions

1. You will use the `get_secret_word` function in the skeleton code provided to
   generate the secret word used for each round of play. The function uses the
   list of words downloaded from the following web page:
   [https://www-cs-faculty.stanford.edu/~knuth/sgb.html](https://www-cs-faculty.stanford.edu/~knuth/sgb.html).
2. You are not required to display letters in color. You may use G and Y to indicate green or yellow (see the sample output). Speak to the instructor during office hour if you wish to implement colored output as shown in the image file included in the repository. This is not required.
3. Error checking is required for *all* input.
  1. If the user guesses a word that is not five letters long the program will print an error message and ask for a new guess. The incorrectly sized guess will not be counted toward the six tries.
  2. If the user replies to the "Would you like to play again?" question with an invalid input the program will print and error message and ask for valid input.
4. You do **not** need to verify that a five-letter guess is an actual word.
5. You **must** implement the following function that will be tested via
   automated test cases:

```python
def check_guess(secret_word: str, guess: str) -> list[str]:
    """Returns a list of characters that indicate which letters of the guess
    are correct and which are not.

    Examples: 
    secret_word: heart
    guess: herds
    function returns ['G', 'G', 'Y', '-', '-']

    secret_word: trust
    guess: train
    function returns ['G', 'G', '-', '-', '-']

    secret_word: train
    guess: strut
    function returns ['-', 'Y', 'Y', '-', '-']

    secret_word: strut
    guess: stats
    function returns ['G', 'G', '-', 'Y', '-']

    If the ith item of guess matches the ith item of secret_word, then the ith
    element of the list will be a 'G'.

    If the ith item of guess does not appear anywhere in the secret_word, then
    the ith item of the list will be '-'.

    If the ith item of guess appears in the secret_word in position j where j
    does not equal i and the character at position j has not already been
    "taken" as a green or yellow character, then the item item of the list will
    be 'Y'.

    Returns [] if secret_word and guess are not both five letters long.

    Parameters:
      secret_word (str): the secret word
      guess (str): the user's guess
    Return:
      a list of string:
        if the ith element of the return value is - then the character 
    """
```


## Hints
- Implement and test your program a small portion at a time! One possible breakdown is as follows:
  1. Prompt the user for input and determine whether the guess matches (exactly) the secret word.
  2. Allow the user to make up to six guesses.  
  3. Determine the number of green (exact match) letters.
  4. Allow the user to play multiple games.
  5. Report on the number of wins and losses.
  6. Determine the number of yellow letters.
  7. Refactor your solution to improve design.


## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all four parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully