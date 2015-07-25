def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to
        # test if the word is in the wordList - you can make a similar function
        # that omits that test)
        if isValidWord(word,hand,wordList):
            
            # Find out how much making that word is worth
            score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if score > best_score:

                # Update your best score, and best word accordingly
                best_score = score
                best_word = word

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function;
    #do your coding within the pseudocode (leaving those comments in-place!)
    
    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        
        # Computer plays
        word_in = compChooseWord(hand, wordList, n)
        
                
        # If the input is a single period:
        if word_in == None:
        
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word_in, hand, wordList) != True:
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
                print ""

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score,
                #in one line followed by a blank line
                total_score += getWordScore(word_in, n)
                print "\"{}\" earned {} points. Total: {} points".format(word_in, getWordScore(word_in, n),total_score)
                print ""
                # Update the hand
                hand = updateHand(hand, word_in)
                
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Run out of letters. Total score: {} points.".format(total_score)
