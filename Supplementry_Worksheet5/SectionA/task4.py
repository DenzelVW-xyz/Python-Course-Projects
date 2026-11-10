sentence = input("Input your sentence: ").split()

for index, word in enumerate(sentence):
    if "good" in word:
        sentence[index] = "great"
        
print(" ".join(sentence))