from ConcurrentEnvironment import State
from ConcurrentEnvironment.Graph import Graph
import copy


def traditional_solver(graph: Graph, final_states: set[str]) -> (set[State], dict[State, str]):
    # winning_region = set()
    # strategy = dict()

    winning_region = almost_sure_solver(graph, final_states)

    return winning_region


def stay(player: int, state: 'State', target_set):
    stay_action_set = set()
    # if player == 1:
    #     for a1 in state.sub_assignment_p1:
    #         flag = 0
    #         for a2 in state.sub_assignment_p2:
    #             if not state.out_neighbors[a1][a2].issubset(target_set):
    #                 flag = 1
    #                 break
    #
    #         if flag == 0:
    #             stay_set.add(a1)
    if player == 1:
        for a1 in state.sub_assignment_p1:
            if all(state.out_neighbors[a1][a2].issubset(target_set) for a2 in state.sub_assignment_p2):
                stay_action_set.add(a1)

    # elif player == 2:
    #     for a2 in state.sub_assignment_p1:
    #         flag = 0
    #         for a1 in state.sub_assignment_p2:
    #             if not state.out_neighbors[a1][a2].issubset(target_set):
    #                 flag = 1
    #                 break
    #
    #         if flag == 0:
    #             stay_set.add(a2)

    if player == 2:
        for a2 in state.sub_assignment_p2:
            if all(state.out_neighbors[a1][a2].issubset(target_set) for a1 in state.sub_assignment_p1):
                stay_action_set.add(a2)

    return stay_action_set


def pre(player: int, target_set, graph: Graph):
    pre_set = set()
    if player == 1:
        return {s for s in graph.states if any(
            all(s.out_neighbors[a1][a2].issubset(target_set) for a2 in s.sub_assignment_p2) for a1 in
            s.sub_assignment_p1)}
    elif player == 2:
        return {s for s in graph.states if any(
            all(s.out_neighbors[a1][a2].issubset(target_set) for a2 in s.sub_assignment_p2) for a1 in
            s.sub_assignment_p1)}


def safe(player: int, graph: Graph, target_set):
    prev_target_set = target_set
    while True:
        next_target_set = prev_target_set.intersection(pre(player, prev_target_set, graph))

        if next_target_set == prev_target_set:
            break
        else:
            prev_target_set = next_target_set

    return next_target_set


def almost_sure_solver(graph: Graph, final_states):
    prev_target_set = set(graph.states.keys())

    while True:

        new_C_set = safe(2, graph, prev_target_set.difference(final_states))
        next_target_set = safe(1, graph, prev_target_set.difference(new_C_set))

        # Updating the sub-assignments for each state
        for state in graph.states:
            state.sub_assignment_p1 = stay(1, state, next_target_set)

        if next_target_set == prev_target_set:
            break
        else:
            prev_target_set = next_target_set

    return next_target_set
