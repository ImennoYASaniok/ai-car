import cv2
import numpy as np
from driving_on_the_road import *
from func import *

left = 0
right = 0

def process_frame(frame):
    binary = binarize(frame)
    binary1 = binary[300:250 + 210, 210:50 + 190]
    binary2 = binary[300:250 + 210, 380:50 + 360]
    cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
    cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)
    # left_line = cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
    # right_line = cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)

    if 255 in binary1:
        print("повернуть налево!")
        left = 1
    else:
        pass
    if 255 in binary2:
        print("повернуть направо!")
        right = 1
    else:
        pass

    if right == 1:
        control(pi, ESC, 1550, STEER, 90 + 7)
    elif left == 1:
        control(pi, ESC, 1550, STEER, 90 - 7)
    else:
        control(pi, ESC, 1550, STEER, 90)


    cv2.imshow("Webcam", binary)
    cv2.imshow("left", binary1)
    cv2.imshow("right", binary2)

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
                print("CFPS : " + str(25.0 / (newTimej - lastTimej)))
                lastTimej = newTimej
                j = 0

            # img = cv.resize(frame, SIZE)
            #binary = binarize(img)
            #perspective = trans_perspective(binary, TRAP, RECT, SIZE)

            # left, right = find_left_right(perspective)
            # print(left, right)
            ret, frame = cap.read()
            if not ret:
                break

            process_frame(frame)

            if cv2.waitKey(1) == 27:
                break

        except KeyboardInterrupt:
            control(pi, ESC, 1500, STEER, 90)
            # останавливаем двигатель
            break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
