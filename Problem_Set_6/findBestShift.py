def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    check = []
    for shift in range(0,26):
        clear_text = applyShift(text, shift)  
        num_word = 0
        for word in clear_text.split(" "):
            if isWord(wordList, word):
                num_word += 1
        check.append(num_word)
    return check.index(max(check))
