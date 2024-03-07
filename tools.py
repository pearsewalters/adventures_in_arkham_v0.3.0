# odds and ends that help 

import random 
from icecream import ic

def rand_from_distro( distro: dict ) -> str:
    """Returns a random key using the values to determine likelihood"""
    total = sum( distro.values() )
    v, r = 0, random.uniform(0,1)
    for k in distro:
        v += distro[k]/total
        if v >= r:
            return k
        
def dot_product( a, b ):
    """The dot product of two vectors"""
    return sum( [ a_n * b_n for a_n, b_n in zip( a, b) ] )

def matrix_multiply( A, B ):
    result = [ [] for row in A ]
    for i, r in enumerate( A ):
        for j, element in enumerate( r ):
            result[i].append( dot_product( r, [ s[j] for s in B ] ) )
    return result

def matrix_square( A ):
    return matrix_multiply( A, A )
