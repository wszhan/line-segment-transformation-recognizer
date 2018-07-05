#  Line Segment Transformation Recognizer

This is an interview mini project.

Given two line segments in the coordinates, the transformation from one to the other could be identified and returned. For rotation around the start/end point of either line segment, an additional included angle would also be returned.

## Line Segment

A line segment should be constructed using the LineSegment object inside the file of line_segment.py, which takes two points as initial arguments. These two points should be distinct, otherwise an error would be raised since two identical points don't make a segment.

## Pattern Recognizer

A PatternRecognizer takes two LineSegment objects as input and return the transformation type. As aforementioned, for rotation around the start/end point of either line segment, an additional included angle would also be returned.