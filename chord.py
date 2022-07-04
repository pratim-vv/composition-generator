from musx import Pitch, Interval, Score, Note
from typing import List, Union

from numpy import isin

CHORD_SYMBOLS = {
    'M' : [Interval('P1'), Interval('M3'), Interval('P5')],
    'm' : [Interval('P1'), Interval('m3'), Interval('P5')],
    'd' : [Interval('P1'), Interval('m3'), Interval('d5')],
    'a' : [Interval('P1'), Interval('M3'), Interval('+5')],
    'aug' : [Interval('P1'), Interval('M3'), Interval('+5')],

    'm6' : [Interval('P1'), Interval('m3'), Interval('P5'), Interval('M6')],

    'M7' : [Interval('P1'), Interval('M3'), Interval('P5'), Interval('M7')],
    'Mm7' : [Interval('P1'), Interval('M3'), Interval('P5'), Interval('m7')],
    'm7' : [Interval('P1'), Interval('m3'), Interval('P5'), Interval('m7')],
    'hd7' : [Interval('P1'), Interval('m3'), Interval('d5'), Interval('m7')],
    'fd7' : [Interval('P1'), Interval('m3'), Interval('d5'), Interval('d7')],
    'Mm7b5' : [Interval('P1'), Interval('M3'), Interval('d5'), Interval('m7')],
    'a7' : [Interval('P1'), Interval('M3'), Interval('+5'), Interval('m7')],
    'aug7' : [Interval('P1'), Interval('M3'), Interval('+5'), Interval('m7')],
    'M7b5' : [Interval('P1'), Interval('M3'), Interval('d5'), Interval('M7')]

}

class Chord():

    def __init__(self, cls: Pitch, arg: str) -> None:
        self.root = cls
        intervals_from_root = CHORD_SYMBOLS[arg]
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

    def nearest_chord_tone(self, pitch: Union[Pitch, int, str]) -> Pitch :
        if not isinstance(pitch, Pitch) :
            pitch = Pitch(pitch)
        midis = [p.keynum() for p in self.pitches]
        pcs = [midi % 12 for midi in midis]
        current_midi = pitch.keynum()
        current_pc = current_midi % 12
        octave_difference = current_midi - midis[pcs.index(current_pc)]
        if current_pc in pcs :
            if octave_difference >= 0 :
                return Interval('P' + str(1 + 7 * octave_difference)).transpose(self.pitches[pcs.index(current_pc)])
            return Interval('-P' + (str(1 + -7 * octave_difference))).transpose(self.pitches[pcs.index(current_pc)])
