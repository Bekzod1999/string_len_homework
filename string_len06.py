def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    y=len(s1)
    z=len(s2)
    if y>z:
        w=z
    else:
        w=y
    return w