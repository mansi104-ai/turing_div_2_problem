import random

def generate_testcase(n_min=2, n_max=20, a_min=1, a_max=50, p_max=10, seed=None):
    
    if seed is not None:
        random.seed(seed)

    n = random.randint(n_min, n_max)
    p = random.randint(0, p_max)
    a = [random.randint(a_min, a_max) for _ in range(n)]

    # Format as Codeforces input style
    input_str = f"{n} {p}\n" + " ".join(map(str, a)) + "\n"
    return input_str


def generate_multiple_tests(num_tests=10, **kwargs):
    
    tests = []
    for i in range(num_tests):
        tests.append(generate_testcase(seed=i, **kwargs))
    return tests


def save_tests_to_file(filename="testcases.txt", num_tests=10, **kwargs):
    tests = generate_multiple_tests(num_tests, **kwargs)
    with open(filename, "w") as f:
        for t in tests:
            f.write(t + "\n")
    print(f"✅ {num_tests} test cases written to {filename}")


if __name__ == "__main__":
    
    save_tests_to_file("small_tests.txt", num_tests=10, n_max=8, a_max=20, p_max=5)
    save_tests_to_file("large_tests.txt", num_tests=5, n_min=50000, n_max=200000, a_max=10**9, p_max=10**9)
