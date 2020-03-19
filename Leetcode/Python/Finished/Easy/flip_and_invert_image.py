class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            popped = A.pop(i)
            A.insert(i, popped[::-1])
        for items in A:
            for i in range(len(items)):
                popped = items.pop(i)
                if popped == 0:
                    items.insert(i, 1)
                else:
                    items.insert(i, 0)
        return A