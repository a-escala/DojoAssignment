import random

print 'Starting the program...'
def coins(num):
    h_count = 0
    t_count = 0
    attempt = 1
    for x in range(1, num):
        ran = random.randint(0, 1)
        if ran == 0:
            h_count += 1
            result = 'heads'
            print 'Attempt #' , attempt, 'Throwing a coin... It\'s a', result,\
            'got ', h_count, 'head(s) so far and', t_count, 'tail(s) so far'
        else:
            t_count += 1
            result = 'tails'
            print 'Attempt #' , attempt, 'Throwing a coin... It\'s a', result,\
            'got ', h_count, 'head(s) so far and', t_count, 'tail(s) so far'
        attempt += 1

coins(5001)
print 'Program terminating in...\n...3\n ...2\n ...1\n Goodbye!'
