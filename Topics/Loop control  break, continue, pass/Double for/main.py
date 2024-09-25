for i in range(10):
    line = ""
    for j in range(10):
        if i == j:
            break
        line += "{} ".format(j)
    print(line)