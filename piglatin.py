
name = input("Enter your first name: ")
pig = "ay"
word = name.lower()
first = word[0]
new_word = word[1:] + first + pig
new_word[1:]
if len(name) > 0 and name.isalpha():
    print new_word
else:
    print "That's not a word"

