def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this line when you code the function
    run = True
    while run:
        str_in = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if str_in == "n":
                hand = dealHand(HAND_SIZE)
        if str_in == "r":
            try:
                playHand(hand, wordList, HAND_SIZE)
            except UnboundLocalError:
                print "You have not played a hand yet. Please play a new hand first!"
        if str_in == "e":
            run = False
        if str_in == "n":
            try:
                playHand(hand, wordList, HAND_SIZE)
            except UnboundLocalError:
                print ""
        elif str_in != "e" and str_in != "r":
            print "Invalid command."
    return  None


