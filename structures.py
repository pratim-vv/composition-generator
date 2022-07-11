import itertools
from typing import List
from random import choice

from numpy import append

rhythyms = [1, 3/4, 1/2, 3/8, 1/4, 3/16, 1/8, 1/16]

def rhythym_sceme(measures: int) -> List[(float, bool)] :
    to_return = []
    current = 0
    rest = 0
    while current != measures :
        is_rest = True
        if current + 1 <= measures:
            to_return.append((current + choice(rhythyms), is_rest))
        elif current + 3/4 <= measures:
            to_return.append((current + choice(rhythyms[1:]), is_rest))
        elif current + 1/2 <= measures:
            to_return.append((current + choice(rhythyms[:2]), is_rest))
        elif current + 3/8 <= measures:
            to_return.append((current + choice(rhythyms[:3]), is_rest))
        elif current + 1/4 <= measures:
            to_return.append((current + choice(rhythyms[:4]), is_rest))
        elif current + 3/16 <= measures:
            to_return.append((current + choice(rhythyms[:5]), is_rest))
        elif current + 1/8 <= measures:
            to_return.append((current + choice(rhythyms[:6]), is_rest))
        else:
            to_return.append((current + 1/16, is_rest))
    return to_return
        


   

if __name__ == "__main__":
    pass


