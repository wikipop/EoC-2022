s = 0


def checkComp(they_play, me_p) -> int:
    """
    :return: Punkty za rozdanie
    """

    if they_play == "A":
        if me_p == "X":
            return 3
        elif me_p == "Y":
            return 6
        elif me_p == "Z":
            return 0
    elif they_play == "B":
        if me_p == "X":
            return 0
        elif me_p == "Y":
            return 3
        elif me_p == "Z":
            return 6
    elif they_play == "C":
        if me_p == "X":
            return 6
        elif me_p == "Y":
            return 0
        elif me_p == "Z":
            return 3


def checkComp2(they_play, expected) -> int:
    if they_play == "A":
        if expected == "X":
            return 0 + 3
        elif expected == "Y":
            return 3 + 1
        elif expected == "Z":
            return 6 + 2
    elif they_play == "B":
        if expected == "X":
            return 0 + 1
        elif expected == "Y":
            return 3 + 2
        elif expected == "Z":
            return 6 + 3
    elif they_play == "C":
        if expected == "X":
            return 0 + 2
        elif expected == "Y":
            return 3 + 3
        elif expected == "Z":
            return 6 + 1


with open("data/2_prompt.txt") as f:
    for i in f:
        temp_points = 0
        they, must = i.split()

        temp_points += checkComp2(they, must)

        s += temp_points

print(s)
