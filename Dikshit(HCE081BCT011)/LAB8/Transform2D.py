import numpy as np
import math

class Transform2D:
    @staticmethod
    def translate(tx, ty):
        return np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ], dtype=float)
        
    @staticmethod
    def scale(sx, sy):
        return np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def rotate(theta_deg):
        t = math.radians(theta_deg)
        return np.array([
            [math.cos(t), -math.sin(t), 0],
            [math.sin(t),  math.cos(t), 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def reflect_x():
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def reflect_y():
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def reflect_origin():
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype=float)

    @staticmethod
    def reflect_y_eq_x():
        return np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ], dtype=float)
    @staticmethod
    def apply(x_coords, y_coords, *composite_matries):
        points = np.vstack([ x_coords, y_coords, np.ones_like(x_coords)])
        transformation_matrix = np.eye(3)
        for composite_matrix in composite_matries:
            transformation_matrix = composite_matrix @ transformation_matrix
        result = transformation_matrix @ points
        return result[0], result[1]


