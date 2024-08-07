from State import State


class Graph:
    def __init__(self) -> None:
        # dict mapping strings of state_data to State objects
        self.states = dict()

        # creating sub-assignments as defined in the paper. (making it as a dictionary mapping states to moves.
        self.sub_assignment_1 = dict()
        self.sub_assignment_2 = dict()

    def add_node(self, state_data: str):
        self.states[state_data] = State(state_data)

    def add_edge(self, source: str, dest: str, action1: str, action2: str):
        self.states[source].add_out_node(dest, action1, action2)
        self.states[dest].add_in_node(source, action1, action2)

        # setting sub assignements as well.
        if source not in self.sub_assignment_1:
            self.sub_assignment_1[source] = set()
        self.sub_assignment_1[source].add(action1)

        if source not in self.sub_assignment_2:
            self.sub_assignment_2[source] = set()
        self.sub_assignment_2[source].add(action2)
        # self.states[source].add_sub_assignment(self.states[source], action1, action2)

    def print(self):
        for s in self.states:
            print(f"{s}: {self.states[s].out_neighbors}")