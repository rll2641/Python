# --------------------reverse--------------------
s = list(input("입력: "))
s.reverse()
print(s)

# --------------------while-----------------------
left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print(s)