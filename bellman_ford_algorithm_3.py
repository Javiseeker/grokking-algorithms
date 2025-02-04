# TODO: Investigate how bellman ford algorithm works...

class BellmanFordAlgorithm:
    def __init__(self):
        self.graph = {}
    
    def initialize_graph(self):
        # graph
        self.graph = {}
        self.graph["START"] = {}
        self.graph["START"]["A"] = 2
        self.graph["START"]["B"] = 2

        self.graph["A"] = {}
        self.graph["A"]["C"] = 2
        self.graph["A"]["FINISH"] = 2

        self.graph["B"] = {}
        self.graph["B"]["A"] = 2

        self.graph["C"] = {}
        self.graph["C"]["B"] = -1
        self.graph["C"]["FINISH"] = 2

        # TODO: investigate what else I need to initialize
    
    def find_shortest_path(self):
        pass
    
    def get_path(self):
        pass
    
    def calculate_weight_of_shortest_path(self):
        pass

def main():
    bellmanFord = BellmanFordAlgorithm()
    bellmanFord.initialize_graph()
    bellmanFord.find_shortest_path()
    print(f"The fastest path is: {bellmanFord.get_path()}")
    print(f"The total weight of the fastest path is: {bellmanFord.calculate_weight_of_shortest_path()}")

if __name__ == "__main__":
    main()
