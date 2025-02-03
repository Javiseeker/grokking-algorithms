# NOTE: you cant use dijkstras algorithm for negative weighted graphs! LOOK at the next sample:

###
# The problem with negative weights is that this core assumption - that once you find a path to a node it must be the shortest - breaks down.
# Here's why: Imagine you find a path to city B that's 10 units long,
# and mark it as permanent. But then later you discover there's a path through city C that includes a negative
# weight of -15. This new path could actually give you a total distance of 5 to reach B.
# But Dijkstra's algorithm already marked B's distance as permanent and won't revisit it!
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

    def get_path(self):
        path = ['fin']
        parent = self.parents['fin']
        while parent is not None:
            path.append(parent)
            parent = self.parents.get(parent)
        return path[::-1]  # Reverse the path to get start->finish order
    
    def initialize_graph(self):
        # These are all mappings using hash tables... so its a hash table (start) of a hash table (graph).
        # In essence, its like creating a hash table for each of the nodes of my graph. Their assignments
        # would be the weights! Also take into account the previous form of graph where I was only interested the nodes and
        # edges like so (breadth_first_search)... graph["you"] = ["alice", "bob", "claire"], now I want weights as well. "Fastest path" problems
        # require these nested hash tables.
        self.graph = {}
        self.graph["start"] = {}
        self.graph["start"]["a"] = 6
        self.graph["start"]["b"] = 2

        self.graph["a"] = {}
        self.graph["a"]["fin"] = 1

        self.graph["b"] = {}
        self.graph["b"]["a"] = 3
        self.graph["b"]["fin"] = 5

        self.graph["fin"] = {}

        # next we need a hash table for the costs that it would take to START to get to FINISH
        # we assign infinity to fin because we dont really know whats the least expensive path.
        self.costs = {}
        self.costs["a"] = 6
        self.costs["b"] = 2
        self.costs["fin"] = float("inf") # this is thw way to assign infinity in python

        # next we need a hash table for the parents, this one is in charge of keeping track of the shortest paths available.
        # for now its just an initialisation because start is connected to both a and b.
        self.parents = {}
        self.parents["a"] = "start"
        self.parents["b"] = "start"
        self.parents["fin"] = None

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

def main():
    dijkstra = DijkstraAlgorithm()
    dijkstra.initialize_graph() # the exercise...
    dijkstra.find_shortest_path()
    # need to understand these 2 prints before doing the exercises!
    print(f"Shortest distance: {dijkstra.costs['fin']}")
    print(f"Shortest path: {' -> '.join(dijkstra.get_path())}")

if __name__ == "__main__":
    main()