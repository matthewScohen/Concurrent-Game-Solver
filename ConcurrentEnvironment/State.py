class State:
    def __init__(self, state_data: str) -> None:
        self.state_data = state_data
        # integers refer to a location in graph of the in/out states
        # out_nodes[action1][action2] = list(State)
        self.out_neighbors = dict()
        # out_nodes[action][action2] = list(State)
        self.in_neighbors = dict()

    def add_in_node(self, state: 'State', action1: str, action2: str):
        if action1 not in self.in_neighbors:
            self.in_neighbors[action1] = dict()
        if action2 not in self.in_neighbors[action1]:
            self.in_neighbors[action1][action2] = dict()
        self.in_neighbors[action1][action2] = state

    def add_out_node(self, state: 'State', action1: str, action2: str):
        if action1 not in self.out_neighbors:
            self.out_neighbors[action1] = dict()
        if action2 not in self.out_neighbors[action1]:
            self.out_neighbors[action1][action2] = dict()
        self.out_neighbors[action1][action2] = state

