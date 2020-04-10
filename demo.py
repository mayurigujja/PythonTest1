a = 3
print(a)
a, b, c = 6, 5.4, "god"
print("{} {} {} {} {}".format("The value of a and c is", a, c, "and value of b is", b))
print(type(b))

values = [1, 2, 3, "mayu", 6.7]
print(values)

values.insert(0, 0)
print(values)

values.append("end")
print(values)

values[3]="Updated"
print(values)

del values[0]
print(values)

print(values[1:3])
