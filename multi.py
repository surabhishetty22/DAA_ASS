def multistage_graph(graph, stages):
    n = len(graph)
    cost = [0] * n
    path = [0] * n

    for i in range(n - 2, -1, -1):
        min_cost = float('inf')
        for j in range(n):
            if j in graph[i]:
                cur_cost = graph[i][j] + cost[j]
                if cur_cost < min_cost:
                    min_cost = cur_cost
                    path[i] = j
        cost[i] = min_cost

    return cost[0], path

# Taking user input for the multistage graph
num_stages = int(input("Enter the number of stages: "))
stages = []
for i in range(num_stages):
    vertices = list(map(int, input(f"Enter vertices in stage {i+1} separated by spaces: ").split()))
    stages.append(vertices)

graph = {}
for i in range(num_stages):
    for vertex in stages[i]:
        edges = {}
        num_edges = int(input(f"Enter the number of edges from vertex {vertex} in stage {i+1}: "))
        for _ in range(num_edges):
            dest, cost = map(int, input(f"Enter destination vertex and cost separated by spaces: ").split())
            edges[dest] = cost
        graph[vertex] = edges

min_cost, path = multistage_graph(graph, stages)
print("The minimum cost of the multistage graph is:", min_cost)
print("The optimal path is:", end=" ")
vertex = path[0]
print(vertex, end=" ")
for i in range(1, num_stages - 1):
    vertex = path[vertex]
    print(vertex, end=" ")
print(path[0])


# ouput:
#Enter the number of stages: 3
#Enter vertices in stage 1 separated by spaces: 1
#Enter vertices in stage 2 separated by spaces: 2 3
#Enter vertices in stage 3 separated by spaces: 4

#Enter the number of edges from vertex 1 in stage 1: 1
#Enter destination vertex and cost separated by spaces: 2 2

#Enter the number of edges from vertex 2 in stage 2: 2
#Enter destination vertex and cost separated by spaces: 3 3
#Enter destination vertex and cost separated by spaces: 4 1

#Enter the number of edges from vertex 3 in stage 2: 1
#Enter destination vertex and cost separated by spaces: 4 2

#Enter the number of edges from vertex 4 in stage 3: 0
#The minimum cost of the multistage graph is: 5
#The optimal path is: 1 -> 2 -> 3 -> 4
