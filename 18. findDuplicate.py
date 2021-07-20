"""
Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums
and uses only constant extra space.
"""

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueLength = len(set(nums))
        duplicateLength = len(nums)
        uniqueSum = sum(set(nums))
        duplicateSum = sum(nums)
        
        if uniqueLength == 1: return nums[0]
        return (duplicateSum - uniqueSum)//(duplicateLength - uniqueLength)

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hair:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
