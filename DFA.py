from typing import final


class DFA():
    def __init__(self, inputData) -> None:
        self.states = inputData[0]
        self.initialState = inputData[1]
        self.alphabet = inputData[2]
        self.transitions = inputData[3:-1]
        self.final_states = inputData[-1]
        self.DFA_graph = {}
        self.createDFA

    def createDFA(self):
        for state in self.states:
            if state in self.initialState:
                self.DFA_graph[state] = {"initial": True, "final":False}
            elif state in self.final_states:
                self.DFA_graph[state] = {"initial": False, "final": True}
            else:
                self.DFA_graph[state] = {"initial": False, "final": False}


        for transition in self.transitions:
            # print(transition)
            initialState, character, endState = transition
            self.DFA_graph[str(initialState)][str(character)] = endState   

    def deleteState(self, state):
        del self.DFA_graph[state]

    def deleteTransitionsToState(self, state):
        """
        Action: this function will delete all transitions to a certain state
        """
        transitions_to_delete = []
        for currState in self.DFA_graph:
            for trans in self.DFA_graph[currState]:
                if self.DFA_graph[currState][trans] == state:
                    transitions_to_delete.append([currState, trans, state])

        for transition in transitions_to_delete:
            # delete transitions from graph
            del self.DFA_graph[transition[0]][transition[1]]
            # delete transition from transitions self
            if transition in self.transitions:
                self.transitions.remove(transition) 

    def createTransition(self, transition):
        """
        Action: This function will create a transition in the internal graph
        """
        state_from, expression, state_to = transition
        self.DFA_graph[state_from][expression] = state_to

        # add the new transitions to self.traansitions
        self.transitions.append(transition)

    def updateTransition(self, transition):
        """
        Action: This function will update a transition that already exists.
        """
        state_from, new_expression, state_to = transition
        # get current expression
        for trans in self.transitions:
            if trans[0] == state_from and trans[2] == state_to:
                previous_expression = trans[1]
        expression = f"{previous_expression} + {new_expression}"
        self.DFA_graph[state_from][expression] = state_to

        # delete the previous transition in order to leave the new one
        del self.DFA_graph[state_from][previous_expression]

        # add the new transitions to self.traansitions
        self.transitions.append(transition)

    def getIntermediateStates(self):
        intermediateStates = []
        for node in self.DFA_graph:
            if not self.DFA_graph[node]["initial"] and not self.DFA_graph[node]["final"]:
                intermediateStates.append(node)

        return intermediateStates

    def checkIfIntermediateRepeats(self,state):
        for transition in self.transitions:
            if transition[0] == state and transition[2] == state:
                return True, transition[1]
        return False, None

    def getTransitionsIntoState(self, state):
        """
        Action: this will get the states that transition into the state given
        """
        statesInto = []
        for transition in self.transitions:
            # make sure to not include a transition to itself
            if transition[2] == state:
                if transition[0] != state:
                    statesInto.append(transition)
        
        return statesInto

    def getTransitionsOutOfState(self, state):
        """
        Action: this will get the states that transition into the state given
        """
        statesOutOf = []
        for transition in self.transitions:
            # make sure to not include a transition to itself
            if transition[0] == state:
                if transition[2] != state:
                    statesOutOf.append(transition)
        
        return statesOutOf

    def checkIfTransitionExists(self, state_from, state_to):
        for transition in self.transitions:
            if transition[0] == state_from and transition[2] == state_to:
                return True
        return False

    def getFinalRegularExpression(self):
        """
        Action: This function will return the regular expression for the DFA
        """ 
        initialState = self.initialState[0]
        finalState = self.final_states[0]
        expression = ""
        # check if the initial state has a transition to itself
        for transition in self.DFA_graph[initialState]:
            if self.DFA_graph[initialState][transition] == initialState:
                expression += f"{transition}*"
                break
        # add the transition to the end
        for transition in self.DFA_graph[initialState]:
            if self.DFA_graph[initialState][transition] == finalState:
                if "+" in transition:
                    expression += f"({transition})"
                else:
                    expression += f"{transition}"
                break

        # check if transition to end repeats
        for transition in self.DFA_graph[finalState]:
            if self.DFA_graph[finalState][transition] == finalState:
                expression += f"({transition})*"
                break

        # now we look if the final state can go back to the initial state
        for transition in self.DFA_graph[finalState]:
            if self.DFA_graph[finalState][transition] == initialState:
                expression += f"[({transition}){expression}]*"
                break

        return expression

    def __repr__(self):
        string = ""
        for state in self.DFA_graph:
            string += f"{state}: {str(self.DFA_graph[state])}\n"
        return string

    def getDFAInformation(self):
        string = f"States: {str(self.states)}\n"
        string += f"Initial State: {str(self.initialState)}\n"
        string += f"Alphabet: {str(self.alphabet)}\n"
        string += "Transitions: \n"
        for transition in self.transitions:
            string += f"{str(transition)}\n"
        string += f"Final States: {str(self.final_states)}\n"
        return string

