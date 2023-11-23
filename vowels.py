text = input("Type a text: ")
vowels = "aeiou"
numberOfVowels = 0


for letter in text:
    for vowel in vowels:
        if letter == vowel:
            numberOfVowels += 1

print(numberOfVowels)