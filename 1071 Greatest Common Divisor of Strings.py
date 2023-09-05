class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd_of_lengths(str1, str2):
            len1 = len(str1)
            len2 = len(str2)
            
            # Calculate the GCD of the lengths using the Euclidean algorithm
            while len2:
                len1, len2 = len2, len1 % len2
            
            return len1

        gcd_len = gcd_of_lengths(str1, str2)
        
        # Check if a substring of length gcd_len divides both strings
        x = str1[:gcd_len]
        if x * (len(str1) // gcd_len) == str1 and x * (len(str2) // gcd_len) == str2:
            return x
        else:
            return ""

# Example usage
# solution = Solution()
# str1 = "ABABAB"
# str2 = "ABAB"
# result = solution.gcdOfStrings(str1, str2)
# print(result)  # Output: "AB"
