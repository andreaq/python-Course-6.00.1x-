def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    coded_text = ""
    for char in text:
            char = coder.get(char, char)
            coded_text += char
    return coded_text
