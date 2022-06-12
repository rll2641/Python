from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    anagrams = defaultdict(list) # 디폴트값을 list로 줌
    
    for word in strs:
        # 정렬하여 딕셔너리에 추가 eat -> aet, tea -> aet 정렬 후, append
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

print(groupAnagrams(strs))

# -------정규식--------
import re

anagram = defaultdict(list)
strs = [word for word in re.sub('[^\w]', ' ', input()).lower().split()]

for i in strs:
    anagram[''.join(sorted(i))].append(i)
    
print(list(anagram.values()))