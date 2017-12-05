example = ("""0
3
0
1
-3""",
    5
)


def solution(input_):
    count = 0
    clean_input = list(map(int, input_.split('\n')))
    idx = 0
    try:
        while True:
            increment = clean_input[idx]
            clean_input[idx] += 1
            idx += increment
            count += 1
    except IndexError:
        return count


def run_tests():
    input_, output = example
    assert solution(input_) == output, solution(input_)


if __name__ == '__main__':
    run_tests()
    with open('day_5.data', 'r') as f:
        print(solution(f.read()))
