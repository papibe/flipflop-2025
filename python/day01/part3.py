from typing import List


def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    return data


def solve(data: List[str]) -> int:
    total_sum: int = 0

    for banana in data:
        points = banana.count("ne")
        if points > 0:
            continue
        points += banana.count("ba")
        points += banana.count("na")

        total_sum += points

    return total_sum


def solution(filename: str) -> int:
    data: List[str] = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 19
    print(solution("./input.txt"))  # 3161
