example = ('0   2   7   0', 5, 4)

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


def solution2(input_):
    clean_input = list(map(int, input_.split()))
    input_len = len(clean_input)
    step_solutions = {}
    step_solution = tuple(clean_input)
    n_iter = 0
    while step_solution not in step_solutions:
        step_solutions[step_solution] = n_iter
        n_iter += 1
        max_v, index = _index_max(clean_input)
        clean_input[index] = 0
        increment, mod = divmod(max_v, input_len)
        for i in range(index + 1, input_len + index + 1):
            clean_input[i % input_len] += increment + (1 if mod > 0 else 0)
            mod -= 1
        step_solution = tuple(clean_input)

    return n_iter - step_solutions[step_solution]


def run_tests():
    input_, output1, output2 = example
    assert solution(input_) == output1, solution(input_)
    assert solution2(input_) == output2, solution2(input_)


if __name__ == '__main__':
    run_tests()
    with open('day_6.data', 'r') as f:
        input_ = f.read()
    print(solution(input_))
    print(solution2(input_))
