def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord) == 1:
        if secretWord[0] in lettersGuessed:
            return secretWord[0]+" "
        else:
            return "_ "
    if secretWord[0] in lettersGuessed:
        return secretWord[0]+" "+getGuessedWord(secretWord[1:],lettersGuessed)
    else:
        return "_"+" "+getGuessedWord(secretWord[1:],lettersGuessed)
