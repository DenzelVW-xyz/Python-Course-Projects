points = 0
question_index = 0
questions = ("USA", "Germany", "Australia", "Malta", "Italy", "Spain")
answers = ("washington", "berlin", "canberra", "valletta", "rome", "madrid")

print("Welcome to the Capital Quiz")

for country in questions:
    
    print("What is the capital of", country + "?")
    user_answer = input("Input your answer: ").lower().strip()
    
    if user_answer == answers[question_index]:
        points += 2
        question_index += 1
    else:
        question_index += 1

print(f"You scored {points}/12")


