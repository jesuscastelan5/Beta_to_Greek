from conson import *
from vowels import *

def BETA_TO_GREEK (string):
    """Converts a betacode string into Greek characters."""
    string += '   '
    string = rev_consonants (string)
    # no diaresis found
    if string.find ('+')<0:
        pass # just pass it through, do not return string yet.
    # found one
    else:
        string = diaresis (string)
    string = rev_vowels (string)
    return string
