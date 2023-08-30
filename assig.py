import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost_matrix):
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_indices, col_indices].sum()
    assignment = list(zip(row_indices, col_indices))
    return assignment, total_cost

if __name__ == "__main__":
    n = int(input("Enter the number of agents/tasks: "))
    cost_matrix = []

    print("Enter the cost matrix (one row at a time, space-separated):")
    for _ in range(n):
        row = list(map(int, input().split()))
        cost_matrix.append(row)

    cost_matrix = np.array(cost_matrix)
    assignment, total_cost = solve_assignment(cost_matrix)

    print("Optimal assignment:")
    for agent, task in assignment:
        print(f"Agent {agent+1} assigned to Task {task+1}")
    print("Total cost:", total_cost)



