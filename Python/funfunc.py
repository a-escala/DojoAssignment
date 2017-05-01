#printing odds and evens
def odd_even():
    for x in range(1, 2001):
        if x % 2 == 0:
            print ("Number is {}. This number is even").format(x)
        else:
            print ("Number is {} This number is odd").format(x)

odd_even()

#multiply each value by 5
a = [2, 4, 10, 16]
b = []
def multiply(a):
    for num in a:
        b.append(num * 5)
    return b

print multiply(a)
