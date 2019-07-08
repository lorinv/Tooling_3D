import cv2
import numpy as np
from math import radians, cos, sin

def rotate_point(points, rotation_center, rot_deg):
    angle = radians(rot_deg)
    x, y = rotation_center
    #points = np.hstack((points, np.array([0] * points.shape[0]).T))
    transform = np.array([[cos(angle),-sin(angle),-x * cos(angle) + y * sin(angle) + x],
                          [sin(angle), cos(angle), -x * sin(angle) - y * cos(angle) + y], 
                          [0,0,1]])
    t_p = np.dot(transform, np.array(points).T).T
    return t_p.astype(np.int16)

canvas = np.zeros((500, 500), dtype=np.uint8)
h,w = canvas.shape[:2]
center = (w/2, h/2)

points = []
num = 16
for i in range(num):
    points.append(rotate_point(np.array([400, 400, 1]), center, i*(360/num)))

i = 0
while True:
    if i < 360:
        color = 255
    else:
        color = 0
    next_points = rotate_point(points, center, i)
    for p in next_points:
        cv2.circle(canvas, tuple(p[:2]), 7, color, -1)
    cv2.imshow('canvas', canvas)
    if cv2.waitKey(10) > 0:
        break
    if i < 180:
        canvas[:, :] = 0
    i = (i + 1) % 720
    
cv2.destroyAllWindows(0)
