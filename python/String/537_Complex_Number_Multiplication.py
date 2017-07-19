'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication.
Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi,
where the integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.

Difficulty:Medium

'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        split_a = a.split('+')
        split_b = b.split('+')
        re_a = int(split_a[0])
        re_b = int(split_b[0])
        tmp_im = 0, 0, []
        im_a , im_b = 0, 0

        tmp_im = split_a[1].split('i')
        im_a = int(tmp_im[0])
        tmp_im = split_b[1].split('i')
        im_b = int(tmp_im[0])

        re_result = re_a * re_b - im_a * im_b
        im_result = re_a * im_b + re_b * im_a

        return str(re_result) + '+' + str(im_result) + 'i'
 
if __name__ == "__main__":
	a = '1+1i'
	b = '1+1i'
	
	result = Solution().complexNumberMultiply(a, b)
	print (result)