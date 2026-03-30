from typing import Dict, Optional

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
    repetitions: int = 0
    previous: Optional[str] = None

    for char in data:
        if char == previous:
            repetitions += 1
        else:
            repetitions = 1

        if char == UP:
            height += repetitions
        elif char == DOWN:
            height -= repetitions

        max_height = max(max_height, height)
        previous = char

    return max_height


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example3.txt"))  # 15
    print(solution("./example2.txt"))  # 15
    print(solution("./input.txt"))  # 1971
