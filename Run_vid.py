import cv2
import numpy as np

def binarize(img):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    binary_h = cv2.inRange(hls, (0, 0, 0), (255, 255, 255))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary_g = cv2.inRange(gray, 230, 255)  # 230

    binary = cv2.bitwise_and(binary_g, binary_h)
    # gaus = cv2.GaussianBlur(binary, (3,3),5) bs4, METHODS
    # canny = cv2.Canny(gaus,270,320)

    # return binary
    return binary

def process_frame(frame):
    binary = binarize(frame)
    binary1 = binary[820:980, 910:940]
    binary2 = binary[820:980, 1080:1110]
    cv2.line(binary, (920, 830), (920, 980), (150, 0, 0), 3)
    cv2.line(binary, (1090, 830), (1090, 980), (150, 0, 0), 3)

    if 255 in binary1:
        print("повернуть налево!")
    else:
        pass
    if 255 in binary2:
        print("повернуть направо!")
    else:
        pass

    frame_re = binary[170:1480, 100:1340]
    cv2.imshow('frame', frame_re)
    # cv2.imshow("Webcam", binary)
    #cv2.imshow("left", binary1)
    #cv2.imshow("right", binary2)

def main():
    cap = cv2.VideoCapture("video.mp4")
    # cap.set(3, 640)
    # cap.set(4, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        process_frame(frame)


        # cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) == 27:
            break

        # binary = binarize(frame)
        #
        # binary1 = binary[300:250 + 210, 210:50 + 190]
        # binary2 = binary[300:250 + 210, 380:50 + 360]
        # left_line = cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
        # right_line = cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)
        #
        # if 255 in binary1:
        #     print("повернуть налево!")
        # else:
        #     pass
        # if 255 in binary2:
        #     print("повернуть направо!")
        # else:
        #     pass
        #
        # cv2.imshow("Webcam", binary)
        # cv2.imshow("left", binary1)
        # cv2.imshow("right", binary2)
    cap.release()
    cv2.destroyAllWindows()

# sftp://192.168.4.4
# pi
# raspberry
# 22
if __name__ == "__main__":
    main()

