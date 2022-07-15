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
    composition = Seq()
    instrumentation = MidiFile.metatrack(ins={0 : ElectricPiano1, 1 : ElectricPiano2, 2 : Trumpet, 3 : MutedTrumpet})
    score = Score(out=composition)
    scale1 = ETScale('major', Pitch('C3'))
    scale2 = ETScale('minor', Pitch('C3'))

    #play_scale(score, ETScale.tetrachord_subsitution(scale1, scale2), 2)
    print(scale1.get_pitches())
    print(ETScale.tetrachord_subsitution.__doc__)
    
   # file = MidiFile('testing.midi', [instrumentation, composition]).write()
