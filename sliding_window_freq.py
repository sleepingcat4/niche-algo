from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        l, r = 0, 0
        formed = 0
        
        window_counts = defaultdict(int)
        min_length = float('inf')
        min_left = 0
        
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_left = l
                
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return s[min_left:min_left + min_length] if min_length != float('inf') else ""
