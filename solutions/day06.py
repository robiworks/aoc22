with open("../data/day06.txt", "r") as f:
    buffer = f.readline().strip()

    for i in range(len(buffer)):
        marker = buffer[i : i + 4]
        s = {c for c in marker}

        if len(s) == 4:
            print(i + 4)
            break
