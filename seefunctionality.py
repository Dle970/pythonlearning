# r = list((range(10)))
# print(r)
# r_sliced = r[8:]
# print(r_sliced)

word = "too"
print(len(word))
correct_letters = "o"
blanks = '_' * len(word)

for i in range(len(word)): # 0 1 2
    if word[i] in correct_letters:
        blanks = blanks[:i] + word[i] + blanks[i + 1:]

print(blanks)