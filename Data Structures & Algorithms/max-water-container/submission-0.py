class Solution:
    def maxArea(self, heights: List[int]) -> int:
        containers=[]
        l=0
        r=len(heights)-1
        for _ in range(len(heights)):
            width=r-l
            height=min(heights[r],heights[l])
            area=width*height
            containers.append(area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max(containers)






