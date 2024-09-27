import random # library required to randomly choose a secret word

def get_secret_word() -> str:
    """
    Returns a randomly generated secret word.
    Uses the list of words in the public domain retrieved from:
    https://www-cs-faculty.stanford.edu/~knuth/sgb.html
    Requires a text file called words.txt.	
    """
    with open('words.txt') as f:
        words = f.read().splitlines() 		
        word = random.choice(words)
    return word

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
    pass

def main():
    pass

if __name__ == '__main__':
    main()