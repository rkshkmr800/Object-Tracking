import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    color = cv2.cvtColor(frame, 1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # draw random rectangle
    cv2.rectangle(gray, (50,50),(100,150), (0,255,0), 2)

    # binarize the image
    ret, bw = cv2.threshold(gray, 128, 255, (cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU))

    connectivity = 4
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(bw, connectivity, cv2.CV_32S)

    sizes = stats[1:, -1]
    nb_components = nb_components - 1

    print(stats)
    print(sizes)

    for i in range(0, nb_components+1):

        # draw the bounding rectangele around each object
        cv2.rectangle(gray, (stats[i][0],stats[i][1]),(stats[i][0]+stats[i][2],stats[i][1]+stats[i][3]), (0,255,0), 2)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()