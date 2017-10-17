l = 0;

(
~chords = Pbind(

	\note, Pseq([[l,l+4,l+7], [l+2,l+5,l+9], [l+4,l+7,l+11],[l+5,l+9,l+12],[l+7,l+11,l+14],[l+9,l+12,l+16],[l+11,l+14,l+17],[l+12, l+16,l+19]], inf).collect(~chord = _),
	// this line here repeats over these sets of notes, aka chords
        \dur, 1
	// each chord plays for 1 second

);


~melody = Pbind(
        \note, Pn(Plazy { Pfin(4, Pshuf(~chord, inf)) }) + 12,
	// shuffles the notes in a chord, limits it to one output
        \dur, 0.3333333
);

x = Ptpar([0, ~chords, 0.0001, ~melody]).play
)

x.stop;  