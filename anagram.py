word = input("Type the word: ")
anagram = input("Type the anagram: ")

if anagram[::-1] == word:
    print(True)
else:
    print(False)
