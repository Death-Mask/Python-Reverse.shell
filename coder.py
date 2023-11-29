from math import gcd

numpers = []
final = []


def get_info():
    for i in range(4):
        f = i+1
        num = int(input(f'numpers ({f}) is :- '))
        numpers.append(num)
    




def factorization(n):

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors




def process_1():
    for i in numpers:
        final.append(factorization(i))

get_info()
process_1()

print(f"Your numper is {final}")
