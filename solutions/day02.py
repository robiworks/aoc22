# Part 1
def score(opponent: str, me: str) -> int:
    # Rock 1, paper 2, scissors 3
    shape = {"X": 1, "Y": 2, "Z": 3}

    # Combinations for win/draw
    win = [("A", "Y"), ("B", "Z"), ("C", "X")]
    draw = [("A", "X"), ("B", "Y"), ("C", "Z")]

    if (opponent, me) in win:
        return shape[me] + 6
    elif (opponent, me) in draw:
        return shape[me] + 3
    else:
        return shape[me]


# Part 2
def move(opponent: str, result: str) -> str:
    # X = lose, Y = draw, Z = win
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    lose = {"A": "Z", "B": "X", "C": "Y"}

    return (
        lose[opponent]
        if result == "X"
        else draw[opponent]
        if result == "Y"
        else win[opponent]
    )


with open("../data/day02.txt") as f:
    lines = f.readlines()
    score1 = 0
    score2 = 0

    for line in lines:
        [opp, me] = line.split()
        score1 += score(opp, me)
        score2 += score(opp, move(opp, me))

    print(score1, score2)
