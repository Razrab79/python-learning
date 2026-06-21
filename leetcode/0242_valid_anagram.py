class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s)!=len(t): return False

        seen = {}
        for x in s:
            seen[x]=seen.get(x, 0)+1
        for y in t:
            if y not in seen or seen[y]==0:
                return False
            seen[y] -= 1
        return True
    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))