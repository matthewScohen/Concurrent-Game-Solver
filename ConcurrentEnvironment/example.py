from ConcurrentEnvironment.Graph import Graph
from Solvers.experimental_solver import experimental_solver
from Solvers.traditional_solver import traditional_solver

if __name__ == "__main__":
    g = Graph()
    g.add_node("1")
    g.add_node("2")
    g.add_node("3")
    # g.add_node("4")
    g.add_edge("1", "2", "a", "A")
    g.add_edge("1", "2", "b", "A")
    g.add_edge("1", "2", "a", "B")
    g.add_edge("1", "2", "b", "B")

    g.add_edge("2", "2", "b", "B")
    g.add_edge("2", "2", "a", "B")
    g.add_edge("2", "2", "b", "A")
    g.add_edge("2", "2", "a", "A")
    #
    g.add_edge("1", "3", "a", "C")
    g.add_edge("1", "2", "b", "C")
    #
    g.add_edge("3", "3", "a", "A")
    g.add_edge("3", "3", "a", "B")
    g.add_edge("3", "3", "a", "C")
    g.add_edge("3", "3", "b", "A")
    g.add_edge("3", "3", "b", "B")
    g.add_edge("3", "3", "b", "C")








    # g.add_edge("1", "3", "a", "D")
    # g.add_edge("4", "2", "b", "A")

    final_states_data = {"2"}
    final_states = set([g.states[s] for s in final_states_data])
    # winning_region1, strategy1 = experimental_solver(g, final_states_data)
    winning_region1_traditional, strategy1_traditional = traditional_solver(g, final_states_data)
    # print([state.state_data for state in winning_region1])
    print([winning_region1_traditional])
    print(strategy1_traditional)
