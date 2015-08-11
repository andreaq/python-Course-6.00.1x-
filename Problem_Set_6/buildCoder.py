import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lover_letter = string.ascii_lowercase
    lover_letter_double = lover_letter*2
    d = {}
    for letter in (lover_letter):
        step = {letter:lover_letter_double[shift],letter.upper():lover_letter_double.upper()[shift]}
        d.update(step)
        shift+=1
    return d
