import random

from musical.theory import Note, Scale
from musical.audio import effect, playback

from timeline import Hit, Timeline

timeline = Timeline()
debug = False

bassArray = []

chordLetters = {
	"c" : ["c","e","g"],
	"d" : ["d","f","a"],
	"e" : ["e","g","b"],
	"f" : ["f","a","c"],
	"g" : ["g","b","d"],
	"a" : ["a","c","e"],
	"b" : ["b","d","f"]
}

key = Note("C3")
scale = Scale(key, 'major')


def returnChord(note):
	return([scale.transpose(note,2),scale.transpose(note,0)])

def nextNote(prevNote, bassNote):
	#if 'c' chordNotes is set to [Note("C3"),Note("E3"),Note("G3")]
	chordNotes = chordLetters[bassNote.note]
	print(chordNotes
		)
	possibleNext = []

	possibleNext.append(scale.transpose(prevNote,1))
	possibleNext.append(scale.transpose(prevNote,-1))

	if scale.transpose(prevNote,2).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,2))

	if scale.transpose(prevNote,-2).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,-2))

	if scale.transpose(prevNote,3).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,3))

	if scale.transpose(prevNote,-3).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,-3))

	if scale.transpose(prevNote,4).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,4))

	if scale.transpose(prevNote,-4).note in chordNotes :
		possibleNext.append(scale.transpose(prevNote,-4))

	return random.choice(possibleNext)


def nextBassNote(inputNote):

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

	return(random.choice([Note(noteBelow),Note(noteAbove)]))


for w in range(0,22):
	if w == 0:
		melodyArray = []
		bassArray = []
		bassArray.append(Note("C2"))
		melodyArray.append(Note(scale.transpose(bassArray[0],9)))
		

	if (w % 2 == 0):

		timeline.add((w/2)*.5,Hit(bassArray[w/2],1))
		bassNote = bassArray[w/2]

	
	
	#Define Melody Array
	bassArray.append(nextBassNote(bassArray[w/2-1]))

	melodyArray.append(nextNote(melodyArray[w-1],bassArray[w%2]))
	


time = 0.0
#Populate Timeline

for note in melodyArray:

	timeline.add(time,Hit(note,0.25))

   	time += 0.25


data = timeline.render()

data = data * .3

playback.play(data)