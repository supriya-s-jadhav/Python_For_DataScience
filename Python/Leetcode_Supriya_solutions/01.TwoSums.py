"""
AUTHOR: Supriya Jadhav
Version: 2.0

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSum(self, nums, target):
        """_summary_

        Args:
            nums (List[int]): _description_
            target (int): _description_

        Returns:
            List[int]: _description_
        """
        # every previous element (number and it's index) is stored in this map
        prevMap = {}  # val : index
        print(prevMap)
        for i, n in enumerate(nums):
            print(f"nums given : {nums}")
            print(f"Target value: {target}")
            print(i, n, prevMap)
            diff = target - n
            print(diff)
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
# Time Complexity : O(n)
# Space Complexity : O(n)
