# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque

class Solution:
    def getHostName(self, val: str) -> str:
        return val.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = list()

        queue = deque()
        queue.append(startUrl)
        hostname = self.getHostName(startUrl)
        visited = set()
        visited.add(startUrl)
        res.append(startUrl)

        while queue:
            url = queue.popleft()
            for otherUrl in htmlParser.getUrls(url):
                otherHostName = self.getHostName(otherUrl)
                if otherHostName == hostname and otherUrl not in visited:
                    visited.add(otherUrl)
                    res.append(otherUrl)
                    queue.append(otherUrl)
        return res