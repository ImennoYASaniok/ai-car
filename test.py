import cv2
import numpy as np
from driving_on_the_road import *
from func import *
def process_frame(frame):
    binary = binarize(frame)
    binary1 = binary[300:250 + 210, 210:50 + 190]
    binary2 = binary[300:250 + 210, 380:50 + 360]
    cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
    cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)
    if 255 in binary1:
        print("повернуть налево!")
        control(pi, ESC, 1550, STEER, 90 - 7)
    elif 255 in binary2:
        print("повернуть направо!")
        control(pi, ESC, 1550, STEER, 90 + 7)
    else:
        control(pi, ESC, 1550, STEER, 90)
    cv2.imshow("Webcam", binary)
def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        try:
            frame = VS.read()
            j += 1
            if j > 25:
                newTimej = time.time()
                lastTimej = newTimej
                j = 0
            ret, frame = cap.read()
            if not ret:
                break
            process_frame(frame)
            if cv2.waitKey(1) == 27:
                break
        except KeyboardInterrupt:
            control(pi, ESC, 1500, STEER, 90)
            break
        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main()