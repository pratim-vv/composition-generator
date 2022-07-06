from typing import Union, List
from more_itertools import first
from musx import Interval, Pitch
from numpy import isin

ET_SCALES = {
    'MAJOR' : [0, 2, 4, 5, 7, 9, 11],
    'MINOR' : [0, 2, 3, 5, 7, 8, 10],
    'HARMONIC_MINOR' : [0, 2, 3, 5, 7, 8, 11],
    'MELODIC_MINOR' : [0, 2, 3, 5, 7, 9, 11, 10, 8],
    'CHROMATIC' : [pc for pc in range(12)],
    'WHOLE_TONE' : [0, 2, 4, 6, 8, 10],
    'AUGMENTED' : [0, 3, 4, 7, 8, 11],
    'PENTATONIC_MAJOR' : [0, 2, 4, 7, 9],
    'PENTATONIC_MINOR' : [0, 3, 5, 7, 10],

    'LYDIAN' : [0, 2, 4, 6, 7, 9, 11],
    'IONIAN' : [0, 2, 4, 5, 7, 9, 11],
    'MIXOLYDIAN' : [0, 2, 4, 5, 7, 9, 10],
    'DORIAN' : [0, 2, 3, 5, 7, 9, 10],
    'AEOLIAN' : [0, 2, 3, 5, 7, 8, 10],
    'PHRYGIAN' :[0, 1, 3, 5, 7, 8, 10],
    'LOCRIAN' : [0, 1, 3, 5, 6, 8, 10],

    'LYDIAN_AUGMENTED' : [0, 2, 4, 6, 8, 9, 11],
    'LYDIAN_DIMINISHED' : [0, 2, 3, 6, 7, 9, 11],
    'LYDIAN_FLAT_SEVENTH' : [0, 2, 4, 6, 7, 9, 10],
    'AUXILLARY_AUGMENTED' : [0, 2, 4, 6, 8, 10],
    'AUXILLARY_DIMINSHED' : [0, 2, 3, 5, 6, 8, 9, 11],
    'AUXILLARY_DIMINSHED_BLUES' : [0, 1, 3, 4, 6, 7, 9, 10],
    'MAJOR_FLAT_SEVENTH' : [0, 2, 4, 5, 7, 9, 11],
    'MAJOR_AUGMENTED_FIFTH' : [0, 2, 4, 5, 7, 8, 9, 11],
    'AFRICAN_AMERICAN_BLUES' : [0, 2, 3, 4, 5, 6, 7, 9, 10, 11],

    'RYU_KYU' : [0, 4, 5, 7, 11],
    'MIN_YO' :[0, 3, 5, 7, 10],
    'RITSU' :[0, 2, 5, 7, 9],
    'MIYAKO_BUSHI' : [0, 1, 5, 7, 8],

    'FLAMENCO' : [0, 1, 4, 5, 7, 8, 11]
}

BASE_INTERVALS = {
    0 : Interval('P1'),
    1 : Interval('m2'),
    2 : Interval('M2'),
    3 : Interval('m3'),
    4 : Interval('M3'),
    5 : Interval('P4'),
    6 : Interval('A4'),
    7 : Interval('P5'),
    8 : Interval('m6'),
    9 : Interval('M6'),
    10 : Interval('m7'),
    11 : Interval('M7'),
    12 : Interval('P8')
}

class ETScale(): 

    def __init__(self, cls: Union[List[int], str]) -> None:
        if isinstance(cls, str) :
            self.name = cls.upper()
            self.pcs = ET_SCALES[self.name]
        else :
            self.name = 'Unnamed'
            self.pcs = cls

    @staticmethod
    def tetrachord_subsitution(inferior: Union[List[int], 'ETScale'], superior: Union[List[int], 'ETScale']) -> List[int]:
        first_half = inferior
        second_half = superior
        if isinstance(inferior, ETScale) :
            first_half = inferior.pcs
        if isinstance(superior, ETScale) :
            second_half = superior.pcs
        if 5 not in first_half or 7 not in second_half :
            raise ValueError('This function is based off of pre-20th century scale construction technqiues. The first scale must contain a perfect fourth and the second must have a perfect fifth.')
        return first_half[:first_half.index(5)+1] + second_half[second_half.index(7):]

    def to_interval(self) -> List[Interval] :
        return [BASE_INTERVALS[pc] for pc in self.pcs]

    def melodic_intervals(self) -> List[Interval]:
        return [BASE_INTERVALS[next - curr] for curr, next in zip(self.pcs, self.pcs[1:])]

    def pitches(self, pitch:Union[Pitch, int, List[int], str]) -> List[Pitch] :
        degree_zero = pitch
        if not isinstance(pitch, Pitch):
            if isinstance(pitch, int) :
                degree_zero = Pitch.from_keynum(pitch)
            else:
                degree_zero = Pitch(pitch)
        return [interval.transpose(degree_zero) for interval in self.to_interval()]

