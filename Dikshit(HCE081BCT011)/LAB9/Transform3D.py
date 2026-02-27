import numpy as np
import math

class Transform3D:
    @staticmethod
    def translate(tx=0, ty=0, tz=0):
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ], dtype=float)
        
    @staticmethod
    def scale(sx = 1, sy = 1, sz = 1):
        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ], dtype=float)

    @staticmethod
    def rotate_about_z(theta_deg):
        t = math.radians(theta_deg)
        return np.array([
            [math.cos(t), -math.sin(t), 0, 0],
            [math.sin(t),  math.cos(t), 0, 0],
            [0,             0,          1, 0],
            [0,             0,          0, 1]
        ], dtype=float)

    @staticmethod
    def rotate_about_y(theta_deg):
        t = math.radians(theta_deg)
        return np.array([
            [math.cos(t), 0, math.sin(t), 0],
            [0,            1,           0, 0],
            [-math.sin(t), 0, math.cos(t), 0],
            [0,             0,          0, 1]
        ], dtype=float)
    
    @staticmethod
    def rotate_about_x(theta_deg):
        t = math.radians(theta_deg)
        return np.array([
            [1,             0,          0, 0],
            [0, math.cos(t), -math.sin(t), 0],
            [0, math.sin(t),  math.cos(t), 0],
            [0,             0,          0, 1]
        ], dtype=float)

    @staticmethod
    def reflect_xy():
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1,0],
            [0, 0, 0, 1],
        ], dtype=float)

    @staticmethod
    def reflect_yz():
        return np.array([
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ], dtype=float)

    @staticmethod
    def apply(x_coords, y_coords, z_coords, *composite_matries):
        points = np.vstack([ x_coords, y_coords, z_coords, np.ones_like(x_coords)])
        transformation_matrix = np.eye(4)
        for composite_matrix in composite_matries:
            transformation_matrix = composite_matrix @ transformation_matrix
        result = transformation_matrix @ points
        return result[0], result[1], result[2]
