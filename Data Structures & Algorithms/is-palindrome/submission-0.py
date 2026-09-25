class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = str.lower(s.replace(" ", ""))
        i = 0
        j = len(strip_s) - 1

        while i < j:
            if not (strip_s[i].isalpha() or strip_s[i].isnumeric()):
                i += 1
                continue
            elif not (strip_s[j].isalpha() or strip_s[j].isnumeric()):
                j -= 1
                continue
            elif strip_s[i] != strip_s[j]:
                return False

            i += 1
            j -= 1

        return True
