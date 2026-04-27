from itertools import combinations
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        combined = list(zip(timestamp, username, website))
        combined.sort()

        user_sites = defaultdict(list)
        for _, user, website in combined:
            user_sites[user].append(website)

        pattern_count = defaultdict(int)
        for user, sites in user_sites.items():
            unique_patterns = set(combinations(sites, 3))
            for pattern in unique_patterns:
                pattern_count[pattern] += 1

        return list(sorted(pattern_count.items(), key = lambda item: (-item[1], item[0]))[0][0])