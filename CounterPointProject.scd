
~note = 0;

~cantusFirmus = Pbind(

	if(~note == -1, { ~up = 1; ~down = -2});
	if(~note == 0, { ~up = 2; ~down = -1});
	if(~note == 2, { ~up = 2; ~down = -2});
	if(~note == 4, { ~up = 1; ~down = -2});
	if(~note == 5, { ~up = 2; ~down = -1});
	if(~note == 7, { ~up = 2; ~down = -2});
	if(~note == 9, { ~up = 2; ~down = -2});
	if(~note == 11, { ~up = 1; ~down = -2});
	if(~note == 12, { ~up = 2; ~down = -1});

    ~interval = Prand([~down,0,~up],1);

	\note, Pseq([~note + ~interval], inf).trace,

	~up = 0;
	~down = 0;


	// shuffles the notes in a chord, limits it to one output, puts it in a pattern, and assigns it the melody
	\dur,   1,
	//each chord plays eithr a quarter note, half note, or whole note

);


x = Ptpar([0, ~cantusFirmus]).play





//makes so the events occur at the same time, with the 0's representing any delay.

x.stop;