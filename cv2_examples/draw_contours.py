import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    color = cv2.cvtColor(frame, 1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(color, 30, 200)
    
    # Finding Contours
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    #cv2.imshow('Canny Edges After Contouring', edged)
    
    print("Number of Contours found = " + str(len(contours)))
    
    # Draw all contours
    # -1 signifies drawing all contours
    for c in contours:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 300:
            continue
        
        box = cv2.minAreaRect(c)
        box = cv2.boxPoints(box)
        
        print(box)
        #cv2.drawContours(color, c, -1, (0, 255, 0), 3)
        # draw the bounding rectangele around each object
        cv2.rectangle(color, (box[0][0],box[0][1]),(box[2][0],box[2][1]), (0,255,0), 2)

    # Display the resulting frame
    cv2.imshow('frame',color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()