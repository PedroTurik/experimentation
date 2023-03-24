from math import isqrt

# Finding primes algorithm, using the sieve of erasthotones method


def primes_less_than(n: int):
    if n<= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return (i for i in range(n) if is_prime[i])

def main():
    for n in primes_less_than(int(input("max_number: "))):
        print(f"{n}, ", end="")
    print()


if __name__=="__main__":
    main()
