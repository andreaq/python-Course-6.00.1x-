def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word in wordList:
        for letter in word:
            try:
                if word.count(letter) > hand[letter]:
                    return False
                    break
            except KeyError:
                return False
                break
        return True
    else:
        return False
