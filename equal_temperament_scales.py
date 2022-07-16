from multiprocessing.sharedctypes import Value
from tracemalloc import start
from typing import Union, List
from more_itertools import first
from musx import Interval, Pitch

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
    """
    This is class for representing scales that use equal temmperament tuning.

    Attributes: 
    type (str) -- Type of scale
    pcs (List[int]) -- Distance of each note from tonic in semitones
    tonic (Pitch) -- Tonic pitch
    intervals (List[Intervals]) -- Interval of each pitch from tonic
    pitches (List[Pitch]) -- list of pitches
    """

    def __init__(self, cls: Union[List[int], str], pitch: Pitch) -> None:
        """
        Constructor for ETScale class.

        Parameters:
        cls (List[int] or str) -- Computes scale using pcs (List[int]) or scale name (str)
        pitch (Pitch) -- Tonic of scale
        """
        if isinstance(cls, str) :
            self.type = cls.upper()
            self.pcs = ET_SCALES[self.type]
        else :
            self.type = 'Unnamed'
            self.pcs = cls
        self.tonic = pitch
        self.intervals = [BASE_INTERVALS[pc] for pc in self.pcs] 
        self.pitches = [interval.transpose(pitch) for interval in self.intervals]
        

    @staticmethod
    def tetrachord_subsitution(inferior: 'ETScale', superior: Union[List[int], 'ETScale']) -> 'ETScale':
        """
        Produces a new scale made up from two others using pre-20th century tetrachord subsitution.

        Parameters:
        inferior (ETScale) -- Provides tonic and uses inferior tetrachord in new scale
        superior (List[int] or ETScale) -- Uses superior tetrachord in new scale

        Returns:
        ETScale -- Equal tempered scale using inferior tetrachord from first parameter and superior tetrachord from second parameter
        """
        first_half = inferior.pcs
        second_half = superior
        if isinstance(superior, ETScale) :
            second_half = superior.pcs
        if 5 not in first_half or 7 not in second_half :
            raise ValueError('This function is based off of pre-20th century scale construction technqiues. The first scale must contain a perfect fourth and the second must have a perfect fifth.')
        return ETScale(first_half[:first_half.index(5)+1] + second_half[second_half.index(7):], inferior.tonic)

    def get_intervals(self) -> List[Interval]:
        """
        Returns intervals between scale degrees and tonic.

        Returns:
        List[Interval] -- An interval list of intervals of each scale degree in relevance to the tonic
        """
        return self.intervals

    def get_melodic_intervals(self) -> List[Interval]:
        """
        Returns melodic intervals between consecutive scale degrees.

        Returns:
        List[Interval] -- An interval list of consecutive scale degrees within the scale
        """
        return [BASE_INTERVALS[next - curr] for curr, next in zip(self.pcs, self.pcs[1:])]

    def get_pitches(self) -> List[Pitch]:
        """
        Returns pitches of the scale.

        Returns:
        List[Pitch] -- A list of the scale's pitches
        """
        return self.pitches

    def melodic_range(self, interval=Interval('P8'), scale_degree=1, start_above=True) -> List[Pitch]:
        """
        Returns pitches within range starting from scale degree, inclusive.

        Parameters:
        interval (Interval) -- List of pitches within interval range
        scale_degree (int) -- Scale degree to start on when computing melodic bounds
        start_above (bool) -- Whether or not starting scale degree is above/on (True) the scale's tonic or below (False)

        Returns:
        List[Pitch] -- A list of pitches diatonic to the scale that lie within the specified intervallic range
        """
        if interval.sign == -1:
            raise ValueError('Does not support negative interval ranges')
        idx = scale_degree - 1
        if idx < 0 or idx >= len(self.pitches):
            raise ValueError('Invalid scale degree')
        to_return = []
        semitones_traveled, octaves_traveled, semitone_range = 0, 0, interval.semitones()
        while semitones_traveled <= semitone_range:
            current_pitch = self.pitches[idx] if start_above else Interval('-P8').transpose(self.pitches[idx])
            for i in range(octaves_traveled):
                current_pitch = Interval('P8').transpose(current_pitch)
            to_return.append(current_pitch)
            if len(to_return) >= 2:
                semitones_traveled += current_pitch.keynum() - to_return[-2].keynum()
            idx += 1
            if idx >= len(self.pitches):
                idx = 0
                octaves_traveled += 1
        return to_return[:-1]



