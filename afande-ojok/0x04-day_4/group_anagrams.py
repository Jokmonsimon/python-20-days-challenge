from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ["ednafa", "tea", "afande", "eat", "bat", "ate", "arc", "car", "faande"]
print("The Group Anagrams are: {}".format(group_anagrams(words)))