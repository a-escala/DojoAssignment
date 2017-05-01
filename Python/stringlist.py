old = "If monkeys like bananas, then I must be a monkey!"
print old.count("monkey")
print old.replace("monkey", "alligator")

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]
print x[0::7]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:2]
x = x[2:]
x.insert(0,y)
print x
