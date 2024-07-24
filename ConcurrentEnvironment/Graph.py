from State import State


class Graph:
    def __init__(self) -> None:
        # dict mapping strings of state_data to State objects
        self.states = dict()

    def add_node(self, state_data: str):
        self.states[state_data] = State(state_data)

    def add_edge(self, source: str, dest: str, action1: str, action2: str):
        self.states[source].add_out_node(dest, action1, action2)
        self.states[dest].add_in_node(source, action1, action2)
