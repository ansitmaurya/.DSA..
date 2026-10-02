1class Solution:
2    def threeSum(self, nums):
3        nums.sort()
4        result = []
5
6        for i in range(len(nums) - 2):
7            if i > 0 and nums[i] == nums[i - 1]:
8                continue
9
10            left = i + 1
11            right = len(nums) - 1
12
13            while left < right:
14                total = nums[i] + nums[left] + nums[right]
15
16                if total == 0:
17                    result.append([nums[i], nums[left], nums[right]])
18
19                    left += 1
20                    right -= 1
21
22                    while left < right and nums[left] == nums[left - 1]:
23                        left += 1
24
25                    while left < right and nums[right] == nums[right + 1]:
26                        right -= 1
27
28                elif total < 0:
29                    left += 1
30                else:
31                    right -= 1
32
33        return result