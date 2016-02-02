name = input("Enter your first name: ")
pig = "ay"
vowels = ["a", "e", "i", "o", "u"]
word = name.lower()
first = word[0]
new_word = word[1:] + first + pig
s = "s"
new_vowel_name = word[1:] + s + pig
if first in vowels:
    print (new_vowel_name)
elif len(name) > 0 and name.isalpha():
    print (new_word)
else:
    print ("That's not a word")


