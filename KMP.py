# form the naive approach KMP uses the fact that when matching each character
# of a string when there is a mismatch we need not come to beginning of the pattern
# to match with main string instead we came to the position where suffix is prefix.
# suffix is prefix means where a end of string(a substring at the end) match
# exactly with a substring at the beginning and we start our search at index + 1.
# making table of suffix and prefix
def makeTable(s):
    table = [0] * len(s)
    j = 0
    i = 1
    while i < len(s):
        if s[i] == s[j]:
            table[i] = j + 1
            j += 1
        else:
            j = 0
        i += 1
    return table


def KMP(main, pattern):
    table = makeTable(pattern)
    j = -1
    i = 0
    while i < len(main) and j < len(pattern):
        # if there is a match increase counter
        if pattern[j + 1] == main[i]:
            j += 1
            i += 1
        # if j is -1 and pattern still do not match move on
        elif j == -1:
            i += 1
        # come back of j to the index where suffix is equal to prefix
        else:
            j = table[j] - 1
        # if all j matched then it is a match
        if j == len(pattern) - 1:
            return True
    return False


print(KMP('abcdeabfabc', 'abcb'))
