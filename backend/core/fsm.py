# G := (x_0, X, X_marked, E, f)


class FSM:
    def __init__(
        self, initial_state, states, marked_states, events, transition_function
    ):
        self.initial_state = initial_state
        self.states = states
        self.marked_states = marked_states
        self.events = events
        self.transition_function = transition_function

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def get_initial_state(self):
        return self.initial_state

    def set_states(self, states):
        self.states = states

    def get_states(self):
        return self.states

    def set_marked_states(self, marked_states):
        self.marked_states = marked_states

    def get_marked_states(self):
        return self.marked_states

    def set_events(self, events):
        self.events = events

    def get_events(self):
        return self.events

    def set_transition_function(self, transition_function):
        self.transition_function = transition_function

    def run(self):
        current_state = self.initial_state
        for event in self.events:
            print(
                f"({current_state} x {event}) -> {self.transition_function[(current_state, event)]}"
            )
            current_state = self.transition_function[(current_state, event)]
        return current_state
