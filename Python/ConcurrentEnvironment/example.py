from Python.Solvers.experimental_solver import experimental_solver
from Python.Solvers.traditional_solver import traditional_solver
from GraphGeneration import generate_random_graph_complete

if __name__ == "__main__":
    g, final_states = generate_random_graph_complete(5, 2, {'a', 'b'}, {'A', 'B'})

    winning_region_traditional, strategy_traditional = traditional_solver(g, final_states)
    winning_region_experimental, strategy_experimental = experimental_solver(g, final_states)

    g.print()
    print(set([s for s in winning_region_traditional]) == set([s.state_data for s in winning_region_experimental]))
    print([s for s in winning_region_traditional])
    print([s.state_data for s in winning_region_experimental])
