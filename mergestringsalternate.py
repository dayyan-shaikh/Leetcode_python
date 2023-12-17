word1 = "abc"
word2 = "pqr"
ans = []
i = 0
while i < len(word1) or i < len(word2):
    if i < len(word1):
        ans.append(word1[i])
    if i < len(word2):
        ans.append(word2[i])
    i += 1
ans = "".join(ans)
print(ans)