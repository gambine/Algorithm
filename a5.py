from knapsack import knapsack
from utils import c_fair_input, fair_pair_input, c_fixed_input

def c_fair(c, payoffs):
	
	
	return knapsack(payoffs, payoffs, float((1/2)*c*sum(payoffs)), float((1/2)*c*sum(payoffs)))

def fair_pair(task_pairs):
	a = [i[0] for i in task_pairs]
	b = [i[1] for i in task_pairs]
	payoffs = []
	for i in range(len(task_pairs)):
		payoffs.append(a[i]-b[i])
		
	
	return c_fair(1,payoffs)

def c_fixed(c, commands):
	dirction = [i[0] for i in commands]
	distance = [i[1] for i in commands]
	
	s = sum(distance)
	b = s*c 
	
	return 0

if __name__ == "__main__":
	problem = input()
	
	input_fn, solver =	(c_fair_input, c_fair) if problem == "c-fair" else \
						(fair_pair_input, fair_pair) if problem == "fair-pair" else \
						(c_fixed_input, c_fixed)

	problem_input = input_fn()
	print(int(solver(**problem_input)))
