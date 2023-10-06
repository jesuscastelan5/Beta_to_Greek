REV_CONS = {98:946, 103:947, 100:948, 118:988, 122:950, 113:952, 107:954,
            108:955, 109:956, 110:957, 99:958, 112:960, # s and r spec cases
            116:964, 102:966, 120:967, 121:968}

def sigma (string, len_str, i):
    """Decides if an 's' is a non final or final sigma."""
    if string [i] == 's':
        # not a final position
        if i != (len_str - 1) and 96 < ord (string [i+1]) and ord (string [i+1]) < 123:
            return chr (963)
        else:
            return chr (962)
    # cap S
    else:
        return chr (931)

def rho (string, i):
    """Produces rho with or without breath marks."""
    string +=' ' 
    if string [i] == 'r':
        if string [i + 1] == '(': # dasia
            return chr (8165)
        if string [i + 1] == ')': # psili
            return chr (8164)
        else:
            return chr (961)
    # cap R, only w/ dasia
    else:
        if string [i + 1] == '(':
            return chr (8172)
        else:
            return chr (929)
    
def rev_consonants (string):
    """Converts most ASCII consonants into Greek consonants.
    Passes 's' and 'r' to sigma() and rho() respectively."""
    return_string = ''
    len_str = len (string)
    for i in range (len_str):
        # not s nor r
        if ord (string [i]) in REV_CONS or (ord (string [i]) + 32) in REV_CONS:
            # lowercase
            if ord (string [i]) in REV_CONS:
                return_string += chr (REV_CONS [ord (string [i])])
            # uppercase
            else:
                return_string += chr (REV_CONS [ord (string [i]) + 32] - 32)
        # s
        elif (string [i] == 's') or (string [i] == 'S'):
            return_string += sigma (string, len_str, i)
        # r
        elif (string [i] == 'r') or (string [i] == 'R'):
            return_string += rho (string, i)
        else:
            return_string += string [i]
    return return_string

