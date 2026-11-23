class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums1=set(nums)
        for num in nums:
            if num-1 in nums1:
                continue
            count=1
            cond=True
            while cond:
                if num+count in nums1:
                    count+=1
                else:
                    cond=False
                    res=max(res,count)
            
        return res


                 
             



            

        