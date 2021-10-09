class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            a = list(map.values())
            current = nums[i]
            x = target - current
            if x in a:
                print([a.index(x), i])
                return [a.index(x), i]
            map[i] = nums[i]


a = Solution()
a.twoSum([2, 11, 15, 7], 9)
