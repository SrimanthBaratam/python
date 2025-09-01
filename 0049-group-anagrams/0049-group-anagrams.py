from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = defaultdict(list)
        for i in strs:
            alpha_array = [0] * 26
            for j in i:
                alpha_array[ord(j) - ord('a')] += 1
            dictionary[tuple(alpha_array)].append(i)
        return list(dictionary.values())
