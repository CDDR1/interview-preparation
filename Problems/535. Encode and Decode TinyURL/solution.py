class Codec:
    
    def __init__(self):
        self.urls, self.tinyToOriginal = {}, {}
        self.counter = 1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tinyUrl = "http://tinyurl.com/" + str(self.counter)
        self.counter += 1
        self.tinyToOriginal[tinyUrl] = longUrl
        self.urls[longUrl] = tinyUrl
        return tinyUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        originalUrl = self.tinyToOriginal[shortUrl]
        self.urls[originalUrl] = originalUrl
        return originalUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Time complexity: O(1)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 9min