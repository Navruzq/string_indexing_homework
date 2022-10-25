def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=='*':
        i = 1
    elif s[1]=='*':
        i = 1
    elif s[2]=='*':
        i = 1
    elif s[3]=='*':
        i = 1
    elif s[4]=='*':
        i = 1
    else:
        i = False
    return i 
print(main("*jkhj"))