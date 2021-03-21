score = float(input('Please input the student score: '))
behavior = True if input('Good behavior? (y/n) ') == 'y' else False

if (score >= 9):
    print('Student name in honor board.')
elif (score >= 7):
    print('Approved')
elif (score >= 4.5):
    print('Student in exam')
elif (score > 3 and behavior):
    print('Student in exam')
    print('Need additional homework')
else:
    print('Reprobate')
print(score)
print('Good behavior' if behavior else 'Bad behavior')
