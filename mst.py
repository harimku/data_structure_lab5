from dynamic_array import DynamicArray
from priority_queue import PriorityQueue, Node


class Graph:
    def __init__(self, vertices, str_map):
        self.V = vertices
        self.str_map = str_map
        self.graph = PriorityQueue()

    def add_edge(self, u, v, w):
        new_edge = Node(u=u, v=v, node=w)
        self.graph.push(new_edge)

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def check_cycle(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def mst(self):
        result = DynamicArray()
        i, e = 0, 0
        parent = DynamicArray()
        rank = DynamicArray()
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            node1 = self.search(parent, u)
            node2 = self.search(parent, v)
            if node1 != node2:
                e = e + 1
                result_node = Node(u=u, v=v, node=w)
                result.append(result_node)
                self.check_cycle(parent, rank, node1, node2)
        total_sum = 0
        for node in result:
            num_to_airport = {v: k for k, v in self.str_map.items()}
            u = num_to_airport[node.u]
            v = num_to_airport[node.v]
            print("%s --- %s: %d" % (u, v, node.node))
            total_sum += node.node
        print('Total Cost of MST: ' + str(total_sum))


def main():
    airport = {
        "Seattle": [("Minneapolis", 2661), ("Denver", 2161), ("San Francisco", 1306)],
        "Minneapolis": [("Chicago", 661), ("Dallas", 1532), ("Denver", 1483)],
        "Chicago": [("Boston", 1613), ("DC", 1145)],
        "Boston": [("New York", 338), ("DC", 725)],
        "New York": [("DC", 383), ("Miami", 2145)],
        "DC": [("Miami", 1709), ("Dallas", 2113)],
        "Miami": [("Dallas", 2161)],
        "Dallas": [("Denver", 1258), ("Las Vegas", 1983)],
        "Denver": [("Las Vegas", 1225)],
        "Las Vegas": [("San Francisco", 919), ("LA", 435)],
        "San Francisco": [("LA", 629)]
    }

    airport_to_num = {
        "Seattle": 0,
        "Minneapolis": 1,
        "Chicago": 2,
        "Boston": 3,
        "New York": 4,
        "DC": 5,
        "Miami": 6,
        "Dallas": 7,
        "Denver": 8,
        "Las Vegas": 9,
        "San Francisco": 10,
        "LA": 11
    }

    g = Graph(vertices=12, str_map=airport_to_num)
    for key, val in airport.items():
        for edge in val:
            u = airport_to_num[key]
            v = airport_to_num[edge[0]]
            w = edge[1]
            g.add_edge(u, v, w)

    g.mst()


if __name__ == '__main__':
    main()
