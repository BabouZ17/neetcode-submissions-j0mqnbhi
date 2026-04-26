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

class Solution:
    def getHostName(self, url: str) -> str:
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        hostname = self.getHostName(startUrl)

        def dfs(url: str):
            visited.add(url)
            for new_url in htmlParser.getUrls(url):
                if self.getHostName(new_url) == hostname and new_url not in visited:
                    dfs(new_url)

        dfs(startUrl)
        return list(visited)
