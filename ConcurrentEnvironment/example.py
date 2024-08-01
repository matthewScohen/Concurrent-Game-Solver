from ConcurrentEnvironment.Graph import Graph
from Solvers.experimental_solver import experimental_solver

if __name__ == "__main__":
    g = Graph()
    g.add_node("1")
    g.add_node("2")
    g.add_node("3")
    g.add_node("4")
    g.add_edge("1", "2", "a", "B")
    g.add_edge("1", "2", "b", "C")
    g.add_edge("1", "3", "a", "D")

    g.add_edge("4", "2", "b", "A")

    final_states = {"2"}
    winning_region, strategy = experimental_solver(g, final_states)
    print([state.state_data for state in winning_region])