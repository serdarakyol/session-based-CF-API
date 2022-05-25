#from numba import jit, prange
from numpy.linalg import norm
from numpy import zeros, dot, float64

#@jit(nopython=True)
def cosine_similarity(a,b):
    dt = dot(a,b)
    if(abs(dt)<=1e-10):
        return 0
    else:
        return dt/norm(a)/norm(b)
    
#@jit(nopython=True, parallel=True)
def calculate_similarity_parallel(multiple_item, single_item):
    n = multiple_item.shape[0]
    scores = zeros(shape=(n), dtype=float64)
    for i in range(n):
        scores[i] = cosine_similarity(a=single_item, b=multiple_item[i])
    return scores

"""@jit(nopython=True)
def add_item2list(items):
    n = items."""
