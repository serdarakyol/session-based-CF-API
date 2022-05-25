from numba import njit, prange
from numpy import zeros, float64, int32, sqrt

@njit('float64(int8[::1], int8[::1])')
def cosine_similarity(a,b):
    # Large safe integer type (int16 is less safe but certainly faster)
    dt = int32(0)
    for i in range(a.size):
        dt += a[i] & b[i]
    
    if dt == 0:
        return 0.0

    sa, sb = int32(0), int32(0)
    for i in range(a.size):
        sa += a[i]
        sb += b[i]
    return dt / sqrt(sa * sb)

@njit('float64[:](int8[:,::1], int8[::1])', parallel=True)
def calculate_similarity_parallel(multiple_item, single_item):
    n = multiple_item.shape[0]
    scores = zeros(n, float64)
    for i in prange(n):
        scores[i] = cosine_similarity(single_item, multiple_item[i])
    return scores
