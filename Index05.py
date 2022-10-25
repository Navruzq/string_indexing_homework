from re import T


def isDigit(x):
    if x>='0' and x<='9':
        return True
    else:
        return False
def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    if isDigit(s[0]):
        k+=1
    if isDigit(s[1]):
        k+=1
    if isDigit(s[2]):
        k+=1
    if isDigit(s[3]):
        k+=1
    if isDigit(s[4]):
        k+=1
    return k
print(main('1djd4'))