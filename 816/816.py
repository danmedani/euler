from typing import NamedTuple
from functools import lru_cache
from typing import List
import math


class Point(NamedTuple):
    x: int
    y: int


def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((abs(p1.x - p2.x) ** 2) + (abs(p1.y - p2.y) ** 2))


@lru_cache(maxsize=1)
def get_s_list() -> List[int]:
    s_list = [290797]
    s = 1
    while s < 4000001:
        s_list.append((s_list[s - 1] ** 2) % 50515093)
        s += 1
    return s_list

def p(n: int) -> Point:
    return Point(x=get_s_list()[n * 2], y=get_s_list()[(n * 2) + 1])

def get_p_list(k: int) -> List[Point]:
    return [p(n) for n in range(k)]

def get_min(d: int) -> float:
    p_list = get_p_list(d)
    p_list.sort(key=lambda point: point.x)
    min_distance = 999999999999
    for i in range(0, d - 1):
        for j in range(i + 1, d):
            if p_list[j].x - p_list[i].x > min_distance:
                break
            dist = distance(p_list[i], p_list[j])
            if dist < min_distance:
                min_distance = dist
    return min_distance

print(get_min(2000000))
