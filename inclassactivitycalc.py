def add(a,b):
    print(a + b)
    return (a + b)
def sub(a,b):  
    print(a - b)
    return (a - b)
def mul(a,b):
    print(a * b)
    return (a * b)
def div(a,b):
    print(a / b)
    return (a / b)

"""
import doctest
def add(a,b):
    #print(a + b)
    """
    >>> add(2, 3)
    5
    """
    return (a + b)
def sub(a,b):  
   # print(a - b)
    """
    >>> sub(7, 3)
    4
    """
    return (a - b)
def mul(a,b):
    #print(a * b)
    """
    >>> mul(2, 3)
    6
    """
    return (a * b)
def div(a,b):
    #print(a / b)
    """
    >>> div(20, 2)
    10.0
    """
    return (a / b)
doctest.testmod()

"""
