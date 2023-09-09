import math as ma  # importing math for sqrt()


def prime_number(n):
    if n <= 1:
        return False

    for i in range(2, int(ma.sqrt(n)), n):
        if n % i == 0:
            return False

    return True


num = 5
print(prime_number(num))
