from typing import List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def solve(data: List[str]) -> int:
    total_sum: int = 0

    for banana in data:
        total_sum += banana.count("ba")
        total_sum += banana.count("na")
        total_sum += banana.count("ne")

    return total_sum


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 24
    print(solution("./input.txt"))  # 10459
