def gg():
    import math
    import time
    start_time = time.time()
    flag = False

    for a in range(1, 150):
        tempA = a**5
        if flag:
            break
        for b in range(a+1, 150):
            tempB = b ** 5
            if flag:
                break
            for c in range(b+1, 150):
                tempC = c ** 5
                if flag:
                    break
                for d in range(c+1, 150):
                    tempD = d ** 5
                    temp = math.pow(tempA+tempB+tempC+tempD, 1/5)
                    if temp - int(temp) <= 0.00000001:
                        print(a,b,c,d, int(temp))
                        print(f"Sum = {a+b+c+d+int(temp)}")
                        flag = True
                        if flag:
                            break
    print("time elapsef: {:.2f}s".format(time.time()- start_time))
gg()