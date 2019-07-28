from typing import NamedTuple
from typing import List
from typing import Optional
from functools import lru_cache
from fractions import Fraction
import math

class Point(NamedTuple):
	x: Fraction
	y: Fraction

class LineSegment(NamedTuple):
	a: Point
	b: Point

class Line(NamedTuple):
	slope: Fraction
	y_int: Fraction
	x: Optional[int]


def point_falls_on_line(point: Point, line: Line) -> bool:
	if line.x is not None:
		return point.x == line.x

	return line.slope * point.x + line.y_int == point.y


def is_point_above_line(point: Point, line: Line) -> bool:
	if line.x is not None:
		return point.x > line.x

	return line.slope * point.x + line.y_int > point.y


@lru_cache(maxsize=5000)
def get_line(line_segment: LineSegment) -> Line:
	if line_segment.a.x - line_segment.b.x == 0:
		return Line(slope=None,y_int=None,x=line_segment.a.x)

	slope = Fraction(
		line_segment.a.y - line_segment.b.y,
		line_segment.a.x - line_segment.b.x
	)
	y_int = line_segment.a.y - slope * line_segment.a.x
	
	return Line(
		slope=slope,
		y_int=y_int,
		x=None
	)


def get_intersection_point(line_one: Line, line_two: Line) -> Point:
	if line_one.x is not None:
		return Point(
			x=line_one.x,
			y=line_one.x*line_two.slope + line_two.y_int
		)
	if line_two.x is not None:
		return Point(
			x=line_two.x,
			y=line_two.x*line_one.slope + line_one.y_int
		)

	x = (line_two.y_int - line_one.y_int) / (line_one.slope - line_two.slope)
	y = x * line_one.slope + line_one.y_int
	return Point(x=x,y=y)



def get_intersection(line_segment_one: LineSegment, line_segment_two: LineSegment):
	line_one = get_line(line_segment_one)
	line_two = get_line(line_segment_two)

	if point_falls_on_line(point=line_segment_one.a, line=line_two):
		return None
	if point_falls_on_line(point=line_segment_one.b, line=line_two):
		return None
	if point_falls_on_line(point=line_segment_two.a, line=line_one):
		return None
	if point_falls_on_line(point=line_segment_two.b, line=line_one):
		return None

	if (
		is_point_above_line(point=line_segment_one.a, line=line_two) != \
		is_point_above_line(point=line_segment_one.b, line=line_two)
	) and (
		is_point_above_line(point=line_segment_two.a, line=line_one) != \
		is_point_above_line(point=line_segment_two.b, line=line_one)
	):
		return get_intersection_point(line_one, line_two)



def generate_line_segments() -> List[LineSegment]:
	s = [290797]
	t = [290797 % 500]

	segments = []
	for i in range(1, 20001):
		new_s = s[len(s)-1] * s[len(s)-1] % 50515093
		s.append(new_s)
		t.append(new_s % 500)

		if i % 4 == 0:
			segments.append(
				LineSegment(
					a=Point(
						x=t[i-3],
						y=t[i-2]
					),
					b=Point(
						x=t[i-1],
						y=t[i]
					)
				)
			)

	return segments


line_segments = generate_line_segments()
print(len(line_segments))
print(line_segments[0:2])
intersections = set()
for i in range(len(line_segments)):
	if i % 100 == 0:
		print(i)
	for j in range(len(line_segments)):
		if i != j:
			intersection = get_intersection(line_segments[i], line_segments[j])
			if intersection is not None:
				intersections.add(intersection)

print(len(intersections))




