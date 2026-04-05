from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class Tunnel:
    entrance: int
    exit: int


def parse(filename: str) -> Tuple[str, Dict[str, Tunnel]]:
    with open(filename, "r") as fp:
        data: str = fp.read().strip()

    tunnels: Dict[str, Tunnel] = {}
    for i, char in enumerate(data):
        if char not in tunnels:
            tunnels[char] = Tunnel(i, 0)
        else:
            tunnels[char].exit = i

    return data, tunnels


def solve(data: str, tunnels: Dict[str, Tunnel]) -> str:
    index: int = 0
    steps: int = 0

    visited = {tunnel: False for tunnel in tunnels}

    while index < len(data):
        tunnel = data[index]
        visited[tunnel] = True
        entrance = tunnels[tunnel].entrance
        exit_ = tunnels[tunnel].exit

        exit_index = entrance if index == exit_ else exit_
        steps += abs(exit_index - index)
        index = exit_index + 1

    not_visited = [tunnel for tunnel, is_visited in visited.items() if not is_visited]

    return "".join(not_visited)


def solution(filename: str) -> str:
    data, tunnels = parse(filename)
    return solve(data, tunnels)


if __name__ == "__main__":
    print(solution("./example.txt"))  # "Bc"
    print(solution("./input.txt"))  # "eBnXhWDRUCbVZw"
