class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset=set(numbers)
        index=0
        result=[]
        for i,num in enumerate(numbers):
            remain=target-num
            if remain in numset:
                index=i
                break
            


        result.append(index+1)
        left=target-numbers[index]

        for i,num in enumerate(numbers):
            if num==left and i!=index:
                result.append(i+1)

        return result


