total_score = 0
count = 0
print('Enter grade: ')
grade = input()
while grade != '':
    if grade == 'A+' or grade == 'A':
        total_score += 4.0
    if grade == 'A-':
        total_score += 3.7
    if grade == 'B+':
        total_score += 3.3
    if grade == 'B':
        total_score += 3.0
    if grade == 'B-':
        total_score += 2.7
    if grade == 'C+':
        total_score += 2.3
    if grade == 'C':
        total_score += 2.0
    if grade == 'C-':
        total_score += 1.7
    if grade == 'D+':
        total_score += 1.3
    if grade == 'D':
        total_score += 1
    if grade == 'F':
        total_score += 0
    count += 1
    grade = input()
average_score = total_score / count
print('Average score =', average_score)
