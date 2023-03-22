# Deterministic Finite Automaton
class DFA:
    def __init__(self, S, A, d, s0, F):
        self.states = S
        self.alphabet = A
        self.transition_table = d
        self.start_state = s0
        self.final_states = F
 
    def delta(self, state, word):
        return self.transition_table[self.states.index(state)][self.alphabet.index(word)]
 
    def delta_circumflex(self, state, word_list):
        if not word_list:
            return state
        else:
            return self.delta(self.delta_circumflex(state, word_list[:-1]), word_list[-1])
 
    def run(self, words):
        return self.delta_circumflex(self.start_state, [word for word in words]) in self.final_states
