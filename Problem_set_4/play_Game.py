def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e',
          keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    Test = True
    word_in_2= ""
    while Test == True:
        word_in_1 = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if word_in_1 == "e":
            Test = False
            break
        if word_in_1 not in ["n","r"]:
            print "Invalid command."
        if word_in_1 == "n":
            hand = dealHand(HAND_SIZE)
            test_hand = True
        if word_in_1 == "r":
            try:
                hand
            except UnboundLocalError:
                test_hand = False 
                print "You have not played a hand yet. Please play a new hand first!"
        if word_in_1 in ["n","r"] and test_hand == True:
            word_in_2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            while word_in_2 not in ["u","c"] and word_in_1 in ["n", "r"]:
                print "Invalid command."
                print ""
                word_in_2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            if word_in_2 == "u":
                playHand(hand, wordList, HAND_SIZE)
                print ""
            elif word_in_2 == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
            print ""
    return None
