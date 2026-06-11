class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        res = 0

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                rows[r].append(picture[r][c])
                cols[c].append(picture[r][c])

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if (
                    picture[r][c] == "B" and
                    sum([1 if cell == "B" else 0 for cell in rows[r]]) == 1 and
                    sum([1 if cell == "B" else 0 for cell in cols[c]]) == 1
                ):
                    res += 1 

        return res