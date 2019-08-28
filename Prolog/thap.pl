mv(X,Y):-write('Move top disk from '),write(X),write(' to '),write(Y),nl.
move(1,X,_,Z):-mv(X,Z).
move(N,X,Y,Z):-N>1,N1 is N-1,move(N1,X,Z,Y),mv(X,Z),move(N1,Y,X,Z).
