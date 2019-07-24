from typing import NamedTuple

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


def point_falls_on_line(point: Point, line: Line) -> bool:
	new_num = (line.slope.num * point.x) + line.y_int.num
	denom = line.slope.denom

	if new_num % denom != 0:
		return False

	return new_num / denom == point.y


def is_point_above_line(point: Point, line: Line) -> bool:
	new_num = (line.slope.num * point.x) + line.y_int.num
	denom = line.slope.denom

	return 1.0 * new_num / denom < point.y


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
		y_int=y_int
	)


def has_intersection(line_segment_one: LineSegment, line_segment_two: LineSegment) -> bool:
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

	return \
		(
			is_point_above_line(point=line_segment_one.a, line=line_two) != \
			is_point_above_line(point=line_segment_one.b, line=line_two)
		) and (
			is_point_above_line(point=line_segment_two.a, line=line_one) != \
			is_point_above_line(point=line_segment_two.b, line=line_one)
		)



print(
	has_intersection(
		LineSegment(
			a=Point(x=46, y=70),
			b=Point(x=15, y=30)
		),
		LineSegment(
			a=Point(x=27, y=44),
			b=Point(x=12, y=32)
		)
	)
)
