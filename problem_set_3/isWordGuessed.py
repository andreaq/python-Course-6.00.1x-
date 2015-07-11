def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord)==1:
        return secretWord[0] in lettersGuessed
    else:
        return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)
