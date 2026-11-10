sentence = input("Input your sentence: ").split()
capatalized_words = [word.capitalize() for word in sentence]
final_sentence = " ".join(capatalized_words)

print(final_sentence)