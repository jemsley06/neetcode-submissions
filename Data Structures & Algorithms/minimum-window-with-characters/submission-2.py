class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(t)

        left = 0
        best_left, best_right = 0, 0
        found = False

        for right, char in enumerate(s, 1):
            if need.get(char, 0) > 0:
                missing -= 1
            need[char] = need.get(char, 0) - 1

            if missing == 0:

                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not found or (right - left) < (best_right - best_left):
                    best_left, best_right = left, right
                    found = True


                need[s[left]] += 1
                missing += 1
                left += 1

        return s[best_left:best_right] if found else ""