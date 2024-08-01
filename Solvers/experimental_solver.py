from collections import defaultdict
from ConcurrentEnvironment.Graph import Graph
from ConcurrentEnvironment.State import State


def experimental_solver(graph: Graph, final_states: set[str]) -> (set[State], dict[State, str]):
    winning_region = list()
    strategy = defaultdict(list)

    # A mapping of all states to a count indicating how many edges must be removed for each possible action
    # when an action has 0 edges left to eliminate the state can be added to the attractor and the action becomes the
    # strategy at that state
    state_map = dict()
    # initialize all action counts
    for state_data, state in graph.states.items():
        state_map[state_data] = dict()
        # if a state is a final state then no actions need to be eliminated (since it is already in the attractor)
        if state_data in final_states:
            winning_region.append(state)
            for action1, _ in state.out_neighbors.items():
                state_map[state_data][action1] = 0
        # if a state is not a final state initialize each action count to the number of outgoing edges that action has
        else:
            for action1, action2_dict in state.out_neighbors.items():
                state_map[state_data][action1] = len(action2_dict.keys())

    # attractor iterations
    index = 0
    while index < len(winning_region):
        # iterate over all incoming states to new attractor states
        for action1, action2_dict in graph.states[winning_region[index].state_data].in_neighbors.items():
            for action2, source in action2_dict.items():
                if state_map[source][action1] == 0:
                    raise Exception("Attempted to eliminate edge from state-action pair that is already marked "
                                    "winning. Make sure final states have no out-going edges.")
                state_map[source][action1] -= 1
                # if all edges for an action are eliminated then the state can be added to the winning region
                if state_map[source][action1] == 0:
                    # a state can already be in the winning region if it has another action that makes it winning
                    if source not in winning_region:
                        winning_region.append(graph.states[source])
                    # the action with all eliminated edges can be added to the strategy list at that state
                    strategy[source].append(action1)
        index += 1
    return winning_region, strategy
