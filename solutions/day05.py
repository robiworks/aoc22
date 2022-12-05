import re

with open("../data/day05.txt", "r") as f:
    lines = f.readlines()

    s = len(lines[0]) // 4
    stacks = [[] for _ in range(s)]

    for line in lines:
        if line.strip().startswith("["):
            # read stacks from l to r
            for i in range(0, s):
                val = line[i * 4 : i * 4 + 3]
                if val.startswith("["):
                    stacks[i].insert(0, val[1])
        elif line.startswith("move"):
            [amount, stack1, stack2] = [
                int(n) for n in re.findall(r"\d+", line.strip())
            ]

            # for _ in range(amount):
            #     stacks[stack2 - 1].append(stacks[stack1 - 1].pop())

            stacks[stack2 - 1].extend(stacks[stack1 - 1][-amount:])
            del stacks[stack1 - 1][-amount:]

    result = "".join([stack[-1] for stack in stacks])
    print(result)
