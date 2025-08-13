# Given two strings s and t, return true if t is an anagram of s, and false otherwise.



# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false



# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## i will be using two solutions
        ## one is a normal hashmap and the other is more memory efficient

        if len(s)!= len(t):
            return False

        counterS , counterT = {}, {}
        for i in range(s):
            counterS[s[i]] = counterS.get(s[i], 0) ## need to add 0 otherwise key value error
            counterT[t[i]] = counterT.get(t[i], 0)

        for c in counterS:
            if counterS[c] != counterT.get(c, 0):
                return False

        return True


        ## another method which is more memory efficient is

        x = set(s)
        y = set(y)

        if x!=y:
            return False

        if x==y:
            for i in x:
                if s.count(i) != t.count(i):
                    return False

        x.clear()
        y.clear()
        return True
