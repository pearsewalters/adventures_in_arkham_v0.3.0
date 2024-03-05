# odds and ends that help 

import random 

def rand_from_distro( distro: dict ) -> str:
    """Returns a random key using the values to determine likelihood"""
    total = sum( distro.values() )
    v, r = 0, random.uniform(0,1)
    for k in distro:
        v += distro[k]/total
        if v >= r:
            return k