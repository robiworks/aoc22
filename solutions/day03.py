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

    # Part 2
    badge_priorities = 0
    for i in range(0, len(lines), 3):
        # Groups of 3 rucksacks
        group = list(map(lambda s: set(s.strip()), lines[i : i + 3]))

        # Common item between groups
        badge = "".join(group[0].intersection(group[1]).intersection(group[2]))
        badge_priorities += priority(badge)

    print(badge_priorities)
