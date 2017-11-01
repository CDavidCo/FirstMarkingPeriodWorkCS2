import random

from musical.theory import Note, Scale
from musical.audio import effect, playback

from timeline import Hit, Timeline

timeline = Timeline()
debug = False

bassProgression = [Note("C2"), Note("D2"), Note("F2"),Note("E2"),Note("F2"),Note("G2"),Note("A2"), Note("G2"),Note("E2"),Note("D2"), Note("C2")]

chordLetters = {
	"c" : ["c","e","g"],
	"d" : ["d","f","a"],
	"e" : ["e","g","b"],
	"f" : ["f","a","c"],
	"g" : ["g","b","d"],
	"a" : ["a","c","e"],
	"b" : ["b","d","f"]
}

key = bassProgression[0]
scale = Scale(key, 'major')

second = scale.transpose(key, 1)
third = scale.transpose(key, 2)
fourth = scale.transpose(key, 3)
sixth = scale.transpose(key, 5)
seventh = scale.transpose(key, 6)
octave = scale.transpose(key, 7)

def returnChord(note):
	return([scale.transpose(note,2),scale.transpose(note,0)])

def nextNote(prevNote, bassNote):
	#if 'c' chordNotes is set to [Note("C3"),Note("E3"),Note("G3")]
	chordNotes = chordLetters[bassNote.note]
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
	
	if (w) % 2 == 0:
	
		timeline.add((w/2)*.5,Hit(bassProgression[w/2],1))
		bassNote = bassProgression[w/2]


	bassNote = bassProgression[w/2]

	if w == 0:
		melodyArray = []
		melodyArray.append(Note(scale.transpose(bassNote,9)))
		bassArray = []
		bassArray.append(Note("C2"))
	
	#Define Melody Array
	bassArray.append(nextBassNote (bassArray[w-1]))

	melodyArray.append(nextNote(melodyArray[w-1],bassProgression[w%2]))
	


time = 0.0
#Populate Timeline

for note in melodyArray:

	timeline.add(time,Hit(note,0.25))

	if (time*100) % 50 == 0:
  		timeline.add(time,Hit(note,0.5))

   	time += 0.25

for note in bassArray:

	timeline.add(time,Hit(note,0.50))

	if (time*200) % 100 == 0:
  		timeline.add(time,Hit(note,0.5))

   	time += 0.25

data = timeline.render()

data = data * .3

playback.play(data)