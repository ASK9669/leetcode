class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # x = digits[-1]
        # digits.pop()
        # if x == 9:
        #     digits.append(1)
        #     digits.append(0)
        # else:
        #     digits.append(x+1)
        num = int("".join(map(str,digits)))
        num += 1
        digit = list(map(int,str(num)))

        return digit
