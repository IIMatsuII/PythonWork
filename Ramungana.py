def Ramungana():
    numbers = []
    for a in range(1, 50):
        for b in range(1, 50):
            if a == b:
                continue
            for c in range(1, 50):
                if c == a or c == b:
                    continue
                for d in range(1, 50):
                    if d == c or d == b or d == a:
                        continue
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        i = a ** 3 + b ** 3
                        if i not in numbers:
                            numbers.append(i)
                            print(numbers)

Ramungana()