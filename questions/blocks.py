# Interview problem from 
# https://www.youtube.com/watch?v=rw4s4M3hFfs&t=523s&ab_channel=Cl%C3%A9mentMihailescu

# Returns the best suitable Block to live. The best Block is the one that
# minimizes the farthest distance needed to walk to reach every building you need.

# Its implicit that every building has a block.




Blocks = [{
"gym": False,
"school": True,
"store": False
},
{
"gym": True,
"school": False,
"store": False
},
{
"gym": True,
"school": True,
"store": False
},
{
"gym": False,
"school": True,
"store": False
},
{
"gym": False,
"school": True,
"store": True
}]

Reqs = ("gym", "school", "store")

def f_back(idx, req):
    counter = 0
    while idx > 0:
        counter += 1
        idx -= 1
        if Blocks[idx][req]:
            return counter
    return 100000

def f_front(idx, req):
    counter = 0
    while idx < len(Blocks)-1:
        counter += 1
        idx += 1
        if Blocks[idx][req]:
            return counter
    return 100000


def f(var, idx, req):
    if Blocks[idx][req]:
        return var
    else:
        return min(f_back(idx, req), f_front(idx, req))


def find_best_apartment(Blocks, Reqs):


    f_dist = (0, +100000000)

    for idx, appartment in enumerate(Blocks):
        far_dist = 0
        for req in Reqs:
            n = f(0, idx, req)
            if n > far_dist: far_dist = n

        if far_dist < f_dist[1]:
            f_dist = (idx, far_dist)
    
    return f_dist[0]


if __name__=="__main__":
    print(find_best_apartment(Blocks, Reqs))

    