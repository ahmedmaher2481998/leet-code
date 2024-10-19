class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        arr = []
        par = set(["{", "}", "(", ")", "[", "]"])
        for i, l in enumerate(s):
            last = arr[len(arr) - 1] if len(arr) > 0 else None
            if l == "}" and last == "{":
                arr.pop()
            elif l == "]" and last == "[":
                arr.pop()
            elif l == ")" and last == "(":
                arr.pop()
            elif l in par:

                arr.append(l)
        return len(arr) == 0
