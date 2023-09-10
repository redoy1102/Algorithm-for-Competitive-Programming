import math as ma       # imported math for the sqrt()

def prime_number(n):
    if n <= 1:
        return n
    for i in range(2, int(ma.sqrt(n)), n):
        if n % i == 0:
            return False

    return True


