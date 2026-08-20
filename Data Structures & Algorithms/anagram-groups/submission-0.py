class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dictionary where the key is an array (unique array where )
        res = defaultdict(list)
        for word in strs:
            array = [0] * 26
            for char in word:
                array[ord(char) - ord('a')] += 1
            
            # change the array to tuple since keys needs to be immutable
            res[tuple(array)].append(word)

        return list(res.values())

            

