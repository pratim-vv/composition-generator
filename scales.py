
MAJOR = [0, 2, 4, 5, 7, 9, 11]
MINOR = [0, 2, 3, 5, 7, 8, 10]
HARMONIC_MINOR = [0, 2, 3, 5, 7, 8, 11]
MELODIC_MINOR = [0, 2, 3, 5, 7, 9, 11, 10, 8]
CHROMATIC = [pc for pc in range(12)]
WHOLE_TONE = [0, 2, 4, 6, 8, 10]
AUGMENTED = [0, 3, 4, 7, 8, 11]
PENTATONIC_MAJOR = [0, 2, 4, 7, 9]
PENTATONIC_MINOR = [0, 3, 5, 7, 10]



LYDIAN = [0, 2, 4, 6, 7, 9, 11]
IONIAN = MAJOR
MIXOLYDIAN = [0, 2, 4, 5, 7, 9, 10]
DORIAN = [0, 2, 3, 5, 7, 9, 10]
AEOLIAN = MINOR
PHRYGIAN =[0, 1, 3, 5, 7, 8, 10]
LOCRIAN = [0, 1, 3, 5, 6, 8, 10]

RYU_KYU = [0, 4, 5, 7, 11]
MIN_YO =[0, 3, 5, 7, 10]
RITSU =[0, 2, 5, 7, 9]
MIYAKO_BUSHI = [0, 1, 5, 7, 8]


FLAMENCO = [0, 1, 4, 5, 7, 8, 11]


PC_SCALES =[

    MAJOR,
    MINOR,
    HARMONIC_MINOR,
    MELODIC_MINOR,
    CHROMATIC,
    WHOLE_TONE,
    AUGMENTED,
    PENTATONIC_MAJOR,
    PENTATONIC_MINOR,

    LYDIAN,
    IONIAN,
    MIXOLYDIAN,
    DORIAN,
    AEOLIAN,
    PHRYGIAN,
    LOCRIAN,

    RYU_KYU,
    MIN_YO,
    RITSU,
    MIYAKO_BUSHI,
    
    FLAMENCO]

class Scale(): 

    def __init__(self) -> None:
        pass
