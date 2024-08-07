from ConcurrentEnvironment import State
from ConcurrentEnvironment.Graph import Graph
import copy


def traditional_solver(graph: Graph, final_states: set[str]) -> (set[State], dict[State, str]):
    winning_region, strategy_1 = almost_sure_solver(graph, final_states)
    return winning_region, strategy_1


def stay(player: int, state: str, target_set, graph: Graph, gamma_1: dict, gamma_2: dict):
    stay_action_set = set()
    if player == 1:
        for a1 in gamma_1[state]:
            if all(set(graph.states[state].out_neighbors[a1][a2]).issubset(target_set) for a2 in gamma_2[state]):
                stay_action_set.add(a1)
    if player == 2:
        for a2 in gamma_2[state]:
            if all(graph.states[state].out_neighbors[a1][a2].issubset(target_set) for a1 in gamma_1[state]):
                stay_action_set.add(a2)

    return stay_action_set


def pre(player: int, target_set, graph: Graph, gamma_1: dict, gamma_2: dict):
    if player == 1:
        return {state_data for state_data, s in graph.states.items() if any(
            all(set(s.out_neighbors[a1][a2]).issubset(target_set) for a2 in gamma_2[state_data]) for a1 in
            gamma_1[state_data])}
    elif player == 2:
        return {state_data for state_data, s in graph.states.items() if any(
            all(set(s.out_neighbors[a1][a2]).issubset(target_set) for a1 in gamma_1[state_data]) for a2 in
            gamma_2[state_data])}


def safe(player: int, graph: Graph, target_set, gamma_1: dict, gamma_2: dict):
    V_k = target_set
    while True:
        V_k_next = V_k.intersection(pre(player, V_k, graph, gamma_1, gamma_2))

        if V_k_next == V_k:
            break
        V_k = V_k_next

    return V_k


def almost_sure_solver(graph: Graph, final_states):
    U_k = set(graph.states.keys())
    gamma_1 = graph.sub_assignment_1
    gamma_2 = graph.sub_assignment_2

    while True:

        C_k = safe(2, graph, U_k.difference(final_states), gamma_1, gamma_2)
        U_k_next = safe(1, graph, U_k.difference(C_k), gamma_1, gamma_2)

        # Updating the sub-assignments for each state
        for state_data, state in graph.states.items():
            if state_data not in final_states:
                gamma_1[state_data] = stay(1, state_data, U_k_next, graph, gamma_1, gamma_2)

        if U_k_next == U_k:
            break
        U_k = U_k_next

    return U_k, gamma_1
