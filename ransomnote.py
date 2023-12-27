from collections import Counter
ransomNote = "aa"
magazine = "aab"
st1=Counter(ransomNote)
st2=Counter(magazine)
print(st1)
print(st2)
if st1 & st2 == st1:
    print(True)
else:
    print(False)