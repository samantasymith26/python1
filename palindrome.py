word = input("Enter a word: ")
reverse_word = word[::-1]
if word == reverse_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
