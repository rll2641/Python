strs = input()

def longestPalindrome(s):
    
    def expand(left, right):
        while  left >= 0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # 만약 길이가 1이거나 회문이면 바로 리턴
    if (len(s) < 2 or s == s[::-1]):
        return s
    
    result = ''
    
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
    
    return result

print(longestPalindrome(strs))