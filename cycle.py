def is_valid(v, pos, path, graph):
    if not graph[path[pos - 1]][v]:
        return False

    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]]:
            return True
        return False

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian cycle exists.")
        return

    print("Hamiltonian cycle exists:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    graph = []

    for _ in range(n):
        row = list(map(int, input(f"Enter adjacency matrix row for vertex {_+1} (0s and 1s separated by spaces): ").split()))
        graph.append(row)

    hamiltonian_cycle(graph)

