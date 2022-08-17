def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    y=len(s)
    if y%2==1:
        z = y//2
        return s[z]
    else:
        z = y // 2
        return s[z-1]+ s[z]
    

x=main('cool')
print(x)