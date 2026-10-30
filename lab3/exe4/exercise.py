ch = input("Character: ").lower()
if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
else:
    print("Not vowel")