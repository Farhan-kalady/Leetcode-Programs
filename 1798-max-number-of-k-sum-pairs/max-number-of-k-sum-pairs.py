class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for num in nums:
            complement = k - num
            if hashmap.get(complement, 0) > 0:
                count += 1
                hashmap[complement] -= 1
            else:    
          
                hashmap[num] = hashmap.get(num, 0) + 1
        return count        
        