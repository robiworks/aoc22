import numpy as np

with open("../data/day08.txt", "r") as f:
    height_map = np.array([list(map(int, l.strip())) for l in f.readlines()])

    visible = 2 * (height_map.shape[0] + height_map.shape[1]) - 4

    for y in range(1, height_map.shape[0] - 1):
        for x in range(1, height_map.shape[1] - 1):
            h = height_map[y, x]

            if (
                np.count_nonzero(height_map[y, :x] >= h) == 0
                or np.count_nonzero(height_map[y, x + 1 :] >= h) == 0
                or np.count_nonzero(height_map[:y, x] >= h) == 0
                or np.count_nonzero(height_map[y + 1 :, x] >= h) == 0
            ):
                visible += 1

    print(visible)
