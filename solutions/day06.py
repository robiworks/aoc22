with open("../data/day06.txt", "r") as f:
    buffer = f.readline().strip()

    found_marker = False
    found_message = False

    for i in range(len(buffer)):
        marker = buffer[i : i + 4]
        message = buffer[i : i + 14]
        s = {c for c in marker}
        m = {c for c in message}

        if len(s) == 4 and not found_marker:
            print("Marker", i + 4)
            found_marker = True

        if len(m) == 14 and not found_message:
            print("Message", i + 14)
            found_message = True

        if found_message and found_marker:
            break
