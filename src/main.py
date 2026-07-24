import cv2
from cvzone.Utils import stackImages
from roi import region_of_interest, draw_roi_overlay
from hough import detect_lines, draw_lines


cap = cv2.VideoCapture("./data/road.mp4")

if not cap.isOpened():
    print("Video failed to load!")

while True:
    ret, image = cap.read()
    img = image.copy()

    if not ret:
        print("Frame failed to read!")
        break

    gray_video = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_video = cv2.GaussianBlur(gray_video, (5, 5), 0)
    edges_video = cv2.Canny(blur_video, 50, 150)

    roi_edges = region_of_interest(edges_video)
    roi_result = draw_roi_overlay(image, roi_edges)

    hough_lines = detect_lines(roi_edges)
    hough_result = draw_lines(image, hough_lines)

    cv2.putText(hough_result, "HUGH Line algorithm",(50,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),1)
    cv2.putText(roi_result, "ROI algorithm",(50,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),1)

    combined = stackImages([roi_result, hough_result], 2, 0.5)
    image = cv2.resize(combined,(1200, 600))

    cv2.imshow("Only ROI VS With HOUGH", image)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

