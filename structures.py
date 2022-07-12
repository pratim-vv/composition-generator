import itertools
from typing import List, Tuple
from random import choice
from musx import Score, Pitch, Note, rhythm

from numpy import append

rhythyms = [1, 3/4, 1/2, 3/8, 1/4, 3/16, 1/8, 1/16]

def rhythym_sceme(beats: int) -> List[Tuple[float, bool]] :
    to_return = []
    current = 0
    rest = 0
    while current != beats :
        is_rest = True
        if current + 1 <= beats:
            to_return.append((current + choice(rhythyms), is_rest))
        elif current + 3/4 <= beats:
            to_return.append((current + choice(rhythyms[1:]), is_rest))
        elif current + 1/2 <= beats:
            to_return.append((current + choice(rhythyms[:2]), is_rest))
        elif current + 3/8 <= beats:
            to_return.append((current + choice(rhythyms[:3]), is_rest))
        elif current + 1/4 <= beats:
            to_return.append((current + choice(rhythyms[:4]), is_rest))
        elif current + 3/16 <= beats:
            to_return.append((current + choice(rhythyms[:5]), is_rest))
        elif current + 1/8 <= beats:
            to_return.append((current + choice(rhythyms[:6]), is_rest))
        else:
            to_return.append((current + 1/16, is_rest))
    return to_return

def apply(score: Score, notes: List[Pitch], rhythyms: List[Tuple[float, bool]], tempo: int, inst: int) -> None:
    start = 0
    for notes in rhythyms:
        dur = rhythm(tempo, notes[1])
        if notes[0]:
            score.add(Note(start, dur, choice(notes), .5, inst))
        start += dur



        


   

if __name__ == "__main__":
    pass


