class LongestPalindrome:
    def longestPalindrome(self, s):
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        odd = False
        hashmap = {}
        output = 0

        for count in s:
            if count not in hashmap:
                hashmap[count] = 1
            else:
                hashmap[count] += 1

        for count in hashmap:
            if hashmap[count] % 2 == 0:
                output += hashmap[count]
            else:
                output += (hashmap[count] - 1)
                odd = True

        if odd:
            return output + 1
        
        return output
    
lp = LongestPalindrome()
print(lp.longestPalindrome("speediskey"))