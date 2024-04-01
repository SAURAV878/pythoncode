#while loop - repeat the code if certain conditoion is meet ot true
y = 0
while y <=10:
    print(y)
    y += 1

    if y == 5:
        break
    print(y)

    if y == 5:
        continue
    print(y)

    if y == 5:
        pass
    print(y)


