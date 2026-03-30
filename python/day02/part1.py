UP: str = "^"
DOWN: str = "v"


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

    return data


def solve(data: str) -> int:
    height: int = 0

    max_height: int = 0
    for char in data:
        if char == UP:
            height += 1
        elif char == DOWN:
            height -= 1

        max_height = max(max_height, height)

    return max_height


def solution(filename: str) -> int:
    data: str = parse(filename)
    return solve(data)


if __name__ == "__main__":
    print(solution("./example1.txt"))  # 1
    print(solution("./example2.txt"))  # 6
    print(solution("./input.txt"))  # 145
