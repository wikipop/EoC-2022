s = 0

with open("data/4_prompt.txt") as f:
    for i in f:
        elf1, elf2 = i.rstrip("\n").split(",")
        elf1, elf2 = elf1.split("-"), elf2.split("-")
        elf1, elf2 = range(int(elf1[0]), int(elf1[1]) + 1), range(int(elf2[0]), int(elf2[1]) + 1)
        elf1, elf2 = set(elf1), set(elf2)
        print(elf1, elf2)

        # if elf1.issubset(elf2) or elf2.issubset(elf1):
        #     s += 1

        if elf1.intersection(elf2) or elf2.intersection(elf1):
            s += 1

print(s)