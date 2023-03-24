from time import perf_counter


B = [1,2,5,2,5,7,34,27,7341,415,87,45,458,9,9,345,114,5,236,-1,-125,-111111,1124,76453,567641,125647,235,252,3,5,235,325,235,32,52,535,23,35,6,57,68,5,8765,45,3,634,6,7,45,234,1256,458,568,3,462,63,4,47,6586,798,7,9]


def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        a = func(*args, **kwargs)
        print(f"\033[34mFunction {func.__name__} took:  \033[0m{(perf_counter() - start)*1000000:.03f} microseconds")
        return a
    return wrapper


@timeit
def selection_sort(a):
    start_index = 0
    while start_index < len(a):
        mini = start_index
        for i in range(start_index,len(a)):
            if a[i] < a[mini]:
                mini = i
        a[start_index], a[mini] = a[mini], a[start_index]
        start_index += 1
    return a


@timeit
def insertion_sort(a):
    for i, n in enumerate(a[1:]):
        j = i       
        while j >= 0 and n < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = n
    return a


@timeit
def bubble_sort(a):
    work = True
    while work:
        work = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                work = True
    return a

def quick_sort(a, start, end):
    if start < end:
        pp = particao(a, start, end)
        quick_sort(a, start, pp)
        quick_sort(a, pp + 1, end)
    return a

def particao(a, start, end):
    pivo = a[end - 1]
    for i in range(start, end):
        if a[i] <= pivo:
            a[i], a[start] = a[start], a[i]
            start += 1
    return start - 1

@timeit
def quick_sort_wrapper(a, start, end):
    return quick_sort(a, start, end)

SUCESS = "\033[32mSucessfully sorted the List\033[0m"
FAIL = "\033[31mFailed to sort the List\033[0m"


if __name__=="__main__":
    print(SUCESS if bubble_sort(B.copy()) == sorted(B) else FAIL)
    print(SUCESS if selection_sort(B.copy()) == sorted(B) else FAIL)
    print(SUCESS if insertion_sort(B.copy()) == sorted(B) else FAIL)
    print(SUCESS if quick_sort_wrapper(B.copy(), 0, len(B)) == sorted(B) else FAIL)
