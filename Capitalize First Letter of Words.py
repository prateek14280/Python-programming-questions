s = "i love programming"
new_s = s.split(" ")
for i in range(len(new_s)):
    word = new_s[i]
    new_word = word[0].upper()
    new_word2  = new_word + word[1:]
    new_s[i] = new_word2
final_s = " ".join(new_s)

print(final_s)
