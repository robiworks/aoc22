with open("../data/day01.txt", "r") as f:
    lines = f.read()
    elves = lines.split("\n\n")

    cals = []
    for elf in elves:
        c = elf.split("\n")
        c = sum([int(cal) for cal in c if cal])
        cals.append(c)

    cals = sorted(cals, reverse=True)
    print(cals[0])
    print(sum(cals[0:3]))
