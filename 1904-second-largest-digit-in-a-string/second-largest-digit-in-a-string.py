class Solution:
    def secondHighest(self, s: str) -> int:
        
        
        my_list = []
        
        for ch in s:
            if ch.isdigit():
                my_list.append(int(ch))
    
        new_set = set(my_list)
        if len(new_set) < 2:
            return -1
        sort = sorted(new_set)    
        return sort[-2]

        