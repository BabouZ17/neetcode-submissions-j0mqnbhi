class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for val in strs:
            current_word = "".join([char for char in sorted(val)])
            result[current_word] = result.get(current_word, []) + [val]
        return list(result.values())
        