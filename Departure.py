# Need to find a way to change the formatting of the imported file to match the below
graph = {'A': {'B': 800}, 'B': {'C': 900, 'F': 400}, 'C': {'D': 400, 'E': 300, 'E': 200},
         'D': {'C': 700, 'E': 400, 'E': 300}, 'E': {'B': 600, 'B': 500}, 'F': {'D': 200}}

# path is set to 0 as well as the nodes to ensure route is started from the start node
def dijkstra(graph, start, goal, passengers):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 99999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        #calculating the lowest weight thus the shortest path

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    #error handling to catch any unacceptable input 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('No outbound flight')
            print('Outbound cost = £0')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        fuel = ((shortest_distance[goal]) * 0.1) * passengers
        print('The outbound route is ' + str(path))
        print('The outbound cost is £' + str(fuel))
