from copy import deepcopy

# Playing around with inheritance.

# This is a class that inherits from list, but its always ordered



class OrderedList(list):
    def __init__(self, *args, reversed=False):
        list.__init__(self, *args)
        self.sort(reverse=reversed)
        self.reversed = reversed

    def extend():
        raise NotImplementedError

    def append(self, *args):
        for n in args:
            self.insert(0, n)

    def __iadd__(self, __x):
        return self + __x

    def __add__(self, *args):
        if len(args) > 1: raise Exception("Too Many args")
        new_list = deepcopy(self)
        new_list.append(*args[0])
        return new_list

    def insert(self, __index, n: int) -> None:
        if self.reversed: return self.rinsert(n)
        lo = 0
        hi = self.__len__()
        while lo < hi:
            mid = (lo+hi)//2
            if self.__getitem__(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return super().insert(lo, n)

    def reverse(self) -> None:
        self.reversed = not self.reversed
        self.sort(reverse=self.reversed)

        
    def rinsert(self, n):
        lo = 0
        hi = self.__len__()
        while lo < hi:
            mid = (lo+hi)//2
            if self.__getitem__(mid) > n:
                lo = mid + 1
            else:
                hi = mid
        return super().insert(lo, n)
    

lista = OrderedList([1, 40, 7, 23, 2, 0], reversed=True)
lista.append(5, 123,51,536,64)
lista = lista + [12, 13]
lista.reverse()
lista += [13,124,26,25,-15, -12]
lista.insert(0,-646)
lista.reverse()

print(lista)
