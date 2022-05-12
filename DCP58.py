# Medium

# This problem was asked by Amazon.

# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            print(start, end)
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
            elif nums[end] > target and nums[start] < target:
                mid = (end + start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                mid = (end + start) // 2
                if nums[mid] == target:
                    return mid
                else:
                    newNums = nums[start : mid + 1]
                    result = self.search(newNums, target)
                    if result != -1:
                        return result + start
                    else:
                        start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1
