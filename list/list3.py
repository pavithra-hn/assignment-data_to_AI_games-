values = [10,20,30,40,50,]
print(values[0])
print(values[1])

values[1] = 25
print(values)

values.append(60)
values.insert(2,15)
print(values)

values.remove(40)
poped_value = values.pop()
print(values)
print("poped:", poped_value)

for value in values:
    print(value)
print("length:", len(values))