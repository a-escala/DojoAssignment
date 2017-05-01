import random



def scores(num):
    for x in range(0, num):
        score = random.randint(60, 100)
        if score <= 100 and score >= 90:
            print 'Score:', score,'; Your grade is A'
        elif score <= 89 and score >= 80:
            print 'Score:', score,'; Your grade is B'
        elif score <= 79 and score >= 70:
            print 'Score:', score,'; Your grade is C'
        elif score <= 69 and score >= 60:
            print 'Score:', score,'; Your grade is D'
        else:
            print 'you failed'
scores(10)
print 'End of Program. Bye!'
