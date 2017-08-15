'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

'''

import collections

class Codec:

    def __init__(self):
        self.dic = collections.defaultdict(set)
        self.num = 0

    def encode(self, longUrl):

        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        self.num += 1
        pos = id(self.num)
        self.dic[pos].add(longUrl)
        return "http://tinyurl.com/" + str(pos)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        for index in self.dic[int(shortUrl.split('/')[-1])] :
        	return index

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":

	url = "https://leetcode.com/problems/design-tinyurl"
	codec = Codec()
	encode = codec.encode(url)
	print (encode)
	print (codec.decode(encode))
	print ("dic", codec.dic)
	assert codec.decode(codec.encode(url)) == url
