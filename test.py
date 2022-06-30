from musx import Score, Note, Seq, MidiFile
from musx.midi.gm import Viola, Violin
from random import choice
from equal_temperament_scales import ET_SCALES

def melody(score, tonic, amount: int, inst) :
    scale = choice(ET_SCALES.items())
    for i in range(amount) :
        next_pitch = choice(scale)
        score.add(Note(time=i, duration=1, pitch=tonic+next_pitch, amplitude=0.5, instrument=inst))




if __name__ == '__main__' :
    composition = Seq()
    instrumentation = MidiFile.metatrack(ins={0 : Viola, 1 : Violin})
    score = Score(out=composition)
    melody(score, 60, 12, 1)
    file = MidiFile('test.midi', [instrumentation, composition]).write()