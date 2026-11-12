word = input("Input your word: ")
reversed_word = word[::-1]

if word.lower() == reversed_word.lower():
    print("Word is a palindrome!")
else:
    print("Word is not a palindrome.")
    
