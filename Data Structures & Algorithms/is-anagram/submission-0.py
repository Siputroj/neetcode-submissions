class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t