import random

from musical.theory import Note, Scale
from musical.audio import effect, playback

from timeline import Hit, Timeline

# Define key and scale
key = Note('C3')
scale = Scale(key, 'Major')

time = 0 # Keep track of currect note placement time in seconds

timeline = Timeline()

note = key

for x in xrange(0,11):

  if (x == 0):

    note = Note("C3")

  if (x == 1):

    note = random.choice([Note("D3"),Note("B2")])

  if (x == 2 ):
    if (note == Note("B2")):
      note = random.choice([Note("A2"),Note("C3")])

    if (note == Note("D3")):
      note = random.choice([Note("E3"),Note("C3")])

  if (x == 3 ):
    if (note == Note("A2")):
      note = random.choice([Note("G2"),Note("B2")])

    if (note == Note("C3")):
        note = random.choice([Note("B2"),Note("D3")])

    if (note == Note("E3")):
      note = random.choice([Note("D3"),Note("F3")])

  if (x == 4):
    if (note == Note("G2")):
      note = random.choice([Note("F2"),Note("A2")])

    if (note == Note("B2")):
      note = random.choice([Note("A2"),Note("C3")])

    if (note == Note("D3")):
      note = random.choice([Note("C3"),Note("E3")])

    if (note == Note("F3")):
      note = random.choice([Note("E3"),Note("G3")])

  if (x == 5):
    if (note == Note("F2")):
      note = Note("G2")

    if (note == Note("A2")):
      note = random.choice([Note("G2"),Note("B2")])

    if (note == Note("C3")):
      note = random.choice([Note("B2"),Note("D3")])

    if (note == Note("E3")):
      note = random.choice([Note("D3"),Note("F3")])

    if (note == Note("G3")):
      note = random.choice([Note("D3"),Note("F3")])

  if (x == 6):
    if (note == Note("G2")):
     note = random.choice([Note("F2"),Note("A2")])

    if (note == Note("B2")):
      note = random.choice([Note("A2"),Note("C3")])

    if (note == Note("D3")):
      note = random.choice([Note("C3"),Note("E3")])

    if (note == Note("F3")):
      note = random.choice([Note("E3"),Note("G3")])

  if (x == 7):
    if (note == Note("F2")):
      note = Note("G2")

    if (note == Note("A2")):
      note = random.choice([Note("G2"),Note("B2")])

    if (note ==Note("C3")):
      note = random.choice([Note("B2"),Note("D3")])

    if (note == Note ("E3")):
      note = random.choice([Note("D3"),Note("F3")])

    if (note == Note ("G3")):
      note = Note("F3")

  if (x == 8):
    if (note == Note("G2")):
      note = Note("A2")

    if (note == Note("B2")):
      note = random.choice([Note("A2"),Note("C3")])

    if (note == Note("D3")):
      note = random.choice([Note("C3"),Note("E3")])

    if (note == Note("F3")):
      note = Note("E3")

  if (x == 9):
    if (note == Note("A2")):
     note = Note("B2")

    if (note == Note("C3")):
     note = random.choice([Note("B2"),Note("D3")])

    if (note == Note("E3")):
      note = Note("D3") 

  if (x == 10):

    note = Note("C3")

  timeline.add(time, Hit(note, 1))

  time += 1

print "Rendering audio..."

data = timeline.render()

print "Playing audio..."

playback.play(data)

print "Done!"