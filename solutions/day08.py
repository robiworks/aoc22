import numpy as np

with open("../data/day08.txt", "r") as f:
    height_map = np.array([list(map(int, l.strip())) for l in f.readlines()])

    visible = 2 * (height_map.shape[0] + height_map.shape[1]) - 4
    scenic = 0

    for y in range(1, height_map.shape[0] - 1):
        for x in range(1, height_map.shape[1] - 1):
            h = height_map[y, x]

            l = np.count_nonzero(height_map[y, :x] >= h)
            r = np.count_nonzero(height_map[y, x + 1 :] >= h)
            u = np.count_nonzero(height_map[:y, x] >= h)
            d = np.count_nonzero(height_map[y + 1 :, x] >= h)

            li = np.argwhere(height_map[y, :x] >= h)
            li = x - li[-1][0] if li.size > 0 else x

            ri = np.argwhere(height_map[y, x + 1 :] >= h)
            ri = ri[0][0] + 1 if ri.size > 0 else height_map.shape[1] - x - 1

            ui = np.argwhere(height_map[:y, x] >= h)
            ui = y - ui[-1][0] if ui.size > 0 else y

            di = np.argwhere(height_map[y + 1 :, x] >= h)
            di = di[0][0] + 1 if di.size > 0 else height_map.shape[0] - y - 1

            if l == 0 or r == 0 or u == 0 or d == 0:
                visible += 1

            scenic = li * ri * ui * di if li * ri * ui * di > scenic else scenic

    print(visible, scenic)
