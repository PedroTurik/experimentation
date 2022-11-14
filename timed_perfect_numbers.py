from math import isqrt
from time import time

# Finding perfect numbers algorithm



def timeit(x, timed=False):
    def wrapper(*args, **kwargs):
        start = time()
        result = x(*args, **kwargs)
        finish = time()
        if timed: print(f"Função {x.__name__} foi executada em {finish-start} segundos")
        return result
    return wrapper

def is_prime(N):
    for i in range(3, isqrt(N)+1):
        if N%i == 0:
            return False
    return True


def main():
    i = 2
    number_of_perfects = int(input("number of perfect numbers: "))
    breaker = 0
    inicio = time() 
    while breaker <= number_of_perfects:
        if is_prime(i):
            prime = 2**i - 1
            if is_prime(prime):
                print(f"{prime*(2**(i-1))} is a perfect number")
                finish = time()
                print(f"the funcion took {finish - inicio} to find a new perfect number")
                breaker += 1
                print(f"{i=}")
        i += 1


if __name__=="__main__":
    main()
    
