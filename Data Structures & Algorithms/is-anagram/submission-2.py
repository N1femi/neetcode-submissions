class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for char in s:
            if s_hash.get(char) == None:
                s_hash[char] = 0
            
            s_hash[char] += 1
        
        for char in t:
            if t_hash.get(char) == None:
                t_hash[char] = 0
            
            t_hash[char] += 1
        
        for index in s_hash:
            if t_hash.get(index) == None:
                return False
            
            if t_hash[index] != s_hash[index]:
                return False


        for index in t_hash:
            if s_hash.get(index) == None:
                return False
            
            if s_hash[index] != t_hash[index]:
                return False

        
        return True
        