# t가 s의 애너그램인지 판별하라
s, t = "anagram", "nagaram"

def isAnagram(s: str, t: str):
    return sorted(s) == sorted(t)
