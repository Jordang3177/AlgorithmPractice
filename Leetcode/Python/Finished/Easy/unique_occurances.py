class Solution:
    def uniqueOccurrences(self, arr):
        occurances = {}
        for i in range(len(arr)):
            if arr[i] in occurances:
                occurances[arr[i]] += 1
            else:
                occurances[arr[i]] = 1
        holder = []
        for key, value in occurances.items():
            holder.append(value)
        set_h = set(holder)
        return len(holder) == len(set_h)