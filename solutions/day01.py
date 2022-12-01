with open("../data/day01.txt", "r") as f:
    lines = f.read()
    elves = lines.split("\n\n")

    maxcals = 0
    for elf in elves:
        cals = elf.split("\n")
        cals = sum([int(cal) for cal in cals if cal])
        maxcals = cals if cals > maxcals else maxcals

    print(maxcals)
