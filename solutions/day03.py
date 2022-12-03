def priority(char: str) -> int:
    o = ord(char)
    return o - 38 if 65 <= o <= 90 else o - 96


with open("../data/day03.txt", "r") as f:
    lines = f.readlines()

    priorities = 0
    for line in lines:
        # Splitting index
        ix = len(line) // 2
        line = line.strip()

        # Compartments
        comp1 = set(line[0:ix])
        comp2 = set(line[ix:])

        # Common item
        common = "".join(comp1.intersection(comp2))
        priorities += priority(common)

    print(priorities)
