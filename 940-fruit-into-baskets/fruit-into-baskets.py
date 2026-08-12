class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        maxi = 0
        n = len(fruits)
        my_dict = {}
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1) 
            right += 1
        return maxi       
