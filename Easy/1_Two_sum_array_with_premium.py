class Solution:
    def twoSum(self, nums, target):
        print("List is " + str(nums))
        print("Target is " + str(target))
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    j = j + 1
                print("Sum is " + str(nums[i] + nums[j]))
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    print("Result is " + str(result))
                    return result
                elif j < len(nums):
                    j = j + 1


a = Solution()
a.twoSum([2, 11, 15, 7], 9)

# This problem was solved by me , works ok on small list but if run on a huge list -
# it time out - its time complexity is O(n2)



