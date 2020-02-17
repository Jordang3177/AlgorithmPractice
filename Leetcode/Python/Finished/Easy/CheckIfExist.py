class Solution:
    def checkIfExist(self, arr):
        if len(arr) <= 1:
            return False
        else:
            for value in arr:
                index = arr.index(value)
                if value*2 in arr[0:index] or value*2 in arr[index+1:len(arr)]:
                    return True
        return False
