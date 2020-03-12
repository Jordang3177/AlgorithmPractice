class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        holder = []
        one = False
        for i in range(len(num)):
            if num[i] == '6' and not one:
                holder.append('9')
                one = True
            else:
                holder.append(num[i])
        answer = ''.join(holder)
        return int(answer)