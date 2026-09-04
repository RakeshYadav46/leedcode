class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        def prefix_sum(nums):
            for i in range(1,len(nums)):
                nums[i]=nums[i]+nums[i-1]
            return nums

        def sufix_sum(nums):
            for i in range(len(nums)-2,-1,-1):
                nums[i]=nums[i]+nums[i+1]
            return nums

        pre=prefix_sum(nums.copy())
        suf=sufix_sum(nums.copy())

        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left=pre[i-1]

            if i==len(nums)-1:
                right=0
            else:
                right=suf[i+1]

            if left==right:
                return i

        return -1

        