
numbers = []
f = open("1-1_input.txt", "r")
for line in f:
    line = int(line.strip())
    if numbers:  # Empty list == false
        pass
    else:
        pass
    numbers.append(line)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            if numbers[i] + numbers[j] == 2020:
                n1 = numbers[i]
                n2 = numbers[j]
                print("Match found! %s + %s = 2020, %s * %s = %s" %(n1, n2, n1, n2, n1 * n2))
        for k in range(len(numbers)):
            if i != j and k != i and k !=j:
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    n1 = numbers[i]
                    n2 = numbers[j]
                    n3 = numbers[k]
                    print("Match found! %s + %s + %s = 2020, %s * %s * %s = %s" %(n1, n2, n3, n1, n2, n3, n1 * n2 * n3))

