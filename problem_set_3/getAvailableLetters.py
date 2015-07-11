def getAvailableLetters(lettersGuessed):  
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all = string.ascii_lowercase
    i =0
    for letter in lettersGuessed:
        all = all.replace(letter, "")
    return all
