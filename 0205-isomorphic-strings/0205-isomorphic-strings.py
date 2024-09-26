class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = {}
        for i,n in enumerate(s):
            if n in ans:
                if ans[n] == t[i]:
                    ans[n] = t[i]
                else:
                    return False

            else:
                if t[i] in ans.values():
                    return False
                else:
                    ans[n] = t[i]
        return True
        