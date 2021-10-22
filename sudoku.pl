not_in_list(_, []).
not_in_list(Elm, [Head|Tail]) :- Elm \= Head, not_in_list(Elm, Tail).