% Hechos
actuo(dicaprio, inception).
actuo(dicaprio, titanic).
actuo(matthew, interestellar).

dirigida_por(inception, nolan).
dirigida_por(interestellar, nolan).

versatil(X) :-
    actuo(X, Y),
    dirigida_por(Y, nolan).