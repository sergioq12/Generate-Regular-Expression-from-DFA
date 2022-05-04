from DFA import DFA
from itertools import product
import pprint

def getData(filename):
    """
    Action: This function will get the data entered given by the textfile
    """
    lines = []
    with open(filename, "r") as f:
        for line in f.readlines():
            lines.append(line)

    for i in range(len(lines)):
        line = lines[i].split()
        lines[i]=line       
    return lines

def intermediateStateProcess(dfa, intermediateStates):
     # For each intermediate state, we need:
    for state in intermediateStates:
        # get the state that goes into the intermediate state
        intoTransitions = dfa.getTransitionsIntoState(state)
        # print(f"Into Transitions: {intoTransitions}")
        # and the possible options that the intermediate state goes to
        outOfTransitions = dfa.getTransitionsOutOfState(state)
        # print(f"outOf Transitions: {outOfTransitions}")
        # get the cartesian product of possible options
        possible_transitions = list(product(intoTransitions, outOfTransitions))
        # for each cartesian product, try to check if the transition already exists
        # pprint.pp(possible_transitions)
        for cartProd in possible_transitions:
            # print((cartProd[0][0], cartProd[1][2]), dfa.checkIfTransitionExists(cartProd[0][0], cartProd[1][2]))
            # start to create the expression that will be used in the new transition
            repeats, character = dfa.checkIfIntermediateRepeats(state)
            if repeats:
                expression = str(cartProd[0][1]) + str(character)+"*" + str(cartProd[1][1])
            else: expression = cartProd[0][1] + cartProd[1][1]

            if dfa.checkIfTransitionExists(cartProd[0][0], cartProd[1][2]):
                # update the expression connecting the product
                transition = [cartProd[0][0], expression, cartProd[1][2]]
                dfa.updateTransition(transition)
                # print("Updated Happening")
            else:
                # expression has been created, now implement it into the DFA
                transition = [cartProd[0][0], expression, cartProd[1][2]]
                # create the transition
                dfa.createTransition(transition)
                # print("Transition Created")
            # print(dfa)

        # after all happening with that intermediate state we need:
        # delete the intermediate state
        dfa.deleteState(state)
        # delete the transitions to the intermediate state
        dfa.deleteTransitionsToState(state)
    print(f"\n\nFinal DFA: \n\n{dfa}")
    return dfa

def toRegEx(dfa):
    """
    Action: This function will convert the DFA into a regular Expression
    return: a string consisting of the regular expression
    """

    # Get the intermediate states 
    intermediateStates = dfa.getIntermediateStates()
    # print(f"Intermediate states: {intermediateStates}")
    # transform the intermediate state transitions into a new DFA
    dfa = intermediateStateProcess(dfa, intermediateStates)
    # get the final regular expression
    return dfa.getFinalRegularExpression()


def main():
    inputData = getData("example.txt")
    dfa = DFA(inputData)
    dfa.createDFA()
    regularExpression = toRegEx(dfa)
    print(f"Final Regular Expression: \n\n\t{regularExpression}\n\n")

if __name__ == "__main__":
    main()