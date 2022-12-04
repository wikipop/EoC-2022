cal_list: [list[int]] = []
cal_sum_list: [int] = []
temp_list: [int] = []

with open('data/1_prompt.txt') as f:
    for i in f:
        if i.rstrip("\n") != '':
            temp_list.append(int(i.rstrip("\n")))
        else:
            cal_list.append(temp_list)
            temp_list = []

for i in cal_list:
    cal_sum_list.append(sum(i))

three_biggest = []
for i in range(3):
    biggest = max(cal_sum_list)
    three_biggest.append(biggest)

    cal_sum_list.pop(cal_sum_list.index(biggest))

print(sum(three_biggest))