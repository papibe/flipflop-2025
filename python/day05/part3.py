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


def solve(data: str, tunnels: Dict[str, Tunnel]) -> int:
    index: int = 0
    steps: int = 0

    while index < len(data):
        tunnel = data[index]
        entrance = tunnels[tunnel].entrance
        exit_ = tunnels[tunnel].exit

        exit_index = entrance if index == exit_ else exit_
        tunnel_steps: int = abs(exit_index - index)
        if tunnel.isupper():
            steps -= tunnel_steps
        else:
            steps += tunnel_steps
        index = exit_index + 1

    return steps


def solution(filename: str) -> int:
    data, tunnels = parse(filename)
    return solve(data, tunnels)


if __name__ == "__main__":
    print(solution("./example.txt"))  # -6
    print(solution("./input.txt"))  # 251
