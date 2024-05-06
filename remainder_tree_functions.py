import numpy as np
import math

"""
Adapted from https://facthacks.cr.yp.to/batchgcd.html
"""

def remainder_tree_batch_gcd(X):
       prods = producttree(X)
       R = prods.pop()
       while prods:
         X = prods.pop()
         R = [R[math.floor(i//2)] % X[i]**2 for i in range(len(X))]
       return [math.gcd(int(r//n), n) for r,n in zip(R,X)]

def producttree(X):
       result = [X]
       while len(X) > 1:
         X = [int(np.product(X[i*2:(i+1)*2])) for i in range(int((len(X)+1)//2))]
         result.append(X)
       return result

