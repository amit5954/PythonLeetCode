class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            current = nums[i]
            x = target - current
            print(x)
            if x in map.keys():
                return [map[x], i]
            print(map)
            print(i)
            map[current] = i
            i = i+1


a = Solution()
a.twoSum([2, 11, 15, 7], 9)
