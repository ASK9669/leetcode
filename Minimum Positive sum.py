class Solution:
    def minimumSumSubarray(self, nums, l, r):
        ans = float('inf')

        for size in range(l, r + 1):
            window_sum = sum(nums[:size])

            if window_sum > 0:
                ans = min(ans, window_sum)

            for i in range(size, len(nums)):
                window_sum -= nums[i - size]
                window_sum += nums[i]

                if window_sum > 0:
                    ans = min(ans, window_sum)

        return -1 if ans == float('inf') else ans
