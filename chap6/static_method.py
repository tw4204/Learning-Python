class String:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # we allow only letters and numbers
        # generator
        s = ''.join(c for c in s if c.isalnum()) # Study this!
        # For case insensitive comparison, we lower-case s
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True


print(String.is_palindrome('Radar', case_insensitive=False)) # False: Case Sensitive
print(String.is_palindrome('A nut for a jar of tuna')) # True
print(String.is_palindrome('Never Odd, Or Even!')) # True
