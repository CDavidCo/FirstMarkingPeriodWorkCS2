import random

from musical.theory import Note, Scale
from musical.audio import effect, playback

from timeline import Hit, Timeline

timeline = Timeline()

bassProgression = [Note("C2"), Note("D2"), Note("E2"),Note("F2"),Note("G2"),Note("A2"),Note("B2"), Note("C3")]
chords = [[],
		  [Note("C3"),Note("E3"),Note("G3")],
		  [Note("D3"),Note("F3"),Note("A3")],
		  [Note("E3"),Note("G3"),Note("B3")],
		  [Note("F3"),Note("A3"),Note("C4")],
		  [Note("G3"),Note("B3"),Note("D4")],
		  [Note("A3"),Note("C4"),Note("E4")],
		  [Note("B3"),Note("D4"),Note("F4")],
		  [Note("C4"),Note("E4"),Note("G4")],
		  ]


key = bassProgression[0]
scale = Scale(key, 'major')

second = scale.transpose(key, 1)
third = scale.transpose(key, 2)
fourth = scale.transpose(key, 3)
sixth = scale.transpose(key, 5)
seventh = scale.transpose(key, 6)
octave = scale.transpose(key, 7)

for x in range(0,8):
	
	timeline.add(x*.5,Hit(bassProgression[x],1))
	bassNote = bassProgression[x]

	
	

	time = 0.0

	def nextNote(inputNote):

	
		if inputNote.note == "c":
			afterNote = "b%i" % (inputNote.octave - 1)
			afterNote = "d%i" % (inputNote.octave) 
		elif inputNote.note == "d":
			 afterNote = "c%i" % (inputNote.octave)
			 afterNote = "e%i" % (inputNote.octave) 
		elif inputNote.note == "e":
			 afterNote = "d%i" % (inputNote.octave)
			 afterNote = "f%i" % (inputNote.octave) 
		elif inputNote.note == "f":
			 afterNote = "e%i" % (inputNote.octave)
			 afterNote = "g%i" % (inputNote.octave) 
		elif inputNote.note == "g":
			 afterNote = "f%i" % (inputNote.octave)
			 afterNote = "a%i" % (inputNote.octave) 
		elif inputNote.note == "a":
			 afterNote = "g%i" % (inputNote.octave)
			 afterNote = "b%i" % (inputNote.octave) 
		else:
			 afterNote = "a%i" % (inputNote.octave)
			 afterNote = "c%i" % (inputNote.octave + 1) 

		return Note(afterNote)

melodyArray = []

bassNote = bassProgression[x]

melodyArray.append(bassNote)

#Definte Melody Array
for x in range(1,16):
    melodyArray.append(nextNote(melodyArray[x-1]))


time = 0.0
#Populate Timeline

for note in melodyArray:
    timeline.add(time,Hit(note,0.25))

    if (time*100) % 50 == 0:
        timeline.add(time,Hit(note,0.5))

    time += 0.25

data = timeline.render()

playback.play(data)