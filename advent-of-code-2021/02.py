test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def move_submarine(inp):
    l = []
    for i in inp:
        split_string = i.split(' ')
        l.append(dict({split_string[0]: int(split_string[1])}))
    horizontal_pos = 0
    depth = 0
    for i in range(len(l)):
        if l[i].get('forward'):
            horizontal_pos += l[i]['forward']
        elif l[i].get('up'):
            depth -= l[i]['up']
        elif l[i].get('down'):
            depth += l[i]['down']

    return horizontal_pos * depth


def move_submarine_with_aim(inp):
    l = []
    for i in inp:
        split_string = i.split(' ')
        l.append(dict({split_string[0]: int(split_string[1])}))
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in range(len(l)):
        if l[i].get('forward'):
            horizontal_pos += l[i]['forward']
            depth += aim * l[i]['forward']
        elif l[i].get('up'):
            aim -= l[i]['up']
        elif l[i].get('down'):
            aim += l[i]['down']

    return horizontal_pos * depth


def test_moving_submarine():
    assert move_submarine(test_data.split('\n')) == 150


def test_moving_submarine_with_aim():
    assert move_submarine_with_aim(test_data.split('\n')) == 900


if __name__ == '__main__':
    with open('input/02') as f:
        inp = f.read().split("\n")
        print(move_submarine(inp))
        print(move_submarine_with_aim(inp))
