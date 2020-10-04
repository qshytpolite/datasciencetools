def computegrade(score):

    if score <0.0 or score >1.0:
        return 'Bad Score'
    elif score >= 0.9 and score <= 1.0:
        return 'A'
    elif score >= 0.8 and score <= 1.0:
        return 'B'
    elif score >= 0.7 and score <= 1.0:
        return 'C'
    elif score >= 0.6 and score <= 1.0:
        return 'D'
    elif score <0.6 and score >=0.0:
        return 'F'
    
r = float(input('Enter score: '))
grade = computegrade(r)
print(grade)

   
    
