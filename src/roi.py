import numpy as np
import cv2


def region_of_interest(image):
    polygon = np.array(
        [
            [
                (480, 580),  # top-left
                (740, 580),  # top-right
                (890, 700),  # bottom-right
                (310, 700),  # bottom-left
            ]
        ]
    )

    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygon, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked


def draw_roi_overlay(image, edges):
    kernel = np.ones((5,5), np.uint8)
    thrick_edges = cv2.dilate(edges, kernel, iterations=1)

    edge_color = np.zeros_like(image)
    edge_color[thrick_edges > 0] = [0, 0, 255]

    result = cv2.addWeighted(image, 1, edge_color,1, 0)


    return result
