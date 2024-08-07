import itertools
import random
from ConcurrentEnvironment.Graph import Graph


def generate_random_graph_complete(num_nodes: int, num_final_states: int, action_set1: set[str], action_set2: set[str]) -> (Graph, set[str]):
    g = Graph()
    state_names = [str(n) for n in range(num_nodes)]
    # add states
    for s in state_names:
        g.add_node(s)
    # mark states as final
    state_list = list(g.states.keys())
    final_states = set()
    for i in range(num_final_states):
        final_states.add(state_list[i])

    for s1 in state_list:
        for action1, action2 in itertools.product(action_set1, action_set2):
            if s1 in final_states:
                # add self loop to final states
                g.add_edge(s1, s1, action1, action2)
            else:
                # add random edge from non-final state to any state
                s2 = random.choice(state_list)
                g.add_edge(s1, s2, action1, action2)
    return g, final_states
