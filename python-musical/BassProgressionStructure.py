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
bassNote = bassProgression


for x in range(0,8):
	
	timeline.add(x*.5,Hit(bassProgression[x],1))
	

time = 0.0

def getChord(inputNote):
	returnChord = []

	print inputNote.note

	if inputNote.note == "c":
		returnChord = chords[1]
	elif inputNote.note == "d":
		returnChord = chords[2]
	elif inputNote.note == "e":
		returnChord = chords[3]
	elif inputNote.note == "f":
		returnChord = chords[4]
	elif inputNote.note == "g":
		returnChord = chords[5]
	elif inputNote.note == "a":
		returnChord = chords[6]
	else:
		returnChord = chords[7]
	
	return returnChord

def getAdjacentNotes(inputNote):

	if inputNote.note == "c":
		noteBelow = "b%i" % (inputNote.octave - 1)
		noteAbove = "d%i" % (inputNote.octave) 
	elif inputNote.note == "d":
		noteBelow = "c%i" % (inputNote.octave)
		noteAbove = "e%i" % (inputNote.octave) 
	elif inputNote.note == "e":
		noteBelow = "d%i" % (inputNote.octave)
		noteAbove = "f%i" % (inputNote.octave) 
	elif inputNote.note == "f":
		noteBelow = "e%i" % (inputNote.octave)
		noteAbove = "g%i" % (inputNote.octave) 
	elif inputNote.note == "g":
		noteBelow = "f%i" % (inputNote.octave)
		noteAbove = "a%i" % (inputNote.octave) 
	elif inputNote.note == "a":
		noteBelow = "g%i" % (inputNote.octave)
		noteAbove = "b%i" % (inputNote.octave) 
	else:
		noteBelow = "a%i" % (inputNote.octave)
		noteAbove = "c%i" % (inputNote.octave + 1) 

	return [Note(noteBelow),Note(noteAbove)]

melodyArray = []

bassNote = bassProgression[x]

melodyArray.append(random.choice(getChord(bassNote)))

#Definte Melody Array
for x in range(1,16):
    melodyArray.append(random.choice(getAdjacentNotes(melodyArray[x-1])))

time = 0.0
#Populate Timeline
for note in melodyArray:
    timeline.add(time,Hit(note,0.25))

    if (time*100) % 50 == 0:
        timeline.add(time,Hit(note,0.5))

    time += 0.25

data = timeline.render()

playback.play(data)