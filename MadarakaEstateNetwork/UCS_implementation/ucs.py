import graphCreation as gc
import heapq
import networkx as nx



def uniformCostSearch(graph, origin, goal):
    frontier = []
    frontierIndex = {}
    node = (0, origin, [origin])
    frontierIndex[node[1]] = [node[0], node[2]]
    heapq.heappush(frontier, node)
    explored = set()
    while frontier:
        if len(frontier) == 0:
            return None
        node = heapq.heappop(frontier)
        del frontierIndex[node[1]]
        if node[1] == goal:
            return node
        explored.add(node[1])
        neighbours = list(graph.neighbors(node[1]))
        path = node[2]
        for child in neighbours:
            path.append(child)
            childNode = (node[0] + graph.get_edge_data(node[1], child)["weight"], child, path)
            print("frontier = {}".format(childNode))
            if child not in explored and child not in frontierIndex:
                heapq.heappush(frontier, childNode)
                frontierIndex[child] = [childNode[0], childNode[2]]
            elif child in frontierIndex:
                if childNode[0] < frontierIndex[child][0]:
                    nodeToRemove = (frontierIndex[child][0], child, frontierIndex[child][1])
                    frontier.remove(nodeToRemove)
                    heapq.heapify(frontier)
                    del frontierIndex[child]

                    heapq.heappush(frontier, childNode)
                    frontierIndex[child] = [childNode[0], childNode[2]]
            path = path[:-1]

        print("Explored {}".format(explored))
nodes = gc.load_graph_from_file("nodes.json")
solution = uniformCostSearch(nodes, "SportsComplex", "ParkingLot")
print("SOLUTION: {}".format(solution))
gc.show_weighted_graph(nodes, 1000, 13, (10, 5))

