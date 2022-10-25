def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    if type(int(s[0]))==int:
        a+=int(s[0])

    if type(int(s[1]))==int:
        a+=int(s[1])

    if type(int(s[2]))==int:
        a+=int(s[2])

    if type(int(s[3]))==int:
        a+=int(s[3])

    if type(int(s[4]))==int:
        a+=int(s[4])
    return a 
print(main('26736'))