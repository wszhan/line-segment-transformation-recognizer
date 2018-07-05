from line_segment import LineSegment
import math
import numpy as np

class PatternRecognizer:
    def __init__(self, line_segment_1, line_segment_2):
        """
        params:
        - line_segment_1: LineSegment(object)
        """
        self.seg_1_ = line_segment_1
        self.seg_2_ = line_segment_2
        self.transformation_ = None

    """

    Utility Functions

    """

    def pattern(self):
        ## 左端点旋转 ##
        if self.left_point_rotation():
            # 输出角度单位为pi
            return self.included_angle(), "Left Point Rotation"

        ## 右端点旋转 ##
        if self.right_point_rotation():
            return self.included_angle(), "Right Point Rotation"

        ## 伸长 ##
        if self.strenching():
            return None, "Line Strenching"

        ## 缩短 ##
        if self.shrinking():
            return "Line Shrinking"

        ## 平移 ##
        if self.parallel():
            return "Line Parallelly Moving"

    """

    Helper Functions: Patterns

    """

    def left_point_rotation(self):
        if (self.length_compare() == 0 and \
        (self.seg_1_.start_point_ == self.seg_2_.end_point_ or \
            self.start_compare() == 0)):
            return True
        else:
            return False

    def right_point_rotation(self):
        if (self.length_compare() == 0 and \
        (self.seg_1_.end_point_ == self.seg_2_.start_point_ or \
            self.end_compare() == 0)):
            return True
        else:
            return False

    def strenching(self):
        if (self.slope_compare() == 0 and \
            self.slope_intercept_compare() == 0 and \
            self.length_compare() == -1):
            return True
        else:
            return False

    def shrinking(self):
        if (self.slope_compare() == 0 and \
            self.slope_intercept_compare() == 0 and \
            self.length_compare() == 1):
            return True
        else:
            return False

    def parallel(self):
        if (self.slope_compare() == 0 and \
            self.length_compare() == 0 and 
            self.slope_intercept_compare() != 0):
            return True
        else:
            return False

    def included_angle(self):
        v1 = self.seg_1_.vectorized()
        v2 = self.seg_2_.vectorized()

        # length
        cosang = np.dot(v1, v2)
        sinang = np.linalg.norm(np.cross(v1, v2))
        return np.arctan2(sinang, cosang)

    """

    Helper Functions: Compare

    """
    def length_compare(self):
        length_1 = self.seg_1_.length_
        length_2 = self.seg_2_.length_
        if length_1 == length_2:
            return 0
        elif length_1 > length_2:
            return 1
        else:
            return -1

    def slope_compare(self):
        slope_1 = self.seg_1_.slope_
        slope_2 = self.seg_2_.slope_
        if slope_1 == slope_2:
            return 0
        elif slope_1 > slope_2:
            return 1
        else:
            return -1

    def slope_intercept_compare(self):
        intercept_1 = self.seg_1_.intercept_
        intercept_2 = self.seg_2_.intercept_
        if intercept_1 == intercept_2:
            return 0
        elif intercept_1 > intercept_2:
            return 1
        else:
            return -1

    def start_compare(self):
        start_1 = self.seg_1_.start_point_
        start_2 = self.seg_2_.start_point_
        if start_1 == start_2:
            return 0
        elif start_1 > start_2:
            return 1
        else:
            return -1

    def end_compare(self):
        end_1 = self.seg_1_.end_point_
        end_2 = self.seg_2_.end_point_
        if end_1 == end_2:
            return 0
        elif end_1 > end_2:
            return 1
        else:
            return -1