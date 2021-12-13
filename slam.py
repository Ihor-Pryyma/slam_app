import cv2

from display import Display

WIDTH = 1920 // 2
HEIGHT = 1080 // 2
screen = Display(WIDTH, HEIGHT)


def process_frame(img):
    img = cv2.resize(img, (WIDTH, HEIGHT))
    screen.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break
