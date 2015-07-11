def hangman(secretWord):
    secretWord = secretWord.lower()
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is {} letters long.".format(len(secretWord))
    print "-------------"
    i = 8
    lettersGuessed = ""
    while i > 0 :
        print "You have {} guesses left.".format(i)
        print "Available letters: {}".format(getAvailableLetters(lettersGuessed))
        letterIn = str(raw_input("Please guess a letter: "))
        letterIn = letterIn.lower()
        if letterIn in lettersGuessed:
            print "Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed))
            i+=1
        else:
            lettersGuessed =lettersGuessed+letterIn
            if (letterIn in secretWord) ==  True:
                print "Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed))
                i+=1
            else:
                print "Oops! That letter is not in my word: {} ".format(getGuessedWord(secretWord, lettersGuessed))
        print "------------"
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "Congratulations, you won!"
            break
        i -= 1   
    return "Sorry, you ran out of guesses. The word was {}.".format(secretWord)
