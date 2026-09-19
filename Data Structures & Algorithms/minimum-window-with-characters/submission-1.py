class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(t)  # total chars still needed (with multiplicity)

        left = 0
        best_left, best_right = 0, 0
        found = False

        for right, char in enumerate(s, 1):  # right is exclusive end
            if need.get(char, 0) > 0:
                missing -= 1
            need[char] = need.get(char, 0) - 1

            if missing == 0:
                # shrink from the left while it's still valid
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not found or (right - left) < (best_right - best_left):
                    best_left, best_right = left, right
                    found = True

                # kick the leftmost char out to keep searching
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[best_left:best_right] if found else ""