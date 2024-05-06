import random
import ast
import numpy as np
import math

from Crypto.Util import number


def remove_1s_version1(input):
	out = list(filter((1).__ne__, input))
	out = list(set(out))
	return out
def assert_primes(integers, number_unique_shared_primes):
	BLs = []
	for a in integers:
		BLs.append(a.bit_length())
	primes = []
	for N in integers:
		if number.isPrime(N) == 1:#Means True
			primes.append(N)
	assert len(list(set(primes))) == number_unique_shared_primes
	return primes
def check_correct_output(initial_primes, primes):
	primes = list(set(primes))
	assert len(initial_primes) == len(list(set(initial_primes)))
	assert len(initial_primes) == len(primes)
	initial_primes.sort()
	primes.sort()
	assert initial_primes == primes

def generate_weak_keys(TOTAL_MODULI, WEAK_MODULI, bitlength):
	random.seed(10)
	tracking = {}
	factors = []
	numb_primes_to_get = 2*TOTAL_MODULI - (2*WEAK_MODULI)
	for numb in range(0, numb_primes_to_get, 2):
		file = open("primes/"+str(numb)+"_"+str(bitlength)+".txt", "r")
		p = ast.literal_eval(file.read())
		file.close()
		file = open("primes/"+str(numb+1)+"_"+str(bitlength)+".txt", "r")
		q = ast.literal_eval(file.read())
		file.close()
		N = p*q
		tracking[N] = [p, q]
		factors.append(p)
		factors.append(q)
	numb += 2
	unique_shared_primes = []
	factors_for_weak_moduli = factors.copy()
	for weak in range(WEAK_MODULI):
		numb += 1
		p = random.choice(factors_for_weak_moduli)
		unique_shared_primes.append(p)
		factors_for_weak_moduli.remove(p)
		
		file = open("primes/"+str(numb)+"_"+str(bitlength)+".txt", "r")
		q = ast.literal_eval(file.read())
		file.close()
		N = p*q
		tracking[N] = [p, q]
	assert len(unique_shared_primes) == len(list(set(unique_shared_primes)))
	return tracking, unique_shared_primes
def integer_single_return_product_tree(X):
       if len(X) == 0: return 1
       while len(X) > 1:
         X = [int(np.product(X[i*2:(i+1)*2])) for i in range(int((len(X)+1)//2))]
       return X[0]


def single_run_GCD(moduli, product_of_divisors):
	factors_found = []
	for mod in moduli:
		resulting_gcd = math.gcd(mod, product_of_divisors)
		if resulting_gcd != 1:
			factors_found.append(resulting_gcd)
	return factors_found

