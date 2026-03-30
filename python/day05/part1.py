import re
from collections import deque, defaultdict, namedtuple
from dataclasses import dataclass
from typing import Deque, Dict, List, Match, Optional, Set, Tuple

Tunnel = namedtuple("Tunnel", ["entrance", "exit"])

def parse(filename: str) -> List[str]:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().strip()

    tunnels_ = {}
    for i, char in enumerate(data):
        if char not in tunnels_:
            tunnels_[char] = []
        tunnels_[char].append(i)

    # for k, v in tunnels.items():
    #     print(k, v)

    tunnels = {}
    for k, v in tunnels_.items():
        tunnels[k] = Tunnel(v[0], v[1])

    return data, tunnels


def solve(data: List[str], tunnels) -> int:
    index: int = 0
    steps: int = 0

    while index < len(data):
        tunnel = data[index]
        entrance = tunnels[tunnel].entrance
        exit_ = tunnels[tunnel].exit

        exit_index = entrance if index == exit_ else exit_
        steps += abs(exit_index - index)
        index = exit_index + 1

    return steps


def solution(filename: str) -> int:
    data, tunnels = parse(filename)
    return solve(data, tunnels)


if __name__ == "__main__":
    print(solution("./example.txt"))  # 38
    print(solution("./input.txt"))  # 1955
