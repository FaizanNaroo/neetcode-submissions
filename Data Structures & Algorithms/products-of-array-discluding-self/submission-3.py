class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*(len(nums))
        output=1
        for i in range(len(nums)):
            output*=nums[i]
            prefix[i]=output

        sufix=[1]*(len(nums))
        output=1
        for i in range(len(nums)):
            index=len(nums)-i-1
            output*=nums[index]
            sufix[index]=output
        res=[1]*(len(nums))
        for i in range(len(nums)):
            if i-1<0:
                res[i]=1*sufix[i+1]
                continue
            elif i+1>=len(nums):
                res[i]=prefix[i-1]*1
                continue
            else:
                res[i]=prefix[i-1]*sufix[i+1]

        return res

            

        