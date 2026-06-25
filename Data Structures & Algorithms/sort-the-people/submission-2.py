class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_to_names = {}
        for name, height in zip(names, heights):
            h_to_names[height] = name
        
        res = []
        heights.sort(reverse=True)
        for height in heights:
            res.append(h_to_names[height])
        return res