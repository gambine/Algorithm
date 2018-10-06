"""
This file contains a solver for the decision variant of the Knapsack problem.
It can be used in one of two ways:
	1)  From your Python code, add the line `from knapsack import knapsack`.
		Then, simply call the function `knapsack` from your code with an
		iterable of values, an iterable of weights, total capacity and the
		target.
		
	2)  Piping your input to the knapsack algorithm through the command line.
		This can be done from any language of your choice. See the Ed workspace
		for format. 
"""

def knapsack(values, weights, capacity, target):
    if capacity != int(capacity):
        return False
    capacity = int(capacity) + 1
    values = values + [0]
    weights = weights + [0]
    number_of_items = len(values)
    table = []

    for i in range(number_of_items):
        table.append([None] * capacity)

    for j in range(capacity):
        table[0][j] = 0

    for i in range(1, number_of_items):
        for j in range(capacity):
            if weights[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-weights[i-1]] + values[i-1])

    return table[-1][-1] >= target

if __name__ == "__main__":
	n = int(input())
	values = map(int, input().split())
	weights = map(int, input().split())
	W = int(input())
	V = int(input())
	print(int(knapsack(values, weights, W, V)))
