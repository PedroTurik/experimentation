from time import time



def timeit(x):
    def wrapper(*args, **kwargs):
        start = time()
        result = x(*args, **kwargs)
        finish = time()
        print(f"Função {x.__name__} foi executada em {finish-start} segundos")
        return result
    return wrapper


def list_div(N):
    div = []
    i = 1
    while i**2 <= N:
        if N%i == 0:
            div.append(i)
            if i**2 < N:
                div.append(N//i)
        i+=1
    return div

@timeit
def list_div_classico(N):
    div = []
    for i in range(1, N//2 + 1):
        if N%i == 0:
            div.append(i)
    return div



i = 2
while True:
    prime = 2**i - 1
    if len(list_div(prime)) == 2:
        print(prime*(2**(i-1)))
    i += 1
    
