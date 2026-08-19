class Solution:
    def majorityElement(self, nums):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        n = len(nums)
        for num, count in frequency.items():
            if count > n / 2:
                return num