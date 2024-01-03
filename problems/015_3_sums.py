# Attempt 1: Brute-force method 0(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        three_sums = []
        for idx in range(n):
            for jdx in range(idx+1, n):
                for kdx in range(jdx+1, n):
                    if (nums[idx]+nums[jdx]+nums[kdx] == 0):
                        temp = sorted((nums[idx], nums[jdx], nums[kdx]))
                        if temp not in three_sums:
                            three_sums.append(temp)
        
        return three_sums


# Attempt 2: Breaking into sub problems O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        three_sums = []
        
        def twoSums(nums, target):
            hashmap = {}
            two_sums = []
            for idx in range(len(nums)):
                rem_val = (target-nums[idx])
                if nums[idx] in hashmap:
                    two_sums.append((nums[idx], hashmap[nums[idx]]))
                else:
                    hashmap[rem_val] = nums[idx]
            return two_sums

        for idx in range(n):
            two_sums = twoSums(nums[idx+1:], -nums[idx])
            for two_sum in two_sums:
                three_nums = [nums[idx], two_sum[0], two_sum[1]]
                three_nums = sorted(three_nums)
                if three_nums not in three_sums:
                    three_sums.append(three_nums)
        
        return three_sums

