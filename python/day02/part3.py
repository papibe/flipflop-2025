from typing import Dict

UP: str = "^"
DOWN: str = "v"


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

    return data


memo: Dict[int, int] = {}


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


def solve(data: str) -> int:
    height: int = 0
    max_height: int = 0

    index: int = 0
    while index < len(data):
        j: int = index
        n: int = 0
        while j < len(data) and data[j] == data[index]:
            j += 1
            n += 1

        if data[index] == UP:
            height += fibonacci(n)

        elif data[index] == DOWN:
            height -= fibonacci(n)

        max_height = max(max_height, height)
        index = j

    return max_height


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example3.txt"))  # 5
    print(solution("./example2.txt"))  # 4
    print(solution("./example4.txt"))  # 144
    print(solution("./input.txt"))  # 49475
