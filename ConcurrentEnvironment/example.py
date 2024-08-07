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

    final_states = {"2"}
    winning_region_experimental, strategy_experimental = experimental_solver(g, final_states)
    winning_region_traditional, strategy_traditional = traditional_solver(g, final_states)
    print([winning_region_traditional])
    print([s.state_data for s in winning_region_experimental])
