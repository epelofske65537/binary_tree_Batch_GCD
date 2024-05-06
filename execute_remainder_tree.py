import math
import numpy as np
import random
import time
import ast
random.seed(0)

from remainder_tree_functions import remainder_tree_batch_gcd
from utilities import *

#bitlength = 1024
bitlength = 512

for N in range(100000+5000, 1000000+5000, 5000):
	for WEAK in [2, 100, 1000]:
		print(WEAK, N)
		tracking, unique_shared_primes = generate_weak_keys(N, WEAK, bitlength)
		moduli_init = list(tracking.keys())
		random.shuffle(moduli_init)
		moduli = list(moduli_init.copy())
		start = time.process_time()
		factors = remainder_tree_batch_gcd(moduli)
		end = time.process_time()
		factors = remove_1s_version1(factors)
		primes = assert_primes(factors, WEAK)
		check_correct_output(unique_shared_primes, primes)
		print("Process time =", end-start)
		
		file = open("results_remainder_tree/fixed_WEAK"+str(WEAK)+"_"+str(N)+"_"+str(bitlength)+".txt", "w")
		file.write(str(end-start))
		file.close()
