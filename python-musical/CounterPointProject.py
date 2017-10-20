import random

from musical.theory import Note, Scale
from musical.audio import effect, playback

from timeline import Hit, Timeline


# Define key and scale
key = Note('C3')
scale = Scale(key, 'Major')

time = 0.0 # Keep track of currect note placement time in seconds

timeline = Timeline()

note = key

for x in xrange(0,12):

  if note.index == "C3":
    note = random.choice(C3, D3)
  
  if note.index == "D3":
    note = random.choice(D3, E3, C3)
  

  if note.index == "E3":
    note = random.choice(E3, F3, D3)
  

  if note.index == "F3" :
    note = random.choice(F3, G3, E3)
  

  if note.index == "G3" :
    note = random.choice(G3, A3, F3)
  

  if note.index == "A3":
    note = random.choice(A3, B3, G3)
  

  if note.index == "B3":
    note = random.choice(B3, C3, A3)


  if note.index == "C4":
    note = random.choice(B3, C4)

  print "Playing audio..."

  data = timeline.render()

  playback.play(data)

  print "Done!"

  timeline.add(time, Hit(note, 1))





# Resolve



print "Rendering audio..."




print "Playing audio..."

playback.play(data)

print "Done!"