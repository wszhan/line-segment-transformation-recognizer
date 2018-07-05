import numpy as np

class LineSegment:
	def __init__(self, p1, p2):
		"""
		params:
		- start point: (x, y)
		- end point: (x, y)
		"""
		comp = self.point_compare(p1, p2)
		if comp == 0:
			raise ValueError("Inputs should be distinct")
		elif comp == 1:
			self.start_point_ = p2
			self.end_point_ = p1
		elif comp == -1:
			self.start_point_ = p1
			self.end_point_ = p2

		self.length_ = self.ls_length()
		self.slope_ = self.ls_slope()
		self.intercept_ = self.ls_intercept()
		self.x_range_ = (min(self.end_point_[0], self.start_point_[0]),
			max(self.end_point_[0], self.start_point_[0]))

	def ls_length(self):
		return np.sqrt(np.square(self.end_point_[1] - self.start_point_[1]) +
			np.square(self.end_point_[0] - self.start_point_[0]))

	def ls_slope(self):
		if self.start_point_[0] == self.end_point_[0]:
			return np.inf
		elif self.start_point_[1] == self.end_point_[1]:
			return 0
		else:
			return float(
				(self.end_point_[1] - self.start_point_[1]) / 
				(self.end_point_[0] - self.start_point_[0])
				)

	def ls_intercept(self):
		return (self.start_point_[1] - self.slope_ * self.start_point_[0])

	def point_compare(self, p1, p2):
		if p1[1] == p2[1] and p1[0] == p2[0]:
			return 0
		elif p1[1] > p2[1]:
			return 1
		elif p1[0] > p2[0]:
			return 1
		else:
			return -1

	def vectorized(self):
		return (self.end_point_[0] - self.start_point_[0],
			self.end_point_[1] - self.start_point_[1])