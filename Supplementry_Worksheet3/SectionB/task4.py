scores = []
amount_of_scores = int(input("How many scores: "))
total = 0

for i in range(amount_of_scores):
    score = int(input(f"Input the #{i + 1} score: "))
    scores.append(score)
    
for score in scores:
    total += score
    
print(f"Final total: {total / amount_of_scores}")