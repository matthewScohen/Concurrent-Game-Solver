from ConcurrentEnvironment.Graph import Graph

if __name__ == "__main__":
    g = Graph()
    g.add_node("1")
    g.add_node("2")
    g.add_edge("1", "2", "a", "b")