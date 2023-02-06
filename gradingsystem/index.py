def calculate_grade(score):
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score <= 69:
        return 'B'
    elif score >= 50 and score <= 59:
        return 'C'
    elif score >= 40 and score <= 49:
        return 'D'
    else:
        return 'Fail'

total_score = 0

for i in range(3):
    score = float(input("Enter score for subject {}: ".format(i+1)))
    total_score += score

average_score = total_score / 3
grade = calculate_grade(average_score)

print("Your average score is: {:.2f}".format(average_score))
print("Your grade is: {}".format(grade))
