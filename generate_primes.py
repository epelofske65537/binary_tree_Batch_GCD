from Crypto.Util import number

"""
Primes are written to text files, not compressed
"""

BL = 512
#BL = 1024

tracking = []

for prime in range(1000000):
	print(prime)
	p = number.getPrime(BL)
	assert p not in tracking
	file = open("primes/"+str(prime)+"_"+str(BL)+".txt", "w")
	file.write(str(p))
	file.close()
	tracking.append(p)
	assert len(list(set(tracking))) == len(tracking)
	#Make sure there are not duplicate primes, that would be ironic
