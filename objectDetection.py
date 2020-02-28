import numpy as np
import cv2
import pyautogui as pag


class ObjectDetection:
    LowerColor = np.array([88, 131, 82])
    UpperColor = np.array([111, 255, 255])
    kernel = np.ones((5, 5), np.uint8)
    camera = cv2.VideoCapture(0)

    def detect(self):
        while True:
            # Grab the current paintWindow
            (grabbed, frame) = self.camera.read()
            frame = cv2.flip(frame, 1)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Check to see if we have reached the end of the video
            if not grabbed:
                break
            width = int(self.camera.get(3))
            height = int(self.camera.get(4))
            p1 = (width // 15, height // 6)
            p2 = (14 * width // 15, 5 * height // 6)
            cv2.rectangle(frame, p1, p2, (0, 0, 0), 2)
            # Determine which pixels fall within the blue boundaries and then blur the binary image
            blueMask = cv2.inRange(hsv, self.LowerColor, self.UpperColor)
            blueMask = cv2.erode(blueMask, self.kernel, iterations=2)
            blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, self.kernel)
            blueMask = cv2.dilate(blueMask, self.kernel, iterations=1)

            # Find contours in the image
            (cnts, _) = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

            # Check to see if any contours were found
            if len(cnts) > 0:
                # Sort the contours and find the largest one -- we
                # will assume this contour correspondes to the area of the bottle cap
                cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
                # Get the radius of the enclosing circle around the found contour
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                # Draw the circle around the contour
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                if int(x) > 14 * width // 15:
                    x = 14 * width // 15
                elif int(x) < width // 15:
                    x = width // 15
                elif int(y) > 5 * height // 6:
                    y = 5 * height // 6
                elif int(y) < height // 6:
                    y = height // 6
                screenX, screenY = pag.size()
                pag.FAILSAFE = False
                pag.moveTo((int(x) - (width // 15)) * screenX // (13 * width // 15)
                           , (int(y) - (height // 6)) * screenY // (4 * height // 6))

                print(pag.size())
                print("coordinates : "
                      , int(x) - (width // 15) * screenX // (13 * width // 15)
                      , int(y) - (height // 6) * screenY // (4 * height // 6))
                # Get the moments to calculate the center of the contour (in this case Circle)
                M = cv2.moments(cnt)
                center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

            # Show the frame and the paintWindow image
            cv2.imshow("Tracking", frame)

            # If the 'q' key is pressed, stop the loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Cleanup the camera and close any open windows
        self.camera.release()
        cv2.destroyAllWindows()
