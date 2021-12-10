import collections

test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def get_gamma_and_epsilon_rating(inp_list):
    gamma_rate = ''
    epsilon_rate = ''
    for col in range(len(inp_list[0])):
        most_common_in_col = get_most_common_in_column(inp_list, col)
        gamma_rate += most_common_in_col[0][0]
        epsilon_rate += most_common_in_col[1][0]
    return {'gamma_rate': gamma_rate, 'epsilon_rate': epsilon_rate}


def get_power_consumption(inp_list):
    ret_dict = get_gamma_and_epsilon_rating(inp_list)
    return int(ret_dict['gamma_rate'], 2) * int(ret_dict['epsilon_rate'], 2)


def test_get_power_consumption():
    assert get_power_consumption(test_data.split('\n')) == 198


def get_most_common_in_column(rows, column):
    col_nums = []
    for row in rows:
        col_nums.append(row[column])
    return collections.Counter(col_nums).most_common(2)


def get_life_rating(inp_list, oxygen):
    ret_list = inp_list.copy()
    for col in range(len(ret_list[0])):
        if len(ret_list) > 1:
            most_common = get_most_common_in_column(ret_list, col)
            if len(most_common) > 1:
                if oxygen:
                    if most_common[0][1] == most_common[1][1]:
                        most_common = '1'
                    else:
                        most_common = most_common[0][0]
                else:
                    if most_common[0][1] == most_common[1][1]:
                        most_common = '0'
                    else:
                        most_common = most_common[-1][0]
            else:
                most_common = most_common[0][0]
            ret_list = [row for row in ret_list if row[col] == most_common]
    return ret_list[0]


def get_life_support_rating(inp_list):
    oxygen_rating = get_life_rating(inp_list, True)
    co2_rating = get_life_rating(inp_list, False)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


def test_get_life_support_rating():
    assert get_life_support_rating(test_data.split('\n')) == 230


if __name__ == '__main__':
    with open('input/03') as f:
        inp = f.read().split('\n')
        print(get_power_consumption(inp))
        print(get_life_support_rating(inp))
