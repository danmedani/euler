from typing import NamedTuple
from typing import List
from typing import Optional
from functools import lru_cache
import math

class Point(NamedTuple):
	x: int
	y: int

class LineSegment(NamedTuple):
	a: Point
	b: Point

class Ratio(NamedTuple):
	num: int
	denom: int

class Line(NamedTuple):
	# denom of slope == denom of y_int
	slope: Ratio
	y_int: Ratio
	x_coordinate: Optional[int]


def add_ratios(ratio_a: Ratio, ratio_b: Ratio) -> Ratio:
	return Ratio(
		num=(ratio_a.num * ratio_b.denom) + (ratio_b.num * ratio_a.denom),
		denom=ratio_a.denom * ratio_b.denom
	)

def subtract_ratios(ratio_a: Ratio, ratio_b: Ratio) -> Ratio:
	return Ratio(
		num=(ratio_a.num * ratio_b.denom) - (ratio_b.num * ratio_a.denom),
		denom=ratio_a.denom * ratio_b.denom
	)

def divide_ratios(ratio_a: Ratio, ratio_b: Ratio) -> Ratio:
	return Ratio(
		num=ratio_a.num * ratio_b.denom,
		denom=ratio_a.denom * ratio_b.num
	)

def point_falls_on_line(point: Point, line: Line) -> bool:
	new_num = (line.slope.num * point.x) + line.y_int.num
	denom = line.slope.denom

	if denom == 0:
		# str8 up and down line
		return point.x == line.x_coordinate

	if new_num % denom != 0:
		return False

	return new_num / denom == point.y


def is_point_above_line(point: Point, line: Line) -> bool:
	new_num = (line.slope.num * point.x) + line.y_int.num
	denom = line.slope.denom

	if denom == 0:
		return point.x > line.x_coordinate

	return 1.0 * new_num / denom < point.y


@lru_cache(maxsize=5000)
def get_line(line_segment: LineSegment) -> Line:
	slope = Ratio(
		num=line_segment.a.y - line_segment.b.y,
		denom=line_segment.a.x - line_segment.b.x
	)
	y_int = Ratio(
		num=(line_segment.a.y * slope.denom) - (line_segment.a.x * slope.num),
		denom=slope.denom
	)
	return Line(
		slope=slope, 
		y_int=y_int,
		x_coordinate=line_segment.a.x if slope.denom == 0 else None
	)


def get_intersection_point(line_one: Line, line_two: Line) -> Point:
	x: Ratio = divide_ratios(
		subtract_ratios(
			line_two.y_int,
			line_one.y_int
		),
		subtract_ratios(
			line_one.slope,
			line_two.slope
		)
	)
	y = add_ratios(
		Ratio(
			num=line_one.slope.num * x.num,
			denom=line_one.slope.denom * x.denom
		),
		line_one.y_int
	)

	gcd_x = math.gcd(x.num, x.denom)
	x_reduced = Ratio(num=x.num/gcd_x if gcd_x != 0 else 0, denom=x.denom/gcd_x if gcd_x != 0 else 0)

	gcd_y = math.gcd(y.num, y.denom)
	y_reduced = Ratio(num=y.num/gcd_y if gcd_y != 0 else 0, denom=y.denom/gcd_y if gcd_y != 0 else 0)

	return Point(
		x=x_reduced,
		y=y_reduced
	)



def get_intersection(line_segment_one: LineSegment, line_segment_two: LineSegment):
	line_one = get_line(line_segment_one)
	line_two = get_line(line_segment_two)

	if point_falls_on_line(point=line_segment_one.a, line=line_two):
		return False
	if point_falls_on_line(point=line_segment_one.b, line=line_two):
		return False
	if point_falls_on_line(point=line_segment_two.a, line=line_one):
		return False
	if point_falls_on_line(point=line_segment_two.b, line=line_one):
		return False

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




