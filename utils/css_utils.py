import math


def get_rotation_angle(transform_str):
    if "matrix" in transform_str:
        values = transform_str.replace("matrix(", "").replace(")", "").split(",")
        a, b = float(values[0]), float(values[1])
        angle = round(math.degrees(math.atan2(b, a)))
        return angle
    return 0
