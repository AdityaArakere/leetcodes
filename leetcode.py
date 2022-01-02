class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        #temp1=[]
        l=len(nums)
        for i in range(0,l):
            for j in range(1,l):
                if nums[i] + nums[j] ==target:
                    if i!=j:
                        return(i,j)
                        #temp1=[i,j]
        #return temp1

print("program1 leetcode")
