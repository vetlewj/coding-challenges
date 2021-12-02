input_list = []
with open('input/01') as f:
    for line in f:
        input_list.append(int(line.rstrip()))


def get_count(list_to_count):
    inc_count = 0
    for i, j in enumerate(list_to_count):
        if i > 0:
            if j > list_to_count[i - 1]:
                inc_count += 1

    print(inc_count)


def get_three_measurement_windows(inp_list):
    three_mw_list = []
    for i in range(len(inp_list)):
        if i < len(inp_list) - 2:
            three_mw_list.append(inp_list[i] + inp_list[i + 1] + inp_list[i + 2])
    return three_mw_list


if __name__ == '__main__':
    get_count(input_list)
    get_count(get_three_measurement_windows(input_list))
