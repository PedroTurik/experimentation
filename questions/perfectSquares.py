from math import isqrt
class Node():
    def __init__(self, val, parent=None):
        self.parent = parent
        self.val = val

class Solution:
    def numSquares(self, n: int) -> int:
        def BFS():
            queue = [Node(n, None)]
            while queue:
                cur_node = queue.pop(0)
                val = cur_node.val
                for i in range(isqrt(val), 0, -1):
                    if val - i*i < 0: continue
                    if val -i*i == 0: return Node(val - i*i, cur_node)
                    queue.append(Node(val - i*i, cur_node))
        win_node = BFS()
        counter = 0
        while win_node.parent:
            counter += 1
            win_node = win_node.parent
        
        return counter
b = Solution()
print(b.numSquares(13))

        



