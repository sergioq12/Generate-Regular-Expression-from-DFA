# Generate-Regular-Expression-from-DFA

This is my final project for a class called Theory of Computing.

The main concept of this class is to investigate the theoretical limitations of computers. Inside this theoretical investigation, we saw different models of computation. All models of computation shared some qualities they had:
- Languages
- Grammars
- Automata

We looked into one model of computing that is called a DFA (Deterministic Finite Automaton). In a general concept, this is a graph model of a computing prodecure that has several states and transitions. Regularly, there is an initial state and also a final state. In the middle, there are states that can be considered intermediate states. The scope of this project is to simplify a DFA to have only the initial state connected to the final state. The process of reduction contracts the transition making complex expressions. We called them Regular Expressions. Something probably every programmer has heard of, right?

Well, in brief, the program takes a textfile in the form:
- States
- Initial State
- Alphabet
- Transitions
- ...
- ...
- Final State

This will create a DFA, and then with the algorithm implemented, it will return and print back a Regular Expression
