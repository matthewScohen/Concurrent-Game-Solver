from ConcurrentEnvironment.Graph import Graph
from ConcurrentEnvironment.State import State


def experimental_solver(graph: Graph, final_states: set[str]) -> (set[State], dict[State, str]):
    winning_region = set()
    strategy = dict()
    return winning_region, strategy
