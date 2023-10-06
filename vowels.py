simp_vowels = {97:945, 101:949, 104:951, 105:953, 111:959, 117:965, 119:969,
                # diaresis
                239:970, 252:971}
diacritics = {'|':chr(837), '/':chr (769), "\\":chr (768), '=':chr (834),
            '(':chr (788), ')':chr (787), '_':chr(772), '^':chr(774), '+':chr(776)}
              #, '^':chr(774), '+':chr(776)}
DIARESES = {'i+':chr(970), 'u+':chr(971), 'I+':chr(938), 'U+':chr(939)}
            # iota
DIARESES_COMP = {'i+/':chr(8147), 'i+\\':chr(8146), 'i+=':chr(8157),
            # upsilon
            'u+/':chr(8163), 'u+\\':chr (8162), 'u+=':chr (8167)}

# 1st breath
# then accent
# then iota
# / is tonons
# merge them in a str, then use normalize
# use NFC not D, to mege char
def merge_vowel_diacrit (string, temp_str, len_str, i):
    """Converts an ASCII string of a vowel and ),(,/,=, or \\ into a Greek vowel."""
    k = 1; return_str = ''
    logging.info (f'i + k = {str(i + k)} and len_str = {len_str}')
    while i + k <len_str and k < 4:
        logging.info (f'temp str is {temp_str} and i + k is {str(i + k)}')
        if string [i + k] in diacritics and (k < 3):
            logging.info ('1st critic')
            temp_str += diacritics [string [i + k]]
            logging.info (f'temp str is now {temp_str}, 35')
            k += 1
        elif string [i + k] not in diacritics: # no diacritic left
            logging.info ('No diacritic left, 38')
            return_str += normalize ('NFC', temp_str)
            break # break while loop b/c no other diacritic left
        else: # third, last diacritic
            logging.info ('last critic, 42')
            temp_str += diacritics [string [i + k]]
            return_str += normalize ('NFC', temp_str);
            break # break while loop
    logging.info (f'return str after while loop 9 is {return_str}, 46')
    if k == 1: # no diacritics
        return_str = temp_str
        logging.info ('no diacritic was used')
    return return_str

def rev_vowels (string):
    string +='   '
    """Sets up an ASCII string of vowels and ),(,/,=, or \\ to be converted into a
    Greek vowel using merge_vowel_diacrit()."""
    return_str =''; len_str = len (string)
    for i in range (len_str):
        logging.info (f'{str(i)} and {string [i]}')
        this_char_uni = ord(string[i]); temp_str = ''
        if not (this_char_uni in simp_vowels or this_char_uni + 32 in simp_vowels or string [i] in diacritics):
            # uses de morgan
            return_str += string[i]
        elif (this_char_uni in simp_vowels or this_char_uni + 32 in simp_vowels):
            # it's a vowel (diacritic won't be passed to return_str)
            logging.info ("It's a vowel, 63")
            if this_char_uni in simp_vowels:
                temp_str = chr (simp_vowels[this_char_uni]) # the ith char
            else: # capital
                temp_str = chr (simp_vowels[this_char_uni + 32] - 32)
            # both go through here
            # for vowels not in final position
            logging.info (f'temp str before merge fucnt is {temp_str}, 70')
            return_str += merge_vowel_diacrit (string, temp_str, len_str, i)
            logging.info (f'return str after merge fucn 7 is {return_str}, 72')
    return return_str[0:(len_str - 4)]

# assumes it went through rev_vowels()
def diaresis (string):
    """Converts i and u with + into a iota and upsilon with a diaresis."""
    len_str = len(string); return_str = ''
    for i in range(len_str - 2):
        if string [ i:i+3 ] in DIARESES_COMP:
            return_str += DIARESES_COMP [ string [ i:i+3 ] ]
        elif string [ i:i+2 ] in DIARESES:
            return_str += DIARESES [ string [ i:i+2 ] ]
        # don't let the plus sign go through
        elif string [i] == '+':
            pass
        else:
            return_str += string [i]
    return return_str

from unicodedata import *
import logging

