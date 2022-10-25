def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0] == '*':
        ans = 0
    elif s[1] == '*':
        ans = 1
    elif s[2] == '*':
        ans = 2
    elif s[3] == '*':
        ans = 3
    elif s[4] == '*':
        ans = 4
    else:
        ans = False
    return ans
print(main("*4544"))
