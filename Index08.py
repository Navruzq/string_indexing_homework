def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans=0
    if s[0] == '*':
        ans = 1
    if s[1] == '*':
        ans = ans+1
    if s[2] == '*':
        ans = ans+1
    if s[3] == '*':
        ans = ans+1
    if s[4] == '*':
        ans = ans+1
    else:
        ans = False
    return ans
print(main("*****"))