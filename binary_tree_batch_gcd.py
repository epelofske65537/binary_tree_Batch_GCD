import math
import numpy as np
import random
from utilities import integer_single_return_product_tree

def partial_producttree_list(X):
	result = [X]
	while len(X) > 2:
		X = [int(np.product(X[i*2:(i+1)*2])) for i in range(int((len(X)+1)//2))]
		result.append(X)
	return result
def GCD_binary_tree(moduli):
	product_tree = partial_producttree_list(moduli)
	nontrivial_divisors = []
	for tree_level in product_tree:
		for product1, product2 in zip(tree_level[::2], tree_level[1::2]):
			divisor = math.gcd(product1, product2)
			if divisor != 1:
				nontrivial_divisors.append(divisor)
	B = integer_single_return_product_tree(nontrivial_divisors)
	return B
