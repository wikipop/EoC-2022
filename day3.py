from pprint import pprint

s = []

table = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

# with open("3_prompt.txt") as f:
#     for i in f:
#         length = len(i)
#         string1 = i[:int(length/2)]
#         string2 = i[int(length/2):]
#
#         for j in string1:
#             for k in string2:
#                 if j == k:
#                     s.append(j)
#                     break
#             if j == k:
#                 break

# s2 = []
# for i in s:
#     s2.append(table[i])

templist = []

with open("data/3_prompt.txt") as f:
    for i in f:
        templist.append(i.rstrip("\n"))

        if len(templist) == 3:
            s.append(templist)
            templist = []

s2 = []

for i in s:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            s2.append(j)
            break

s3 = []

for i in s2:
    s3.append(table[i])

print(sum(s3))