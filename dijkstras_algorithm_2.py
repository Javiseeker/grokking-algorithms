class DijkstraAlgorithm:
    def __init__(self):
        self.graph = {}
        self.costs = {}
        self.parents = {}
        self.processed = []

    def find_lowest_cost_node(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    
    def find_shortest_path(self):
        # Dijkstras algorithm...
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()
    
    def calculate_weight_of_shortest_path(self):
        current = "FINISH"
        parent = self.parents["FINISH"]
        total_weight = 0
        
        while parent is not None:
        # Add weight between current node and its parent
            total_weight += self.graph[parent][current]
            current = parent
            parent = self.parents.get(parent)
            
        return total_weight
        
    def get_path(self):
        path = ["FINISH"]
        parent = self.parents["FINISH"]
        while parent is not None:
            path.append(parent)
            parent = self.parents.get(parent)
        return path[::-1] 
    
    def initialize_graph(self):
        # graph
        self.graph = {}
        self.graph["START"] = {}
        self.graph["START"]["A"] = 10

        self.graph["A"] = {}
        self.graph["A"]["B"] = 20
        
        self.graph["B"] = {}
        self.graph["B"]["C"] = 1
        self.graph["B"]["FINISH"] = 30

        self.graph["C"] = {}
        self.graph["C"]["A"] = 1

        self.graph["FINISH"] = {}

        # costs
        inf = float("inf")
        self.costs = {}
        self.costs["A"] = 10
        self.costs["B"] = inf
        self.costs["C"] = inf
        self.costs["FINISH"] = inf

        # parents
        self.parents = {}
        self.parents["A"] = "START"
        self.parents["B"] = None
        self.parents["C"] = None
        self.parents["FINISH"] = None
    
def main():
    dijkstra = DijkstraAlgorithm()
    dijkstra.initialize_graph()
    dijkstra.find_shortest_path()
    print(f"The fastest path is: {dijkstra.get_path()}")
    print(f"The total weight of the fastest path is: {dijkstra.calculate_weight_of_shortest_path()}")

if __name__ == "__main__":
    main()
