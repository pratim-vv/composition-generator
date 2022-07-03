from musx import Pitch, Interval, Score, Note
from typing import List, Union

CHORD_SYMBOLS = {
    'M' : [Interval('M3'), Interval('P5')],
    'm' : [Interval('m3'), Interval('P5')],
    'd' : [Interval('m3'), Interval('d5')],
    'a' : [Interval('M3'), Interval('+5')],

    'M7' : [Interval('M3'), Interval('P5'), Interval('M7')],
    'Mm7' : [Interval('M3'), Interval('P5'), Interval('m7')],
    'm7' : [Interval('m3'), Interval('P5'), Interval('m7')],
    'hd7' : [Interval('m3'), Interval('d5'), Interval('m7')]
}

class Chord():

    def __init__(self, cls: Pitch, arg: str) -> None:
        self.root = cls
        intervals_from_root = CHORD_SYMBOLS[arg]
        self.pitches = [cls]
        for interval in intervals_from_root:
            self.pitches.append(interval.transpose(cls))

    def implement(self, score: Score, time: float, duration: float, amplitude: float, instruments: Union[int, List[int]]) -> None:
        if isinstance(instruments, int) :
            instruments = [instruments]
        pitch_idx = 0
        curr_octave = 0
        for inst in instruments :
            transpose_by = Interval('P' + str(1 + 7 * curr_octave))
            pitch = transpose_by.transpose(self.pitches[pitch_idx])
            score.add(Note(time, duration, pitch, amplitude, inst))
            pitch_idx += 1
            if pitch_idx >= len(self.pitches) :
                curr_octave += 1
                pitch_idx = 0

    def arpeggiate(self, score: Score, start: float, length: float, instances: int, amplitude=0.5, instrument=0) -> None:
        for i in range(instances) :
            for pitch in self.pitches:
                score.add(Note(start, length, pitch, amplitude, instrument))
                start += length




    def chord_tone(self, pitch: Union[Pitch, int, str]) -> bool :
        if not isinstance(pitch, Pitch) :
            pitch = Pitch(pitch)
        for p in self.pitches :
            if p.pc() == pitch.pc() :
                return True
        return False


