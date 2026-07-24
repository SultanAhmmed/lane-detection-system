import cv2

points = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print("Clicked:", x, y)


cap = cv2.VideoCapture("./data/road.mp4")

ret, frame = cap.read()


if ret:
    cv2.imshow("Frame", frame)

    # Attach mouse callback to the window
    cv2.setMouseCallback("Frame", mouse_click)

    while True:
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

cv2.destroyAllWindows()

print("All points:", points)
