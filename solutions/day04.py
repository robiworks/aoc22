def full_overlap(section1: "tuple[int, int]", section2: "tuple[int, int]") -> bool:
    (s1, e1) = section1
    (s2, e2) = section2

    return (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2)


with open("../data/day04.txt", "r") as f:
    lines = f.readlines()

    full_overlaps = 0
    for line in lines:
        [sec1, sec2] = line.split(",")
        [s1, e1] = sec1.split("-")
        [s2, e2] = sec2.split("-")

        t1 = (int(s1), int(e1))
        t2 = (int(s2), int(e2))

        full_overlaps += 1 if full_overlap(t1, t2) else 0

    print(full_overlaps)
