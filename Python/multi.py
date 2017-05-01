#part 1 print all odd numbers from 1 to 1000
for count in range(1, 1000, 2):
    print count

#print multiples of 5 from 5 to 1,000,000
for count in range(5, 1000000, 5):
    print count

#print the sum of all values in a list
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

#print the average of a list
a = [1, 2, 5, 10, 255, 3]
b = sum(a) / len(a)
print b
