example = ('0   2   7   0', 5)


def _index_max(iterable):
    max_v = max(iterable)
    index = iterable.index(max_v)
    return max_v, index


def solution(input_):
    clean_input = list(map(int, input_.split()))
    input_len = len(clean_input)
    step_solutions = set()
    step_solution = tuple(clean_input)
    while step_solution not in step_solutions:
        step_solutions.add(step_solution)
        max_v, index = _index_max(clean_input)
        clean_input[index] = 0
        increment, mod = divmod(max_v, input_len)
        for i in range(index + 1, input_len + index + 1):
            clean_input[i % input_len] += increment + (1 if mod > 0 else 0)
            mod -= 1
        step_solution = tuple(clean_input)

    return len(step_solutions)


def run_tests():
    input_, output = example
    assert solution(input_) == output, solution(input_)


if __name__ == '__main__':
    run_tests()
    with open('day_6.data', 'r') as f:
        print(solution(f.read()))
