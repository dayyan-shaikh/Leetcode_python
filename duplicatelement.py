# nums=[1,2,3,4]
# hashset=set()
# for i in nums:
#     if i in hashset:
#         print(True)
#     hashset.add(i)
    
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
