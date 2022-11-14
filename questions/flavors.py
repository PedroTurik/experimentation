from functools import cache, wraps
import time
from random import shuffle
import tracemalloc

# This is a question given my a colleague, that asks for all possible
# ice cream flavor pairs, given that flavors have priorities over others, and high priority
# flavors need to be places first at any given pair

# memory and timing decorators used to optimize the code and compare answers




def measure_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()
        return result
    return wrapper


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.20f} seconds')
        return result
    return timeit_wrapper


ranks = [('a','b'),('a','e'),('b','c'),('c','d'),('d','f'),('e','f'),('f','g'),('h','g'),('i','g'),('g', 'j'),('g','k'),('k','l'),('k','m'),('k','n'),('n','o'),('n', 'p'),('p','o'), ('o','q'),('o','r'),('q','s'),('s','t'),('t','u'),('r','v'),('a1','a'),('b','e'),('v', 'w'),('v','x'),('x','y'),('w','y'),('z','b2'),('z','c2'),('b2','d2'),('d2','e2'),('c2','e2'),('hpai','h')]
shuffle(ranks)


tmp = {x for x, _ in ranks}
tmp2 = {x for _, x in ranks}
flavor_set = tmp.union(tmp2)
adj_list = dict()
for flavor in flavor_set:
    adj_list[flavor] = {y for x, y in ranks if x == flavor}



@timeit
def DFS():
    child_dict = {}

    def findchild(src, set_pass):
        if src in child_dict:
            for x in child_dict[src]:
                set_pass.add(x)
            return
        set_pass.add(src)
        for children in adj_list[src]:
            findchild(children, set_pass)
        return set_pass

    counter = 0
    for flavor in flavor_set:
        ret = findchild(flavor, set())
        child_dict[flavor] = ret
        counter += len(ret) -1
    return counter

print('DFS: ', DFS())
