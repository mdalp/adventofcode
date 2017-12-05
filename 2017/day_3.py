"""
37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49
"""
import math

examples = [
    (1, 0),
    (12, 3),
    (23, 2),
    (26, 5),
    (1024, 31),
]


def size(x):
    round_sqrt = math.ceil(math.sqrt(x))
    return round_sqrt + (1 + round_sqrt) % 2


def radius(x):
    return int(size(x) / 2)


def solution(x):
    if x == 1:
        return 0
    r = radius(x)
    return r + abs(((x - 1) % (r * 2)) - r)


def run_tests():
    for input_, output in examples:
        assert solution(input_) == output


if __name__ == '__main__':
    run_tests()
    print(solution(289326))



