import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list) # 디폴트값을 list로 줌
    
    for word in strs:
        # 정렬하여 딕셔너리에 추가 eat -> aet, tea -> aet 정렬 후, append
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

print(groupAnagrams(strs))