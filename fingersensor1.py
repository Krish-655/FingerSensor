import cv2
import numpy as np
import mediapipe as mp
import os

wCam, hCam = 2800, 2800
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinate = (4,2)


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        handPoints = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):
                # print(idx,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handPoints.append((cx, cy))

        for point in handPoints:
            cv2.circle(img, point, 10, (0, 0, 255), cv2.FILLED)

        upCount = 0
        for coordinate in fingerCoordinates:
            if handPoints[coordinate[0]][1] < handPoints[coordinate[1]][1]:
                upCount += 1
        if handPoints[thumbCoordinate[0]][0] > handPoints[thumbCoordinate[1]][0]:
            upCount += 1
        
        if upCount == 1:
            cap = cv2.VideoCapture(0)
            while True:
                
                r,frame = cap.read()
                if r == True:
                     frame = cv2.resize(frame,(700,700))
                     cv2.imshow("krish",frame)
                     cv2.imwrite(r"C:\Users\HP\OneDrive\Desktop\images\new_image1.jpg",frame)
        
                if (cv2.waitKey(1) & 0xff == ord("p")):
                     break
                else :
                    break
            cap.release()
            #cv2.destroyAllWindows()

        if upCount == 2:
            import cv2
            cam = cv2.VideoCapture(0)
            frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

            while True:
                ret, frame = cam.read()

                cv2.imshow('Camera', frame)

                if cv2.waitKey(1) == ord('q'):
                    break

            cam.release()
            cv2.destroyAllWindows()
     

        if upCount==3:
            import os
            list_name = os.listdir(r"C:\Users\HP\OneDrive\Desktop\images")
            list_name
            for name in list_name:
                path = "C:\\Users\\HP\\OneDrive\\Desktop\\images" 
                img_name = path + "\\" + name
                imgs = cv2.imread(img_name)
                res_img = cv2.resize(imgs,(900,1000))
                cv2.imshow("krish3",res_img)
                cv2.waitKey(0)
        
        if upCount == 4:
            
            cap = cv2.VideoCapture(r'C:\Users\HP\OneDrive\Desktop\0pencv\loops.mp4')
            if (cap.isOpened()== False):
                print("Error opening video file")
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    cv2.imshow('Frame', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
 
                        

                else:
                    break

            cap.release()

        if upCount == 5:
            cv2.putText(img, str("welcome to finger sensor model"), (50,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            cv2.waitKey(25)
                        
  
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1) 
          