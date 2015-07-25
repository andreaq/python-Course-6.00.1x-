def updateHand_foo(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    if len(word)== 1:
        if word[0] in hand and hand[word[0]] > 0:
            hand[word[0]] -= 1
        return hand
    elif len(word) > 1:
        if word[0] in hand and hand[word[0]] > 0:
            hand[word[0]] -= 1
        hand = updateHand(hand, word[1:])
        return 	hand

def updateHand(hand, word):
    hand_copy = hand.copy()
    #print hand_copy
    return updateHand_foo(hand_copy, word)
