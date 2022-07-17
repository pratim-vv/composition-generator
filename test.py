from xml.etree.ElementTree import PI
from musx import Score, Note, Seq, MidiFile, Pitch, Interval
from musx.midi.gm import Trombone, TenorSax, Trumpet, MutedTrumpet, ElectricPiano1, ElectricPiano2
from random import choice
from equal_temperament_scales import ETScale
from chord import Chord
from structures import rhythym_scheme, apply

def play_scale(score, scale, inst) :
    current = 0
    pitches = scale.pitches
    for pitch in pitches :
        score.add(Note(time=current, duration=1, pitch=pitch, amplitude=1, instrument=inst))
        current += 1
    score.add(Note(time=current, duration=1, pitch=Interval('P8').transpose(scale.tonic), amplitude=1, instrument=inst))





if __name__ == '__main__' :
    """
    composition = Seq()
    instrumentation = MidiFile.metatrack(ins={0 : ElectricPiano1, 1 : ElectricPiano2, 2 : Trumpet, 3 : MutedTrumpet})
    score = Score(out=composition)
    scale2 = ETScale('minor', Pitch('C3'))
    print(scale2.melodic_range(interval=Interval('P12')))
    """
    scale1 = ETScale('major', Pitch('C3'))
    print(scale1.diatonic([Pitch('C3'), Pitch('D8')]))
    print(scale1.diatonic(Pitch('B#2')))
    print(scale1.diatonic(Pitch('B#2'), True))
    print(scale1.diatonic([Pitch('C3'), Pitch('B#6')]))
    
   # file = MidiFile('testing.midi', [instrumentation, composition]).write()
