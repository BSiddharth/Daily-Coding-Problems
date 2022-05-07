# # Easy

# # This problem was asked by Microsoft.

# # Implement a URL shortener with the following methods:

# #       shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# #       restore(short), which expands the shortened string into the original url. If no such shortened  string exists, return null.

# # Hint: What if we enter the same URL twice?

import random


class Codec:
    def __init__(self) -> None:
        self.longToShort = {}
        self.shortToLong = {}
        # 48-57 65-90 97-122
        self.list = []
        for x in range(48, 123):
            if 48 <= x <= 57 or 65 <= x <= 90 or 97 <= x <= 122:
                self.list.append(chr(x))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        shortUrl = ""
        for x in range(6):
            random.seed(longUrl + str(x))
            index = random.randint(0, len(self.list) - 1)
            shortUrl += self.list[index]
        self.longToShort[longUrl] = shortUrl
        self.shortToLong[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.shortToLong[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# print(codec.decode(codec.encode("url")))
