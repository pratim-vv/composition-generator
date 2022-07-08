from xml.etree.ElementTree import PI
from musx import Score, Note, Seq, MidiFile, Pitch
from musx.midi.gm import Trombone, TenorSax, Trumpet, MutedTrumpet
from random import choice
from equal_temperament_scales import ETScale
from chord import Chord

def play_scale(score, scale, tonic, inst) :
    if isinstance(scale, ETScale):
        scale = scale.pcs
    for idx, p in enumerate(scale) :
        score.add(Note(time=idx, duration=1, pitch=tonic+p, amplitude=0.5, instrument=inst))
    score.add(Note(time=len(scale), duration=1, pitch=tonic+12, amplitude=0.5, instrument=inst))





if __name__ == '__main__' :
    composition = Seq()
    instrumentation = MidiFile.metatrack(ins={0 : Trombone, 1 : TenorSax, 2 : Trumpet, 3 : MutedTrumpet})
    score = Score(out=composition)
    #scale = ETScale('pentatonic_major')
    #play_scale(score, scale, 66, 0)
    #play_scale(score, scale, 66+12, 1)
    chord = Chord(Pitch('C3'), 'M9')
    #chord.implement(score, 0, 1, .5, [i for i in range(4)])
    #Chord(Pitch.from_keynum(50), "m7").implement(score, 1, 1, .5, [i for i in range(4)])
    #Chord(Pitch.from_keynum(53), "M").implement(score, 2, 1, .5, [i for i in range(4)])
    #Chord(Pitch.from_keynum(55), "Mm7").implement(score, 3, 1, .5, [i for i in range(4)])
    #Chord(Pitch.from_keynum(57), "m").implement(score, 4, 1, .5, [i for i in range(4)])
    chord.arpeggiate(score, 0, .25, 4)
    Chord(Pitch('F3'), 'M7').arpeggiate(score, 3, .25, 4)
    Chord(Pitch('G3'), 'M').arpeggiate(score, 6, .25, 4)
    chord.implement(score, 9, 4, .5, [0, 1])
    file = MidiFile('testing.midi', [instrumentation, composition]).write()
