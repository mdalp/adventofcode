example = (
    """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa""",
    2
)


def solution(x):
    valid_count = 0
    for row in x.split('\n'):
        line = row.split()
        line_set = set()
        for word in line:
            if word in line_set:
                break
            line_set.add(word)
        else:
            valid_count += 1
    return valid_count


def run_tests():
    input_, output = example
    assert solution(input_) == output


if __name__ == '__main__':
    run_tests()
    with open('day_4.data', 'r') as f:
        print(solution(f.read()))
