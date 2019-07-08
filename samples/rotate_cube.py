import cv2
import numpy as np
from math import radians, cos, sin

def rotate_points(points, r, p, y):
	pass


def projected_points(rotated_points):
	pass


points = np.array([[0,0,0], [0,1,0], [1,1,0], [1,0,0],
                   [0,0,0], [0,1,1], [1,1,1], [1,0,1]])

points *= 50
points += 100

canvas = np.zeros((500, 500), dtype=np.uint8)
h,w = canvas.shape[:2]
center = (w/2, h/2)
color = (255,0,0)

i = 0
while True:
	rotated_points = rotate_points(points, r, p, y)
	projected_points = project_points(rotated_points)
    for p in points:
        cv2.circle(canvas, tuple(p[:2]), 7, color, -1)
    cv2.imshow('canvas', canvas)
    if cv2.waitKey(10) > 0:
        break
    canvas[:, :] = 0
    i = (i + 1) % 360
    
cv2.destroyAllWindows(0)
