import itertools
from typing import List, Tuple
from random import choice
from musx import Score, Pitch, Note, rhythm

from numpy import append

rhythyms = [1, 3/4, 1/2, 3/8, 1/4, 3/16, 1/8, 1/16]

def rhythym_scheme(beats: float) -> List[Tuple[float, bool]] :
    to_return = []
    current = 0.0
    rest = 0
    #update current
    while current != beats :
        is_rest = True
        idx = 7
        if current + 1 <= beats:
            idx = 0
        elif current + 3/4 <= beats:
            idx = 1
        elif current + 1/2 <= beats:
            idx = 2
        elif current + 3/8 <= beats:
            idx = 3
        elif current + 1/4 <= beats:
            idx = 4
        elif current + 3/16 <= beats:
            idx = 5
        elif current + 1/8 <= beats:
            idx = 6
        chosen = choice(rhythyms[idx:])
        current += chosen
        to_return.append((is_rest, chosen))
    return to_return

def apply(score: Score, notes: List[Pitch], rhythyms: List[Tuple[float, bool]], tempo: float, inst: int, start=0.0) -> None:
    for rhy in rhythyms:
        dur = ((tempo / rhy[1]) / 60.0) ** -1
        if rhy[0]:
            score.add(Note(start, dur, choice(notes), .5, inst))
        start += dur

def range_to_melody(number: int, breadth: List[Pitch], start=None) -> List[Pitch]:
    if start is None:
        start = breadth[0]
    melody = [start]
    midi_keys = {}
    for pitch in breadth:
        midi_keys[pitch.keynum()] = pitch
    direction = (0, 0) #number of intervals in direction, -1 for down 1 for up
    fifth = True
    unison = True
    recovery = (False, 'step')
    for i in range(number-1):
        valid_keys = []
        past_pitch = melody[-1].keynum()
        if recovery[0]:
            if recovery[1] == 'step':
                if direction[1] == -1:
                    pass                    



                








        


   

if __name__ == "__main__":
    pass


