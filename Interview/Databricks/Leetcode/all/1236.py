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
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        q = deque()
        vis = set()
        q.append(startUrl)

        base = ''
        if startUrl.count('/') == 2:
            base = startUrl
        else:
            idx, slash = 0, 3
            while slash > 0:
                c = startUrl[idx]
                if c == '/':
                    slash -= 1
                
                idx += 1
                base += c

        base = base[:-1]

        while q: 
            f = q.popleft()
            vis.add(f)
            connected = htmlParser.getUrls(f)
            for url in connected:
                if url not in vis and url.startswith(base):
                    vis.add(url)
                    q.append(url)
        
        return list(vis)