# Util. functions for reading problem input from stdin.

def c_fair_input():
	kwargs = {}
	kwargs['c'] = float(input())
	input() # We don't need to read in the 'n' parameter.
	kwargs['payoffs'] = list(map(int, input().split()))
	return kwargs
	
def fair_pair_input():
	kwargs = {}
	n = int(input())
	kwargs['task_pairs'] = [[int(v) for v in input().split()] for _ in range(n)]
	return kwargs

def c_fixed_input():
	kwargs = {}
	kwargs['c'] = float(input())
	n = int(input())
	parse_command = lambda s,i: (str(s), int(i))
	kwargs['commands'] = [parse_command(*input().split()) for _ in range(n)]
	return kwargs
