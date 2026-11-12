sentence = input("What is your sentence: ").split()
word_to_replace = input("What word do you want to replace: ")
replaced_with = input("What word do you want to replace it with: ")

for word in sentence:
    if word == word_to_replace:
        sentence[sentence.index(word)] = replaced_with
        
sentence = " ".join(sentence)
print(sentence)
