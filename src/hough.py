import cv2
import numpy as np


def detect_lines(edge_image):
    """
    Detect line segments using the Probabilistic Hough Transform.
    """

    lines = cv2.HoughLinesP(
        edge_image,
        rho=2,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=40,
        maxLineGap=100,
    )
    return lines


def draw_lines(image, lines):
    line_image = image.copy()

    if lines is None:
        return line_image

    for line in lines:
        x1, y1, x2, y2 = line

        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    return line_image
