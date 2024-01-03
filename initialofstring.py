# Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym.
words = ["alice","bob","charlie"]
s = "abc"
# words = ["an","apple"]
# s = "a"
w=''
for i in  words:
    w+=i[0]
print(w)
if w==s:
    print(True)
else:
    print(False)